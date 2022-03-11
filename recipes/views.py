from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Luiz Fernando'
    })


def contato(request):
    return render(request, 'me_apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
