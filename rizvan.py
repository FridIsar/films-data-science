import csv
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == '__main__':

    data = pd.read_csv(os.getcwd()+os.sep+"datasets"+os.sep+"films-imdb"+os.sep+"IMDb movies.csv", low_memory=False)


#j1 = sns.jointplot(data=data, x='reviews_from_critics', y='reviews_from_users')
    #plt.show()

    #Représentation graphique du nombre d'avis des critiques en fonction du nombre d'avis des utilisateurs

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Représentation graphique du nombre d'avis des critiques en fonction du nombre d'avis des utilisateurs")
    ax1.set_xlabel('reviews_from_critics')
    ax1.set_ylabel('reviews_from_users')
    ax1.scatter(data['reviews_from_critics'], data['reviews_from_users'])

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.set_title("Représentation graphique du nombre d'avis des utilisateurs en fonction de la durée du film")
    ax2.set_xlabel('reviews_from_users')
    ax2.set_ylabel('duration')
    ax2.scatter(data['reviews_from_users'], data['duration'])
    plt.show()