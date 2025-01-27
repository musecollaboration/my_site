from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')


def posts_info(request, name_post: str):
    return HttpResponse(f'Информация о посте {name_post}')


def int_post(request, number_post: int):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
