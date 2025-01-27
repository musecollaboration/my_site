from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')


def posts_info(request, name_post: str):
    context = {'name_post': name_post}
    return render(request, 'blog/detail_by_name.html', context=context)


def int_post(request, number_post: int):
    context = {'number_post': number_post}
    return render(request, 'blog/detail_by_number.html', context=context)
