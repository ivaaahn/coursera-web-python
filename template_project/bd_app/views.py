from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.

from .models import Developers


def index(req: HttpRequest):
    name = req.GET.get('n')
    name = name if name else 'Дима'

    return render(req, 'bd_app/index.html', context={'title': 'index', 'name': name})


def developers(req: HttpRequest):
    developers = list(Developers.objects.all())

    return render(req, 'bd_app/developers.html', context={'title': 'developers', 'developers' : developers})
