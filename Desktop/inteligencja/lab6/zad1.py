import pandas as pd

missing_values = ["-", "NA"]
df = pd.read_csv("iris_with_errors.csv", na_values=missing_values)


# a) Policz ile jest w bazie brakujących lub nieuzupełnionych danych. Wyświetl
# statystyki bazy danych z błędami.

print("Czy są jakieś brakujące wartości?")
print(df.isnull().values.any())

print("Ilość brakujących wartości:")
print(df.isnull().sum().sum())

print("Ilość brakujących wartości w danych kolumnach:")
print(df.isnull().sum())


# b) Sprawdź czy wszystkie dane numeryczne są z zakresu (0; 15). Dane spoza
# zakresu muszą być poprawione. Możesz tutaj użyć metody: za błędne dane
# podstaw średnią (lub medianę) z danej kolumny.

sepalLengthMedian = df['sepal.length'].median()
sepalWidthMedian = df['sepal.width'].median()
petalLengthMedian = df['petal.length'].median()
petalWidthMedian = df['petal.width'].median()

df[df['sepal.length'] < 0] = sepalLengthMedian
df[df['sepal.length'] > 15] = sepalLengthMedian
df['sepal.length'].fillna(sepalLengthMedian, inplace=True)

df[df['sepal.width'] < 0] = sepalWidthMedian
df[df['sepal.width'] > 15] = sepalWidthMedian
df['sepal.width'].fillna(sepalWidthMedian, inplace=True)

df[df['petal.length'] < 0] = petalLengthMedian
df[df['petal.length'] > 15] = petalLengthMedian
df['petal.length'].fillna(petalLengthMedian, inplace=True)

df[df['petal.width'] < 0] = petalWidthMedian
df[df['petal.width'] > 15] = petalWidthMedian
df['petal.width'].fillna(petalWidthMedian, inplace=True)

# c) Sprawdź czy wszystkie gatunki są napisami: „Setosa”, „Versicolor” lub „Virginica”.
# Jeśli nie, wskaż jakie popełniono błędy i popraw je własną (sensowną) metodą.

df[df['variety'] == "setosa"] = "Setosa"
df[df['variety'] == "Versicolour"] = "Versicolor"
df[df['variety'] == "virginica"] = "Virginica"
