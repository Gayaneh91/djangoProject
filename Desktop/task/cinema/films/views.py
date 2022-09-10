import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from .models import Film
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
# Create your views here.


def welcome(request):

    return render(request, 'Welcome.html')


def scrap(request):

    url = 'https://www.imdb.com/chart/top/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    res = soup.find(class_='titleColumn')
    film_list = res.find_all('tr')

    for film in film_list:

        tds = film.find_all('td')
        f = Film(name=film.find('a').text,
                 year=film.select('td span')[0].text[1:-1],
                 rate=soup.find('td', class_='imdbRating').text.strip(),
                 number_of_users=soup.find('td', class_='imdbRating').find('strong').get('title').split(' ')[3].replace(',', ''))
        f.save()
        # print(f)

    return render(request, 'scrap.html')


def table(request):
    allfilms = Film.objects.all()
    return render(request, 'scrap.html', {'allfilms':allfilms})


def graphic(request):

    films = Film.objects.filter(rate=9)

    x = []
    y = []
    for f in films:
        x.append(f.name)
        y.append(f.rate)


    plt.scatter(x, y)
    plt.savefig('static/film.svg')

    return render(request, 'graphic.html')


