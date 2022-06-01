import pandas
from matplotlib import pyplot

# a
cities = pandas.read_csv("miasta.csv")

# print(cities)

# print(cities.values)

# b
new_row = pandas.DataFrame.from_dict({
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]
})

cities_with_new_row = pandas.concat([cities, new_row], ignore_index=True, sort=False)
# print(cities_with_new_row)

#c
pyplot.plot(cities.Rok, cities.Gdansk, color='r', linestyle='solid',
            marker='o', label="Population of Gdańsk")
pyplot.xlabel('Year')
pyplot.ylabel('Number of residents')
pyplot.title("Population of Gdańsk", fontsize=20)
pyplot.grid()
pyplot.legend()
pyplot.show()

# d
pyplot.plot(cities.Rok, cities.Gdansk, color='g', linestyle='solid',
            marker='o', label="Population of Gdańsk")

pyplot.plot(cities.Rok, cities.Poznan, color='b', linestyle='solid',
            marker='o', label="Population of Poznań")

pyplot.plot(cities.Rok, cities.Szczecin, color='r', linestyle='solid',
            marker='o', label="Population of Szczecin")
pyplot.xlabel('Year')
pyplot.ylabel('Number of residents')
pyplot.title("Population of Polish cities", fontsize=20)
pyplot.grid()
pyplot.legend(["Population of Gdańsk", "Population of Poznań", "Population of Szczecin"])
pyplot.show()