from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Главная страница</h1>')


def group_posts(request, name):
    return HttpResponse(f'Посты {name}')
