import requests
from bs4 import BeautifulSoup




url = 'https://www.imdb.com/chart/top/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# number = soup.findAll('td', class_="titleColumn")[0][0].text
# n = number.split(-2)
# print(number)
# link = 'https://www.imdb.com/' + soup.find('td', class_="titleColumn").get('href')
# print(link)
# name = soup.find('td', class_="titleColumn").find('a', title='Frank Darabont (dir.), Tim Robbins, Morgan Freeman').text
# print(name)
# year = soup.find('td', class_="titleColumn").find('span', class_='secondaryInfo').text
# y = year.replace('(','').replace(')', '')
# print(y)
# rate = soup.find('td', class_="imdbRating").text
# print(rate)

# film_list = soup.findAll('td', class_="titleColumn")
#
# for film in film_list:
#     f = Film(name = soup.find('td', class_="titleColumn").find('a', title='Frank Darabont (dir.), Tim Robbins, Morgan Freeman').text,
#             year = soup.find('td', class_="titleColumn").find('span', class_='secondaryInfo').text.replace('(', '').replace(')',''),
#             rate = soup.find('td', class_="imdbRating").text.replace('\n', ''))
#     f.save()
#
#     print(f)

#2
# for film in film_list:
#     tds = film.find_all('tr')
#     f = Film(name=tds[1].text,
#              year=tds[1][2].text,
#              rate=tds[2].text,)
#
#     f.save()
res = soup.find(class_='chart full-width')
film_list = res.find_all('tr')
for film in film_list:
    tds = film.find_all('td')

    # name = film_list[1].find('td', class_='titleColumn').select('td title')[0].text.strip()
    # year = film_list[1].find('td', class_='titleColumn').select('td span')[0].text[1:-1]
    # rate = film_list[1].find('td', class_='imdbRating').find('strong').get('title')
    # f.save()


    name = film_list[1].find('td', class_='titleColumn').find('a').text
    year = film_list[1].find('td', class_='titleColumn').select('td span')[0].text[1:-1]
    rate = film_list[1].find('td', class_='imdbRating').text.strip()
    user = film_list[1].find('td', class_='imdbRating').find('strong').get('title').split(' ')[3].replace(',', '')


    print('name - ', name)
    print('rate - ', rate)
    print('users - ', user)
    print('year - ', year)