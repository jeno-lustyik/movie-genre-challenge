import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv (r'C:\Users\omolara\Documents\strive school\strive-exercise\10. Movie Challenge\sample_dataset.csv')
#print (df.describe())
#Rating_duration = df['rating']/df['duration']
df2 = df.assign(Rating_duration= df['rating']/df['duration'])
df3 = df2.assign(Rating_movtime= df2['rating']/df2['release'])
print (df3.describe())

def norm_max_min():
    Rating_max_min = df3.copy()
    column= 'Rating_duration'
    #for cols in Rating_max_min.columns:
    Rating_max_min[column] = (Rating_max_min[column] -  Rating_max_min[column].min())/ (Rating_max_min[column].max() - Rating_max_min[column].min())
    a = df3.assign(Rating_max_min = Rating_max_min[column])
    return a
df4 = print(norm_max_min())


#Rating_max_min = df.copy()
# def norm_max_min():
#     Rating_max_min = df.copy()
#     column= 'budget ($ Mil)'
#     #for cols in Rating_max_min.columns:
#     Rating_max_min[column] = (Rating_max_min[column] -  Rating_max_min[column].min())/ (Rating_max_min[column].max() - Rating_max_min[column].min())
#     return Rating_max_min[column]
# print(norm_max_min())


# plt.bar(df4['rating'],df4['release'],width = 0.4, label = 'ratings per year')
# plt.grid(True,linestyle = '--', color = 'dimgrey')
# plt.ylabel('release year')
# plt.xlabel('ratings')
# plt.legend()
# plt.show()

df4.plot.scatter(x = 'release', y = 'rating', color = 'darkred', s = 25, figsize = (12,2))