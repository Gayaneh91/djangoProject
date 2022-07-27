import requests
from bs4 import BeautifulSoup

URL = 'https://www.kinopoisk.ru/lists/movies/top250/'

def show_movies(request):
    r = requests.get(URL)
    print(r.text)
    soup = BeautifulSoup(r.content, "html.parser")
#print(soup)
    results = soup.find('div', class_='styles_root__ti07r')
    films_list = 'https://www.kinopoisk.ru/lists/movies/top250' + results.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
    print(films_list)
