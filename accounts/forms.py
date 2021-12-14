from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields
from cpf_field.models import MyModel
from cpf_field.validators import validate_cpf

from accounts.models import Cliente, Gerente, Garcom, ChefCozinha
from pedidos.models import Mesa


class ClientLoginForm(AuthenticationForm):
   def __init__(self, * args, ** kwargs): super(ClientLoginForm, self).__init__( * args, ** kwargs)

   username = forms.CharField(widget=forms.TextInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Nome',
      }))
   password = forms.CharField(widget=forms.PasswordInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Senha',
      }))
   mesa = forms.ModelChoiceField(queryset=Mesa.objects.filter(disponivel=True), empty_label="Escolha uma mesa")

class ClienteCreationForm(UserCreationForm):
   def __init__(self, * args, ** kwargs): super(UserCreationForm, self).__init__( * args, ** kwargs)

   username = forms.CharField(widget=forms.TextInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Nome',
      }))
   cpf = MyModel._meta.get_field('cpf').formfield(
      widget=forms.NumberInput(
         attrs = {
            'class': 'form-control',
            'placeholder': 'CPF',
         }
      ),
      validators=[validate_cpf]
   )
   password1 = forms.CharField(widget=forms.PasswordInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Senha',
      }))
   password2 = forms.CharField(widget=forms.PasswordInput(
      attrs = {
         'class': 'form-control',
         'placeholder': 'Repita a senha',
      }))
   mesa = forms.ModelChoiceField(queryset=Mesa.objects.filter(disponivel=True), empty_label="Escolha uma mesa")

   field_order = ['username', 'cpf', 'password1', 'password2', 'mesa']