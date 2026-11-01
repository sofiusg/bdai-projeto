from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models import Q, ProtectedError
from .models import (Especialidade, Medico, Paciente, Relatorio,
                     TipoExame, Equipamento, Exame)
from .forms import (EspecialidadeForm, MedicoForm, PacienteForm, RelatorioForm,
                    TipoExameForm, EquipamentoForm, ExameForm)


# ===================== Página inicial =====================

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contagens"] = [
            ("Especialidades", Especialidade.objects.count(), "especialidade_list"),
            ("Médicos", Medico.objects.count(), "medico_list"),
            ("Pacientes", Paciente.objects.count(), "paciente_list"),
            ("Relatórios", Relatorio.objects.count(), "relatorio_list"),
            ("Tipos de exame", TipoExame.objects.count(), "tipoexame_list"),
            ("Equipamentos", Equipamento.objects.count(), "equipamento_list"),
            ("Exames", Exame.objects.count(), "exame_list"),
        ]
        return context


# ===================== Especialidade =====================

class EspecialidadeListView(ListView):
    model = Especialidade
    template_name = "especialidade_list.html"
    context_object_name = "especialidades"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q", "")
        if q:
            queryset = queryset.filter(nome__icontains=q)
        return queryset


class EspecialidadeDetailView(DetailView):
    model = Especialidade
    template_name = "especialidade_detail.html"
    context_object_name = "especialidade"


class EspecialidadeCreateView(CreateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "especialidade_form.html"
    success_url = reverse_lazy("especialidade_list")


class EspecialidadeUpdateView(UpdateView):
    model = Especialidade
    form_class = EspecialidadeForm
    template_name = "especialidade_form.html"
    success_url = reverse_lazy("especialidade_list")


class EspecialidadeDeleteView(ProtegidoDeleteView):
    model = Especialidade
    success_url = reverse_lazy("especialidade_list")


# ===================== Médico =====================

class MedicoListView(ListView):
    model = Medico
    template_name = "medico_list.html"
    context_object_name = "medicos"

    def get_queryset(self):
        queryset = Medico.objects.select_related("especialidade")
        q = self.request.GET.get("q", "")
        especialidade = self.request.GET.get("especialidade", "")
        if q:
            queryset = queryset.filter(Q(nome__icontains=q) | Q(num_cedula__icontains=q))
        if especialidade:
            queryset = queryset.filter(especialidade_id=especialidade)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["especialidades"] = Especialidade.objects.all()
        return context


class MedicoDetailView(DetailView):
    model = Medico
    template_name = "medico_detail.html"
    context_object_name = "medico"


class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico_list")


class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico_list")


class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("medico_list")


# ===================== Paciente =====================

class PacienteListView(ListView):
    model = Paciente
    template_name = "paciente_list.html"
    context_object_name = "pacientes"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q", "")
        sexo = self.request.GET.get("sexo", "")
        if q:
            queryset = queryset.filter(Q(nome__icontains=q) | Q(num_utente__icontains=q))
        if sexo:
            queryset = queryset.filter(sexo=sexo)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sexos"] = Paciente.SEXO_CHOICES
        return context


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = "paciente_detail.html"
    context_object_name = "paciente"


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente_list")


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente_list")


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("paciente_list")


# ===================== Relatório =====================

class RelatorioListView(ListView):
    model = Relatorio
    template_name = "relatorio_list.html"
    context_object_name = "relatorios"

    def get_queryset(self):
        queryset = Relatorio.objects.select_related(
            "medico", "exame__paciente", "exame__tipo_exame")
        q = self.request.GET.get("q", "")
        medico = self.request.GET.get("medico", "")
        if q:
            queryset = queryset.filter(
                Q(exame__paciente__nome__icontains=q) | Q(conclusao__icontains=q))
        if medico:
            queryset = queryset.filter(medico_id=medico)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medicos"] = Medico.objects.all()
        return context


class RelatorioDetailView(DetailView):
    model = Relatorio
    template_name = "relatorio_detail.html"
    context_object_name = "relatorio"


class RelatorioCreateView(CreateView):
    model = Relatorio
    form_class = RelatorioForm
    template_name = "relatorio_form.html"
    success_url = reverse_lazy("relatorio_list")

    def get_initial(self):
        # permite abrir /relatorios/add/?exame=5 com o exame já escolhido
        initial = super().get_initial()
        exame = self.request.GET.get("exame")
        if exame:
            initial["exame"] = exame
        return initial


class RelatorioUpdateView(UpdateView):
    model = Relatorio
    form_class = RelatorioForm
    template_name = "relatorio_form.html"
    success_url = reverse_lazy("relatorio_list")


class RelatorioDeleteView(DeleteView):
    model = Relatorio
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("relatorio_list")


# ===================== Tipo de exame =====================

class TipoExameListView(ListView):
    model = TipoExame
    template_name = "tipoexame_list.html"
    context_object_name = "tipos"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q", "")
        if q:
            queryset = queryset.filter(Q(nome__icontains=q) | Q(descricao__icontains=q))
        return queryset


class TipoExameDetailView(DetailView):
    model = TipoExame
    template_name = "tipoexame_detail.html"
    context_object_name = "tipo"


class TipoExameCreateView(CreateView):
    model = TipoExame
    form_class = TipoExameForm
    template_name = "tipoexame_form.html"
    success_url = reverse_lazy("tipoexame_list")


class TipoExameUpdateView(UpdateView):
    model = TipoExame
    form_class = TipoExameForm
    template_name = "tipoexame_form.html"
    success_url = reverse_lazy("tipoexame_list")


class TipoExameDeleteView(DeleteView):
    model = TipoExame
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("tipoexame_list")


# ===================== Equipamento =====================

class EquipamentoListView(ListView):
    model = Equipamento
    template_name = "equipamento_list.html"
    context_object_name = "equipamentos"

    def get_queryset(self):
        queryset = Equipamento.objects.prefetch_related("tipos_exame")
        q = self.request.GET.get("q", "")
        tipo = self.request.GET.get("tipo", "")
        if q:
            queryset = queryset.filter(
                Q(nome__icontains=q) | Q(fabricante__icontains=q) |
                Q(modelo__icontains=q) | Q(num_serie__icontains=q))
        if tipo:
            # filtrar pela relação N:N: equipamentos que fazem este tipo de exame
            queryset = queryset.filter(tipos_exame=tipo)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos"] = TipoExame.objects.all()
        return context


class EquipamentoDetailView(DetailView):
    model = Equipamento
    template_name = "equipamento_detail.html"
    context_object_name = "equipamento"


class EquipamentoCreateView(CreateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "equipamento_form.html"
    success_url = reverse_lazy("equipamento_list")


class EquipamentoUpdateView(UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "equipamento_form.html"
    success_url = reverse_lazy("equipamento_list")


class EquipamentoDeleteView(DeleteView):
    model = Equipamento
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("equipamento_list")


# ===================== Exame =====================

class ExameListView(ListView):
    model = Exame
    template_name = "exame_list.html"
    context_object_name = "exames"

    def get_queryset(self):
        queryset = Exame.objects.select_related(
            "paciente", "tipo_exame", "equipamento", "relatorio")
        q = self.request.GET.get("q", "")
        estado = self.request.GET.get("estado", "")
        tipo = self.request.GET.get("tipo", "")
        if q:
            queryset = queryset.filter(
                Q(paciente__nome__icontains=q) | Q(paciente__num_utente__icontains=q))
        if estado:
            queryset = queryset.filter(estado=estado)
        if tipo:
            queryset = queryset.filter(tipo_exame_id=tipo)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estados"] = Exame.ESTADO_CHOICES
        context["tipos"] = TipoExame.objects.all()
        return context


class ExameDetailView(DetailView):
    model = Exame
    template_name = "exame_detail.html"
    context_object_name = "exame"


class ExameCreateView(CreateView):
    model = Exame
    form_class = ExameForm
    template_name = "exame_form.html"
    success_url = reverse_lazy("exame_list")

    def get_initial(self):
        # permite abrir /exames/add/?paciente=3 com o paciente já escolhido
        initial = super().get_initial()
        paciente = self.request.GET.get("paciente")
        if paciente:
            initial["paciente"] = paciente
        return initial


class ExameUpdateView(UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = "exame_form.html"
    success_url = reverse_lazy("exame_list")


class ExameDeleteView(DeleteView):
    model = Exame
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("exame_list")

    # ===================== Apagar com proteção =====================

class ProtegidoDeleteView(DeleteView):
    template_name = "confirm_delete.html"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError as e:
            # pares (tipo de registo, registo), ex.: ("médico", "Ana Carvalho")
            relacionados = [(obj._meta.verbose_name, obj) for obj in e.protected_objects]
            context = self.get_context_data(
                erro=True, relacionados=relacionados[:10], total=len(relacionados))
            return self.render_to_response(context)