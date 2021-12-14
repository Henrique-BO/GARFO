from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import ClientLoginForm
from . import views

app_name = 'accounts'
urlpatterns = [
    path('cliente/signup/', views.cliente_signup, name='cliente_signup'),
    path('cliente/login/', views.cliente_login, name='cliente_login'),
    path('equipe/login/', views.equipe_login, name='equipe_login'),
]