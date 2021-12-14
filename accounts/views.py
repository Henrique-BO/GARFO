from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from accounts.forms import ClienteCreationForm, ClientLoginForm
from accounts.models import Cliente

def cliente_signup(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            cpf = form.cleaned_data['cpf']
            mesa = form.cleaned_data['mesa']
            cliente = Cliente(user=user, cpf=cpf, mesa=mesa)
            cliente.save()
            login(request, user)
            return HttpResponseRedirect(reverse('pedidos:index'))
    else:
        form = ClienteCreationForm()

    context = {'form': form}
    return render(request, 'accounts/cliente_signup.html', context)

def cliente_login(request):
    if request.method == 'POST':
        form = ClientLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                cliente = user.cliente
                cliente.mesa = form.cleaned_data['mesa']
                cliente.save()
                login(request, form.get_user())
                return HttpResponseRedirect(reverse('pedidos:index'))
            except:
                form.add_error("username", "Usuário não é um Cliente. Favor entrar pelo login da Equipe.")
    else:
        form = ClientLoginForm()

    context = {'form': form}
    return render(request, 'accounts/cliente_login.html', context)

def equipe_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                user.cliente
                form.add_error("username", "Usuário não faz parte da Equipe. Favor entrar pelo login de Cliente.")
            except:
                login(request, form.get_user()) 
                if request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                return HttpResponseRedirect(reverse('pedidos:index'))
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/equipe_login.html', context)