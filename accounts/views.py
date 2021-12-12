from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ClientCreationForm, ClientUserCreationForm, UserLoginForm, ClientMesaForm
from accounts.models import Cliente

def client_signup_user(request):
    if request.method == 'POST':
        form = ClientUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ClientUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/client_signup_user.html', context)

def client_signup(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            client_user = request.user
            client_cpf = form.cleaned_data['cpf']
            client_mesa = form.cleaned_data['mesa']
            client = Cliente(user=client_user,
                            cpf=client_cpf,
                            mesa=client_mesa)
            client.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ClientCreationForm()

    context = {'form': form}
    return render(request, 'accounts/client_signup.html', context)

def client_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:client_login_mesa'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'accounts/client_login.html', context)

def client_login_mesa(request):
    if request.method == 'POST':
        form = ClientMesaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pedidos:cardapio'))
    else:
        form = ClientMesaForm()

    context = {'form': form}
    return render(request, 'accounts/client_login.html', context)