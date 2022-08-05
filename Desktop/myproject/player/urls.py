from django.urls import path
from . import views

app_name = 'player'
urlpatterns = [
    path('', views.welcome),
    path('<int:player_id>/', views.movie),
    path('<int:player_id>/song/', views.song),
]

