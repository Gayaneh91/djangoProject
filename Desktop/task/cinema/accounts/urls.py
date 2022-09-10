from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('home/', views.home, name='home'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('home/register/', views.register, name='register'),
    path('home/login/', views.user_login, name='login'),
]