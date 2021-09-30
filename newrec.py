import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

dirname = os.path.dirname(__file__)
movies_p= os.path.join(dirname, 'Movielens','ml-latest-small','movies.csv')
ratings_p = os.path.join(dirname, 'Movielens', 'ml-latest-small','ratings.csv')
tags_p = os.path.join(dirname, 'Movielens', 'ml-latest-small','tags.csv')

movies = pd.read_csv(movies_p)
ratings = pd.read_csv(ratings_p)
tags = pd.read_csv(tags_p)

data = movies
# data = data.set_index('movieId')

print(data.head(35))

data = data.drop(['title'], axis=1)
for i in range(1,len(data.genres)):
    data.genres[i] = list(data.genres[i].split('|'))
    # print(data.genres[i])


x = pd.DataFrame(ratings.groupby('movieId')['rating'].mean())
tagsByMovie = pd.DataFrame(tags.groupby('movieId')['tag'].apply(list))

data = data.merge(x, on='movieId') 
# data = data.merge()


data = data.combine_first(tagsByMovie)



print(data.head(10))