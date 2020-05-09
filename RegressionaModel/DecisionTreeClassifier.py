"""
Build a decsion tree classifier model on the 'iris' dataframe where the dependent variable is 'Species'
and independent variable are the rest of the columns.The training and split data needs to be 70:30
"""
#Loading required packages.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def Decision_Tree_Classifier_Model_fn():

    #iris dataset
    iris = pd.read_csv('Iris.csv')
    iris.head()

    #Getting the features and the targets
    x = pd.DataFrame(iris[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']]) #features
    y = iris['Species'] #targets

    #splitting into trainig and test data
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

    #Building the model
    classifier = DecisionTreeClassifier()
    classifier.fit(x_train,y_train)

    #predicting the value
    y_predict =classifier.predict(x_test)
    print('Confusion matrix is :')
    print(confusion_matrix(y_test,y_predict))
    print('Accuracy score:',accuracy_score(y_test,y_predict))
    



if __name__  == '__main__':
    print("Decision_Tree Classifier Model process started...")
    Decision_Tree_Classifier_Model_fn()
    print("Decision Tree Classifier Model process completed...")