from django.urls import path

from . import views

app_name = 'films'
urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('scrap/', views.scrap, name='scrap'),
    path('graphic/', views.graphic, name='graphic'),
    # path('scrap/film_list', views.film_list, name='film_list')
    ]