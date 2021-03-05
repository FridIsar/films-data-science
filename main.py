import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':

    data = pd.read_csv(os.getcwd()+os.sep+"datasets"+os.sep+"films-imdb"+os.sep+"IMDb movies.csv", low_memory=False)

    best_movies = []

    score_100 = data[(data['metascore'] > 97)]

    score_100.groupby("director").size().plot.barh()

    plt.show()



    # Snippets utiles

    # plot = score_100.plot.pie(y='metascore', labels=score_100.director, figsize=(5, 5))
    # data_head = data.head(1000)
    #
    # data_head.plot(kind="scatter", x="reviews_from_users", y="reviews_from_critics")
    # plt.show()

    # for row in data.itertuples():
    #     if row.metascore > 99:
    #         best_movies.append(row)