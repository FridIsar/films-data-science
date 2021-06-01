import pandas as pd
from selenium import webdriver



df = pd.read_csv('IMDb_movies.csv')

def RUN(text1, text2, text3, text4, text5):
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn import tree
    import pydot

    df = pd.read_csv('IMDb_movies.csv', low_memory=False)

    indexNames = df[(df['country'] != text5 + "")].index
    df.drop(indexNames, inplace=True)

    indexNames3 = df[(df['genre'] != text4 + "")].index
    df.drop(indexNames3, inplace=True)

    indexNames2 = df[(df['avg_vote'] != 'NaN')].index
    df.drop(indexNames2)

    del df["imdb_title_id"]
    # del df["title"]
    del df["original_title"]
    del df["date_published"]
    del df["country"]
    del df["language"]
    # del df["year"]
    del df["writer"]
    del df["director"]
    del df["actors"]
    del df["description"]
    # del df["avg_vote"]
    del df["votes"]
    del df["budget"]
    del df["usa_gross_income"]
    del df["worlwide_gross_income"]
    del df["reviews_from_users"]
    del df["reviews_from_critics"]
    del df["production_company"]
    # del df["duration"]
    del df["metascore"]
    del df["genre"]

    df.dropna()
    lenr = len(df.index)
    print(lenr)
    df1 = df.sample(n=(lenr - 1))

    X = df1.drop(columns=['title'])
    y = df1['title']
    df1

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier(max_depth=3)

    model.fit(X_train, y_train)
    model.score(X_train, y_train)

    model.fit(X, y)

    pred = model.predict([[text1, text2, text3]])
    print(pred)
    text = "%s" % (pred[0])

    dot_data = "result.dot"
    tree.export_graphviz(model, out_file=dot_data,
                         feature_names=['year', 'avg_vote', 'duration'],
                         class_names=sorted(y.unique()),
                         label='all',
                         rounded=True,
                         filled=True)

    (graph,) = pydot.graph_from_dot_file(dot_data)
    graph.write_png("result.png")

    return text

def selenium(text):
    driver = webdriver.Chrome(r"C:\Users\PC\Downloads\chromedriver_win32\chromedriver.exe")
    driver.set_window_size(1900, 1020)
    url = "https://www.google.com/search?q=" + text +"+film"

    driver.get(url)
