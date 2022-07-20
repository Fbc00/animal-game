from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:id>/', views.detalhes, name='detalhes'),
    path('registrar/', views.registrar, name='registrar'),
    path('aposta/', views.aposta_feita, name='apostas')
]
