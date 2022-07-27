import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from .models import Kino


def top_list(request):
    return render(request, 'top_list.html')
# Create your views here.

def scrapping(request):
    URL = 'https://www.kinopoisk.ru/lists/movies/top250/'

    r = requests.get(URL)
    # print(r.text)
    soup = BeautifulSoup(r.content, "html.parser")
    # print(soup)

    results = soup.find('div', class_='styles_root__ti07r')
    films_list = 'https://www.kinopoisk.ru/lists/movies/top250' + results.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
    # print(films_list)

    for fl in films_list[1:26]:

        divs = fl.find_all('div')
        for i in range(len(divs)):
            try:
                k = k.original_name=divs[2].text
            except:
                k = '-'

        return HttpResponse()





