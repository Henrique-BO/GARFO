from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name = "login.html", authentication_form = TeamUserLoginForm), name='login'),
    path('client/signup/1', views.client_signup_user, name='client_signup_user'),
    path('client/signup/2', views.client_signup, name='client_signup'),
    path('client/login/1', views.client_login, name='client_login'),
    path('client/login/2', views.client_login_mesa, name='client_login_mesa'),
]