from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(req: HttpRequest):
    data=req.GET.get('x')
    data = data if data else 10
    
    return render(req, 'templatetags/index.html', context={'data': data})