import pandas as pd

df = pd.read_csv('IMDb_movies.csv', low_memory=False)

indexNames1 = df[(df['year'] == "TV Movie 2019")].index
df.drop(indexNames1, inplace=True)

indexNames2 = df[(df['duration'] >= 250)].index
df.drop(indexNames2, inplace=True)

indexNames3 = df[(df['metascore'] <= 7)].index
df.drop(indexNames3, inplace=True)

indexNames4 = df[(df['genre'].map(len) >= 8)].index
df.drop(indexNames4, inplace=True)

df.dropna()

df.to_csv("cleanData.csv")
