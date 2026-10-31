from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.db.models import Q
from .models import (Especialidade, Medico, Paciente, Relatorio,
                     TipoExame, Equipamento, Exame)
from .forms import EspecialidadeForm, MedicoForm, PacienteForm, RelatorioForm


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
            ("Tipos de exame", TipoExame.objects.count(), None),
            ("Equipamentos", Equipamento.objects.count(), None),
            ("Exames", Exame.objects.count(), None),
        ]
        return context


# ===================== Pessoa A: Especialidade =====================

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


class EspecialidadeDeleteView(DeleteView):
    model = Especialidade
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("especialidade_list")


# ===================== Pessoa A: Médico =====================

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


# ===================== Pessoa A: Paciente =====================

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


# ===================== Pessoa A: Relatório =====================

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


# ===================== Pessoa B =====================