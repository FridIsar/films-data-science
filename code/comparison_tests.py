from modules import visumodule

vm = visumodule.Visualiser("/Users/isar/PycharmProjects/films-data-science/datasets/films-imdb/IMDb movies.csv")

vm.comparison("reviews_from_critics", "reviews_from_users", 2000)

vm.comparison("usa_gross_income", "worlwide_gross_income", 100000000)

vm.comparison("budget", "worlwide_gross_income", 100000000)