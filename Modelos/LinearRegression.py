from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


iris = load_iris()

X=iris.data
y=iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2) #random_state=42)

#Creando dos modelos uno de Linear regression y uno de Decision tree classifier
lr=LinearRegression()
dtc=DecisionTreeClassifier()
svc=LinearSVC(multi_class='crammer_singer')

import pickle

lr.fit(X_train,y_train)
dtc.fit(X_train, y_train)
svc.fit(X_train, y_train)

test_data=X_test[15]
#test_data=[5.1,3.5,1.4,0.2]
print("LR:",lr.predict([test_data]))
print("DTC:",dtc.predict([test_data]))
print("SVC:",svc.predict([test_data]))

pickle.dump(lr, open('model_lr.pkl','wb'))
pickle.dump(dtc, open('model_dtc.pkl','wb'))
pickle.dump(svc, open('model_svc.pkl','wb'))




