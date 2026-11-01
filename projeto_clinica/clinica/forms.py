from django import forms
from .models import (Especialidade, Medico, Paciente, Relatorio,
                     TipoExame, Equipamento, Exame)


class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'num_cedula', 'especialidade', 'email', 'telefone', 'foto']


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'num_utente', 'data_nascimento', 'sexo', 'telefone', 'morada']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = ['exame', 'medico', 'data', 'texto', 'conclusao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # só mostrar exames realizados que ainda não têm relatório
        # (ao editar, incluir também o exame deste relatório)
        exames = Exame.objects.filter(relatorio__isnull=True, estado='realizado')
        if self.instance.pk:
            exames = exames | Exame.objects.filter(pk=self.instance.exame_id)
        self.fields['exame'].queryset = exames


class TipoExameForm(forms.ModelForm):
    class Meta:
        model = TipoExame
        fields = ['nome', 'descricao', 'duracao_min', 'preco']


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'fabricante', 'modelo', 'num_serie', 'data_aquisicao',
                  'sala', 'tipos_exame', 'foto']
        widgets = {
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            # N:N mostrada como caixas para marcar
            'tipos_exame': forms.CheckboxSelectMultiple,
        }


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['paciente', 'tipo_exame', 'equipamento', 'data', 'estado',
                  'observacoes', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean(self):
        # o equipamento escolhido tem de fazer o tipo de exame escolhido (usa a N:N)
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo_exame')
        equipamento = cleaned_data.get('equipamento')
        if tipo and equipamento and not equipamento.tipos_exame.filter(pk=tipo.pk).exists():
            self.add_error('equipamento',
                           f'O equipamento "{equipamento}" não faz exames do tipo "{tipo}".')
        return cleaned_data