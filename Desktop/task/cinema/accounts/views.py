from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from werkzeug.utils import redirect
from .models import AcUser
from django.http import HttpResponse


def home(request):

    return render(request, 'registration/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            member = AcUser(user=user, is_admin=False)
            member.save()
            return redirect('welcome')

    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})


def user_login(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            member = AcUser(user=user)
            member.save()
            return redirect('welcome')

    else:
        form = UserCreationForm()
    return render(request, 'registration/login.html', {'form':form})