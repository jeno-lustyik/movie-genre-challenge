from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

title_links = []
movie_names = []
directors = []
stars = []

# get frontpage
pages = np.arange(1, 101, 50)

for page in pages:
    url = f'https://www.imdb.com/search/title/?genres=adventure&start={page}&explore=title_type,genres&ref_=adv_nxt'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find the headers that contain the titles
    temp = soup.find('div', class_='lister-list')
    headers = soup.find_all('h3', class_='lister-item-header')
    # Scrape the links

    for title in headers:
        links = title.find('a')
        title_links.append('https://www.imdb.com' + links['href'])
        movie_names.append(links.text)

    # Find the p-s that contain directors or directors

    d = temp.find_all('p', class_='')
    for i in d:
        director = ''
        if 'Director' in i.text:
            for k in i.text[15:]:
                if k == '|':
                    break
                else:
                    director += k
        directors.append(director)

    # s = temp.find_all('p', class_='')
    # for i in s:
    #     star = ''
    #     if 'Star' in i.text:
    #         for k in i.text:
    #             star += k
    #     stars.append(star)

for i in directors:
    directors[directors.index(i)] = ''.join(i.strip().split('\n'))
# for i in stars:
#     stars[stars.index(i)] = ''.join(i.strip().split('\n'))
# for i in stars:
#     if '|' in i:
#         stars[i] = stars[i[i.index('|'):]]
#         stars[stars.index(i)] = stars[index.(i)].replace('Stars:', '')
#     else:
#         stars[index.(i)] = stars[index.(i)].replace('Stars:', '')

print(stars)
print(len(stars))

# filming_date = []
# for i in title_links:
#     movie_page = requests.get(i)
#     movie_soup = BeautifulSoup(movie_page.content, 'html.parser')
#     movie_temp = movie_soup.find_all('a', class_='ipc-metadata-list-item__label ipc-metadata-list-item__label--link')
#     date_text = '-'
#     for k in movie_temp:
#         if 'tt_dt_loc' in k['href']:
#             date_page = requests.get('https://www.imdb.com' + k['href'])
#             date_soup = BeautifulSoup(date_page.content, 'html.parser')
#             # section = date_soup.find('section', id_='filming_dates')
#             date = date_soup.find('li', class_='ipl-zebra-list__item')
#             if date is not None:
#                 date_text = date.text
#         else:
#             continue
#     date_text = date_text.strip()
#     filming_date.append(date_text)
#
# print(filming_date)
