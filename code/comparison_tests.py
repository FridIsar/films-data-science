from modules import visumodule as vm

vm.comparison("films-imdb/IMDb movies.csv", "reviews_from_critics", "reviews_from_users", 2000)

vm.comparison("films-imdb/IMDb movies.csv", "usa_gross_income", "worlwide_gross_income", 100000000)

vm.comparison("films-imdb/IMDb movies.csv", "budget", "worlwide_gross_income", 100000000)