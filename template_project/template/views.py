from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.

def echo(request: HttpRequest):
    data = dict(request.GET.items())
    x = request.headers.get('X-Print-Statement')
    for k, v in request.headers.items():
        print(f'{k} : {v}')

    x = x if x else 'Empty'
    
    return render(request, 'template/echo.html', context={'data': data, 'x': x})


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })

    