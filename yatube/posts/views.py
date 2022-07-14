from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    template_main = 'posts/index.html'
    text = "Это главная страница проекта Yatube"
    context = {
        'text': text,
    }
    return render(request, template_main, context)


def group_posts(request):
    template_group = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text,
    }
    return render(request, template_group, context)
