from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import ClientLoginForm
from . import views

app_name = 'accounts'
urlpatterns = [
    path('cliente/signup/', views.cliente_signup, name='cliente_signup'),
    path('cliente/login/', views.cliente_login, name='cliente_login'),
    # path('client/signup/1', views.client_signup_user, name='client_signup_user'),
    # path('client/signup/2', views.client_signup, name='client_signup'),
    # path('client/login/1', views.client_login, name='client_login'),
    # path('client/login/2', views.client_login_mesa, name='client_login_mesa'),
]