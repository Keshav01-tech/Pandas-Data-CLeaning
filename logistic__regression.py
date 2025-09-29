from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
iris = datasets.load_iris()
print(iris.keys()) 
x= iris['data'][:,3:]
y= (iris['target']==2).astype(np.int_)
clf = LogisticRegression()
clf.fit(x,y)
example = clf.predict(([[3]]))
x_new = np.linspace(0,3,1000).reshape(-1,1)
y_new = clf.predict_proba(x_new)
plt.plot(x_new,y_new[:,1] )
plt.show()