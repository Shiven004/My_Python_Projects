"""
Build a linear regression model on the 'Boston' dataframe where the independent variable is 'rm'
and dependent variable is 'medv'.The training and split data needs to be 80:20
"""
#Loading required packages.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def Linear_Regression_Model_fn():

    #Boston dataset
    boston = pd.read_csv('Boston.csv')
    boston.head()

    #Getting the features and the targets
    x = pd.DataFrame(boston['rm']) #features
    y = pd.DataFrame(boston['medv']) #targets

    #splitting into trainig and test data
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    #Building the model
    linearReg = LinearRegression()
    linearReg.fit(x_train,y_train)

    #predicting the value
    y_predict =linearReg.predict(x_test)
    print('Root Mean square Error:',np.sqrt(metrics.mean_squared_error(y_test,y_predict)))



if __name__  == '__main__':
    print("Linear Regression model process starts...")
    Linear_Regression_Model_fn()
    print("Linear Regression model process completed...")