import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.metrics import confusion_matrix


df = pd.read_csv("diabetes.csv")

# a) Podziel w losowy sposób bazę danych irysów na zbiór treningowy i zbiór
# testowy w proporcjach 70%/30%. Wyświetl oba zbiory. Podziel te zbiory na
# cztery części (inputy i class), jeśli jest taka potrzeba

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=13)

train_inputs = train_set[:, 0:8]
train_classes = train_set[:, 8]
test_inputs = test_set[:, 0:8]
test_classes = test_set[:, 8]


# b) Zainicjuj drzewo decyzyjne metodą DecisionTreeClassifier.
dtc = DecisionTreeClassifier()


# c) Wytrenuj drzewo decyzyjne na zbiorze treningowym, wykorzystując funkcję fit.
dtc.fit(train_inputs, train_classes)


# d) Wyświetl drzewo w formie tekstowej i/lub w formie graficznej.
r = export_text(dtc)
print(r)


# e) Dokonaj ewaluacji klasyfikatora, Wyświetl dokładność klasyfikatora, czyli procent
# poprawnych odpowiedzi.

print(dtc.score(test_inputs, test_classes))


# f) Wyświetl macierz błędów (ang. confusion matrix), która zestawia liczby
# błędnych i poprawnych odpowiedzi, dla wszystkich klas.

pred = dtc.predict(test_inputs)
matrix = confusion_matrix(test_classes, pred)
print(matrix)