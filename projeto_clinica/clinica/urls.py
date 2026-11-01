from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

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

    # Tipos de exame
    path('tipos-exame/', views.TipoExameListView.as_view(), name='tipoexame_list'),
    path('tipos-exame/add/', views.TipoExameCreateView.as_view(), name='tipoexame_create'),
    path('tipos-exame/<int:pk>/', views.TipoExameDetailView.as_view(), name='tipoexame_detail'),
    path('tipos-exame/<int:pk>/edit/', views.TipoExameUpdateView.as_view(), name='tipoexame_edit'),
    path('tipos-exame/<int:pk>/delete/', views.TipoExameDeleteView.as_view(), name='tipoexame_delete'),

    # Equipamentos
    path('equipamentos/', views.EquipamentoListView.as_view(), name='equipamento_list'),
    path('equipamentos/add/', views.EquipamentoCreateView.as_view(), name='equipamento_create'),
    path('equipamentos/<int:pk>/', views.EquipamentoDetailView.as_view(), name='equipamento_detail'),
    path('equipamentos/<int:pk>/edit/', views.EquipamentoUpdateView.as_view(), name='equipamento_edit'),
    path('equipamentos/<int:pk>/delete/', views.EquipamentoDeleteView.as_view(), name='equipamento_delete'),

    # Exames
    path('exames/', views.ExameListView.as_view(), name='exame_list'),
    path('exames/add/', views.ExameCreateView.as_view(), name='exame_create'),
    path('exames/<int:pk>/', views.ExameDetailView.as_view(), name='exame_detail'),
    path('exames/<int:pk>/edit/', views.ExameUpdateView.as_view(), name='exame_edit'),
    path('exames/<int:pk>/delete/', views.ExameDeleteView.as_view(), name='exame_delete'),
]