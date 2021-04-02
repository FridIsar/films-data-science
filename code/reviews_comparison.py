# TODO moduliser
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns
import os

allocine = pd.read_csv(os.getcwd()+os.sep+os.pardir+os.sep+
                       "datasets"+os.sep+"films-imdb"+os.sep+"IMDb movies.csv", low_memory=False)
sns.set(style="white", palette="deep")

#ax1.set_xlim([0.5,100.5])


#ax1.hist(allocine["metascore"], bins = 10, range = (0,100), color='C0') # bin range = 1


best_movies = allocine#[allocine["metascore"] >= 98]

f, ax = plt.subplots(figsize=(15,6))

sns.despine(top=True, right=True, left=False, bottom=False) #retire lignes

ax.hist(allocine["reviews_from_critics"], bins = 10, range = (0,2000), histtype = 'step',
         lw=1.5, label='Press Ratings', color='C0')
ax.hist(allocine["reviews_from_users"], bins = 10, range = (0,2000), histtype = 'step',
         lw=1.5, label='Users Ratings', color='C1')
ax.legend(loc = 'upper left')
ax.set_title('Comparison of Distributions')
ax.set_xlabel('Ratings')

f.savefig('../graphiques/reviews_comparison.png', bbox_inches='tight', dpi=200)