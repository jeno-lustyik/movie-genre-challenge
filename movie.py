from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


ratings = []
duration = []
genre = []
desc = []


pages = np.arange(1, 101, 50)

for page in pages:

    url1 = f"https://www.imdb.com/search/title/?genres=adventure&start={page}&explore=title_type,genres&ref_=adv_nxt"
#url2 = 'https://www.imdb.com/search/title/?genres=adventure&start=51&explore=title_type,genres&ref_=adv_nxt'
    pg = requests.get(url1)
    
    soup = BeautifulSoup(pg.content, 'html.parser')

    div_movies = soup.find_all('div', class_ = 'lister-item mode-advanced')

    for i in div_movies:
        if i.find('strong') is not None:
            ratings.append(i.find('strong').text)
        else:
            ratings.append('_')


        if (i.find('span', class_ = 'runtime')) is not None:
            duration.append(i.find('span', class_ = 'runtime').text.replace(' min',''))

        else:
            duration.append('_')


        if (i.find('span', class_ = 'genre')) is not None:
            genre.append(i.find('span', class_ = 'genre').text.replace('\n', ''))

        else:
            genre.append('_')


        if (i.find('p', class_='text-muted')) is not None:
            desc.append(i.find('p', class_='text-muted').text.replace('\n', ''))

        else:
            desc.append('_')


        


#print(len(ratings))
#print(len(duration))
#print(len(genre))
print(desc)



