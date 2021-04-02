import csv
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

if __name__ == '__main__':

    data = pd.read_csv(os.getcwd()+os.sep+os.pardir+os.sep+"datasets"+os.sep+"films-imdb"+os.sep+"IMDb movies.csv", low_memory=False)


#j1 = sns.jointplot(data=data, x='reviews_from_critics', y='reviews_from_users')
    #plt.show()

#Représentation graphique du nombre d'avis des critiques en fonction du nombre d'avis des utilisateurs

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("Représentation graphique du nombre d'avis des critiques en fonction du nombre d'avis des utilisateurs")
    ax1.set_xlabel('reviews_from_critics')
    ax1.set_ylabel('reviews_from_users')
    ax1.scatter(data['reviews_from_critics'], data['reviews_from_users'])

#Représentation graphique du nombre d'avis des utilisateurs en fonction de la durée du film
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.set_title("Représentation graphique du nombre d'avis des utilisateurs en fonction de la durée du film")
    ax2.set_xlabel('reviews_from_users')
    ax2.set_ylabel('duration')
    ax2.scatter(data['reviews_from_users'], data['duration'])
    #montre qu'un film de durée inférieur à 200 min sont plus appréciés


# Représentation graphique du nombre d'avis des critiques en fonction de la durée du film
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(111)
    ax3.set_title("Représentation graphique du nombre d'avis des critiques en fonction de la durée du film")
    ax3.set_xlabel('reviews_from_critics')
    ax3.set_ylabel('duration')
    ax3.scatter(data['reviews_from_critics'], data['duration'])
    # montre qu'un film de durée inférieur à 200 min sont plus appréciés

#Représentation graphique de la recette des films en fonction du nombre d'avis du public
    #fig4 = plt.figure()
    #ax4 = fig4.add_subplot(111)
    #ax4.set_title("Représentation graphique de la recette des films en fonction du nombre d'avis du public")
    #ax4.set_xlabel('reviews_from_users')
    #ax4.set_ylabel('worlwide_gross_income')
    #ax4.scatter(data['reviews_from_users'], data['worlwide_gross_income'])
    # montre qu'un film qui a été bien noté par le public est un film qui a rapporté le plus de millions de dollars
    #il faut enlever le $ dans la colonne worlwide_gross_income

# Représentation graphique du nombre de votes en fonction du nombre d'avis du public
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111)
    ax5.set_title("Représentation graphique du nombre de votes en fonction du nombre d'avis du public")
    ax5.set_xlabel('reviews_from_users')
    ax5.set_ylabel('votes')
    ax5.scatter(data['reviews_from_users'], data['votes'])

    plt.show()