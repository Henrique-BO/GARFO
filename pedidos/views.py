from django.shortcuts import render


def index(request):
    context = {}
    return render(request,'pedidos/index.html', context)