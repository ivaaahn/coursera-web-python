"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls.conf import include

from .view import simple_route, index, slug_route, sum_route, sum_get_method, sum_post_method

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('routing/', include([
        path('simple_route/', simple_route),
        re_path(r'^slug_route/(?P<data>[\w-]{1,16})/$', slug_route),
        re_path(r'^sum_route/(?P<a>-?\d)/(?P<b>-?\d)/$', sum_route),
        path('sum_get_method/', sum_get_method),
        path('sum_post_method/', sum_post_method)
    ]))
]
