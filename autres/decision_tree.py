import numpy as np
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function

col_names = ['imdb_title_id', 'title', 'original_title', 'year', 'date_published', 'genre', 'duration', 'country', 'language', 'director', 'writer', 'production_company', 'actors', 'description', 'avg_vote', 'votes', 'budget', 'usa_gross_income', 'worlwide_gross_income', 'metascore', 'reviews_from_users', 'reviews_from_critics']
# load dataset
data = pd.read_csv(os.getcwd() + os.sep + "datasets" + os.sep + "films-imdb" + os.sep + "IMDb movies.csv", low_memory=False, header=None, names=col_names)
#pima = pd.read_csv("diabetes.csv", header=None, names=col_names)
del data['imdb_title_id']
del data['title']
del data['original_title']
del data['date_published']
del data['genre']
del data['country']
del data['language']
del data['director']
del data['writer']
del data['production_company']
del data['actors']
del data['description']
del data['budget']
del data['usa_gross_income']
del data['worlwide_gross_income']
del data['metascore']
del data['reviews_from_users']
del data['reviews_from_critics']

print(data.head())

print(data.isnull().sum())

data.fillna(data.mean(), inplace=True)
data[:] = np.nan_to_num(data)

data['duration'] = data['duration'].str.extract('(\d+)', expand=False).astype(float)
data['avg_vote'] = data['avg_vote'].str.extract('(\d+)', expand=False).astype(float)
data['votes'] = data['votes'].str.extract('(\d+)', expand=False).astype(float)

data.fillna(0, inplace=True)

print(data.head())

print(data.isnull().sum())

#split dataset in features and target variable
feature_cols = ['duration', 'avg_vote', 'votes']
X = data[feature_cols] # Features
y = data.year # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test


# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)



from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('decision_tree.png')
Image(graph.create_png())

