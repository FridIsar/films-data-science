from modules import visumodule

vm = visumodule.Visualiser("/Users/isar/PycharmProjects/films-data-science/datasets/films-imdb/IMDb movies.csv")

vm.distribution("metascore")

vm.distribution("year")