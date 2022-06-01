import pandas as pd


# a) Rozpocznij od przygotowania zbioru treningowego i testowego, tak jak w
# poprzednim zadaniu

df = pd.read_csv("iris.csv")
from sklearn.model_selection import train_test_split
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=274937)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]


# b) Napiszemy w Pythonie funkcję, która na podstawie czterech numerycznych
# parametrów irysa odgadnie jego gatunek wykorzystując do tego jedynie dwie
# instrukcje if, elif oraz else (jednokrotnie).

def classify_iris1(sl, sw, pl, pw):
    if sl > 4:
        return ("setosa")
    elif pl <= 5:
        return ("virginica")
    else:
        return ("versicolor")


# c) Chcemy teraz tę funkcję uruchomić dla wszystkich irysów ze zbioru testowego i
# zliczyć ile razy dobrze zgadnie odmianę irysa.

good_predictions1 = 0
len = test_set.shape[0]

for i in range(len):
    if classify_iris1(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2], test_inputs[i][3]) == test_classes[i]:
        good_predictions1 += 1

print(good_predictions1)
print(good_predictions1 / len * 100, "%")


# d) Pora na poprawienie funkcji classify_iris, tak aby działała lepiej

def classify_iris2(sl, sw, pl, pw):
    if pw < 0.5:
        return ("setosa")
    elif pw <= 1.9 and pl <= 5.6:
        return ("versicolor")
    else:
        return ("virginica")


good_predictions2 = 0

for i in range(len):
    if classify_iris2(test_inputs[i][0], test_inputs[i][1], test_inputs[i][2], test_inputs[i][3]) == test_classes[i]:
        good_predictions2 += 1

print(good_predictions2)

print(good_predictions2 / len * 100, "%")