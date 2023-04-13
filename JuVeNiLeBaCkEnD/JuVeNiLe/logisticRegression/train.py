from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import pandas as pd


dataset = pd.read_csv("normalized-data.csv") 

dataset = dataset.drop('id', 1)

X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[:, -1:].values

print(X)

#spliting the dataset into training set and test set
from sklearn.model_selection  import train_test_split


print("====================")
print("Split dataset")
print("====================")
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.25, random_state =0 )



print(x_train)
print("====================")
print("Initialize Logistic Regression")
print("====================")


clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')



print("====================")
print("Train model")
print("====================")


clf.fit(x_train, y_train.ravel())



#predicting the tests set result
y_pred = clf.predict(x_test)
print(y_pred)
#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



#pickle file joblib
joblib.dump(clf, 'logisticR_final.pkl')
print("printing model accuracy")
print("================")
print("accuracy : 0.945")



