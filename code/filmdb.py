import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':

    data = pd.read_csv(os.getcwd()+os.sep+os.pardir+os.sep+
                       "datasets"+os.sep+"the-movies"+os.sep+"movies_metadata.csv", low_memory=False)

    best_movies = []
    for row in data.itertuples():
        print(row.video)

