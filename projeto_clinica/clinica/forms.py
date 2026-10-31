from django import forms
from .models import Especialidade, Medico, Paciente, Relatorio, Exame


# ===================== Pessoa A =====================

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
        # só mostrar exames que ainda não têm relatório
        # (ao editar, incluir também o exame deste relatório)
        exames = Exame.objects.filter(relatorio__isnull=True)
        if self.instance.pk:
            exames = exames | Exame.objects.filter(pk=self.instance.exame_id)
        self.fields['exame'].queryset = exames


# ===================== Pessoa B =====================