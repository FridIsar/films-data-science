import warnings
import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns
import os

warnings.simplefilter(action='ignore', category=FutureWarning)


class Visualiser:
    """Classe prenant un dataset/chemin qui permet d'afficher différents graphiques"""

    def __init__(self, dataset):
        if isinstance(dataset, str):
            self.dataset = pd.read_csv(dataset, low_memory=False)
        else:
            self.dataset = dataset

    def distribution(self, field):
        sns.set(style="white", palette="deep")
        f1, ax1 = plt.subplots(figsize=(40,9))
        f1.suptitle('Distribution of '+field,
                   fontsize=13)
        f1.subplots_adjust(top=0.85)
        sns.countplot(self.dataset[field])
        ax1.set_xlabel(field)
        ax1.set_ylabel("number")
        sns.despine(top=True, right=True, left=False, bottom=False)
        #f1.savefig('graphiques'+os.sep+'distrib_'+field+'.png', bbox_inches='tight', dpi=200)

    def comparison(self, field_one, field_two, range):
        # remove non numeric data if string:
        dataset = self.dataset
        print(dataset[field_one].dtype)
        if dataset[field_one].dtype != np.float64:
            dataset[field_one] = dataset[field_one].str.extract('(\d+)', expand=False).astype(float)
        if dataset[field_two].dtype != np.float64:
            dataset[field_two] = dataset[field_two].str.extract('(\d+)', expand=False).astype(float)

        sns.set(style="white", palette="deep")

        f, ax = plt.subplots(figsize=(15, 6))

        sns.despine(top=True, right=True, left=False, bottom=False)  # retire lignes

        ax.hist(dataset[field_one], bins=10, range=(0, range), histtype='step',
                lw=1.5, label=field_one, color='C0')
        ax.hist(dataset[field_two], bins=10, range=(0, range), histtype='step',
                lw=1.5, label=field_two, color='C1')
        ax.legend(loc='upper left')
        ax.set_title('Comparison between '+field_one+' and '+field_two)
        #ax.set_xlabel('Ratings')

        #f.savefig('graphiques/' + field_one + '_' + field_two + '_comparison.png', bbox_inches='tight', dpi=200)
