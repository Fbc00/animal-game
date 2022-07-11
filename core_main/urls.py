from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('detalhes/', views.detalhes, name='detalhes'),
    path('registrar/', views.registrar, name='registrar'),
]
