from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # ===================== Pessoa A =====================

    # Especialidades
    path('especialidades/', views.EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidades/add/', views.EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidades/<int:pk>/', views.EspecialidadeDetailView.as_view(), name='especialidade_detail'),
    path('especialidades/<int:pk>/edit/', views.EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('especialidades/<int:pk>/delete/', views.EspecialidadeDeleteView.as_view(), name='especialidade_delete'),

    # Médicos
    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/add/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/', views.MedicoDetailView.as_view(), name='medico_detail'),
    path('medicos/<int:pk>/edit/', views.MedicoUpdateView.as_view(), name='medico_edit'),
    path('medicos/<int:pk>/delete/', views.MedicoDeleteView.as_view(), name='medico_delete'),

    # Pacientes
    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/add/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/<int:pk>/', views.PacienteDetailView.as_view(), name='paciente_detail'),
    path('pacientes/<int:pk>/edit/', views.PacienteUpdateView.as_view(), name='paciente_edit'),
    path('pacientes/<int:pk>/delete/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # Relatórios
    path('relatorios/', views.RelatorioListView.as_view(), name='relatorio_list'),
    path('relatorios/add/', views.RelatorioCreateView.as_view(), name='relatorio_create'),
    path('relatorios/<int:pk>/', views.RelatorioDetailView.as_view(), name='relatorio_detail'),
    path('relatorios/<int:pk>/edit/', views.RelatorioUpdateView.as_view(), name='relatorio_edit'),
    path('relatorios/<int:pk>/delete/', views.RelatorioDeleteView.as_view(), name='relatorio_delete'),

    # ===================== Pessoa B =====================
]