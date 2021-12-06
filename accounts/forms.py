from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
   def __init__(self, * args, ** kwargs): super(UserLoginForm, self).__init__( * args, ** kwargs)

username = forms.EmailField(widget = forms.TextInput(
   attrs = {
      'class': 'form-control',
      'placeholder': 'Nome',
   }))
password = forms.CharField(widget = forms.PasswordInput(
   attrs = {
      'class': 'form-control',
      'placeholder': 'Senha',
   }
))