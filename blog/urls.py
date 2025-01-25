from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts/', views.posts),
    path('posts/<int:number_post>/', views.int_post),
    path('posts/<str:name_post>/', views.posts_info),
]
