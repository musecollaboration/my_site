from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return HttpResponse('Все посты блога')


def posts_info(request, name_post: str):
    return HttpResponse(f'Информация о посте {name_post}')


def int_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
