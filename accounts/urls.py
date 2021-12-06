from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "login.html", authentication_form = UserLoginForm), name='login'),
]