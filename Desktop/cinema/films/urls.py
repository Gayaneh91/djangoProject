from django.urls import path

from . import views

app_name = 'films'
urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('scrap/', views.scrap, name='scrap'),
    path('graphic/', views.graphic, name='graphic'),
    path('welcome/table/', views.table, name='table')
    ]