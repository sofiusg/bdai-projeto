from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('luthiersHTML/', views. luthiersHTMLFUNC, name='luthiersHTML'),
    path('luthiersTESTE/', views. luthiersTESTEFUNC, name='luthiersTESTE'),

    # Luthiers
    path('luthiers/', views.LuthierListView.as_view(), name='luthier_list'),
    path('luthiers/add/', views.LuthierCreateView.as_view(),
    name='luthier_create'),
    path('luthiers/<int:pk>/', views.LuthierDetailView.as_view(),
    name='luthier_detail'),
    path('luthiers/<int:pk>/edit/', views.LuthierUpdateView.as_view(),
    name='luthier_edit'),
    path('luthiers/<int:pk>/delete/', views.LuthierDeleteView.as_view(),
    name='luthier_delete'),
    
    # Guitarras
    path('guitarras/', views.GuitarListView.as_view(), name='guitar_list'),
    path('guitarras/add/', views.GuitarCreateView.as_view(),
    name='guitar_create'),
    path('guitarras/<int:pk>/', views.GuitarDetailView.as_view(),
    name='guitar_detail'),
    path('guitarras/<int:pk>/edit/', views.GuitarUpdateView.as_view(),
    name='guitar_edit'),
    path('guitarras/<int:pk>/delete/', views.GuitarDeleteView.as_view(),
    name='guitar_delete'),
]