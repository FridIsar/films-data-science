import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns
import os

def distribution(dataset_name, field):
    dataset = pd.read_csv(os.getcwd()+os.sep+os.pardir+os.sep+"datasets"+os.sep+"films-imdb"+os.sep+dataset_name, low_memory=False)
    sns.set(style="white", palette="deep")
    f1, ax1 = plt.subplots(figsize=(40,9))
    f1.suptitle('Distribution of '+field,
               fontsize=13)
    f1.subplots_adjust(top=0.85)
    sns.countplot(dataset[field])
    ax1.set_xlabel(field)
    ax1.set_ylabel("number")
    sns.despine(top=True, right=True, left=False, bottom=False)
    f1.savefig(os.pardir+os.sep+'graphiques'+os.sep+'distrib_'+field+'.png', bbox_inches='tight', dpi=200)