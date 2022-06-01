import numpy
import math
import random
#a
wektor1 = numpy.array([3, 8, 9, 10, 12])
wektor2 = numpy.array([8, 7, 7, 5, 6])
print(wektor1+wektor2)
print(wektor1*wektor2)
#b
print(numpy.sum(wektor1*wektor2))
# c
print(math.sqrt(numpy.sum((wektor1)**2)))
print(math.sqrt(numpy.sum((wektor2)**2)))
# d
pointD=[]
for i in range(0,50):
    x=random.randrange(1,101)
    pointD.append(x)
print(pointD)
#e
print(sum(pointD))
print(min(pointD))
print(max(pointD))
print(numpy.mean(pointD))
print(numpy.std(pointD))
#f
normalized=[]
for i in pointD:
    n=(i-min(pointD))/(max(pointD)-min(pointD))
    normalized.append(n)
print(normalized)
max_index = numpy.argmax(pointD)
print('max było na pozycji: ',max_index,'i wynosilo: ',max(pointD),'. Teraz na tej pozycji jest: ',normalized[max_index])

#g
standarized=[]
for i in pointD:
    n=(i-numpy.mean(pointD))/numpy.std(pointD)
    standarized.append(n)
print(standarized)
print(numpy.mean(standarized))
print(numpy.std(standarized))

#h
dyskretyzacja=[]
for i in pointD:
    string=str(i)
    start=i-int(string[len(string)-1])
    end=start+10
    range="[{}, {})".format(start,end)
    # range=(start,end)
    dyskretyzacja.append(range)
print(dyskretyzacja)