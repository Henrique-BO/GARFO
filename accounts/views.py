from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from cpf_field.forms import CPFFieldForm

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
                print(cliente.mesa)
                cliente.save()
                login(request, form.get_user())
                return HttpResponseRedirect(reverse('pedidos:index'))
            except:
                pass
    else:
        form = ClientLoginForm()

    context = {'form': form}
    return render(request, 'accounts/cliente_login.html', context)