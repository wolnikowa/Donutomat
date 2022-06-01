
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # visualization
from sklearn.neural_network import MLPClassifier # neural network
from sklearn.model_selection import train_test_split
from sklearn import metrics


data = pd.read_csv("iris.csv")
data.sample(5)

data.head(5)
sns.pairplot( data=data, vars=('SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'), hue='Species' )
data.describe()

df_norm = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
df_norm.sample(n=5)

df_norm.describe()

target = data[['Species']].replace(['setosa','versicolor','virginica'],[0,1,2])
target.sample(n=5)

df = pd.concat([df_norm, target], axis=1)
df.sample(n=5)

train, test = train_test_split(df, test_size = 0.3)
trainX = train[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]# taking the training data features
trainY=train.Species# output of our training data
testX= test[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']] # taking test data features
testY =test.Species   #output value of test data
trainX.head(5)

trainY.head(5)
trainX.head(5)
testY.head(5)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3), random_state=1)


clf.fit(trainX, trainY)
prediction = clf.predict(testX)
print(prediction)
print(testY.values)

print('The accuracy of the Multi-layer Perceptron is:',metrics.accuracy_score(prediction,testY))









