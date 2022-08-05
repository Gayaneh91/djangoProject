import requests
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bs4 import BeautifulSoup
from .models import Movies, Songs


def welcome(request):
    return render(request, 'welcome.html')


def movie(request):
    movies_list = get_object_or_404(Movies, id=player_id)
    return render(request, 'player/movie.html', {'movies_list': movies_list})


def song(request):
    songs_list = get_object_or_404(Songs, id=player_id)
    return render(request, 'player/song.html', {'songs_list': songs_list})
