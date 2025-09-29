from sklearn.neighbors import  KNeighborsClassifier
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
print(iris.DESCR)
feautures = iris.data
lables = iris.target
print(feautures[0],lables[0])
clf = KNeighborsClassifier()
clf.fit(feautures,lables)
while True:
    user_input = input("Enter 4 feature values separated by commas (e.g., 2.3, 4.5, 1.2, 0.7): ")


    features = np.array([list(map(float, user_input.split(',')))]).reshape(1, -1)


    prediction = clf.predict(features)
    print("Predicted class:", prediction[0])

