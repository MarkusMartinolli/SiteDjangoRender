from django.contrib import admin
from django.urls import path, include
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Rotas de Cadastro
    path('cadastro/', views.signup_choice, name='signup_choice'),
    path('cadastro/cliente/', views.signup_cliente, name='signup_cliente'),
    path('cadastro/oficina/', views.signup_oficina, name='signup_oficina'),
    
    # Painéis
    path('painel/cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('painel/oficina/', views.dashboard_oficina, name='dashboard_oficina'),
    
    # Serviços
    path('servico/<int:pk>/pegar/', views.pegar_servico, name='pegar_servico'),
    path('servico/<int:pk>/concluir/', views.concluir_servico, name='concluir_servico'),
]