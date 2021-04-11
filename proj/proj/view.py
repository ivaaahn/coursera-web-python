from functools import wraps
from django.http import HttpResponse, HttpResponseNotAllowed
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponseNotFound
# from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_http_methods


def simple_route(request: HttpRequest):
    print('METDOD = ', request.method)
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    return HttpResponse(status=200)

def slug_route(request: HttpRequest, data: str):
    print('REQUEST = ', request)
    return HttpResponse(f'Hello, slug_route. {data}')
    
def sum_route(request: HttpRequest, a: int, b: int):
    return HttpResponse(f'{int(a)} + {int(b)} = {int(a)+int(b)}')

@require_http_methods(["GET"])
def sum_get_method(request: HttpRequest):
    if not request.GET:
        ans = 'I got no parameters'
    else:   
        try:
            a = int(request.GET['a'])
            b = int(request.GET['b'])
        except ValueError:
            raise Http404('PABAMS')
        else:
            ans = a+b
    
    return HttpResponse(ans)

@require_http_methods(["POST"])
def sum_post_method(request: HttpRequest):
    print(request.POST)
    if not request.POST:
        ans = 'I got no parameters'
    else:
        try:
            a = int(request.POST['a'])
            b = int(request.POST['b'])
        except ValueError:
            raise Http404('PABAMS')
        else:
            ans = a+b
    
    return HttpResponse(ans)

def index(request):
    return HttpResponse('Hello')