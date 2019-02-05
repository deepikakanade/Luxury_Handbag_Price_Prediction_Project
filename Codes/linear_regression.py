#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:11:43 2018

@author: deepika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

df_train = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/train.csv")
df_test = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/test.csv")

del df_train["Unnamed: 0"]
del df_test["Unnamed: 0"]

df_train_y = df_train["price"]
df_train_x = df_train.drop(["price"], axis=1)

df_test_y = df_test["price"]
df_test_x = df_test.drop(["price"], axis=1)

### Linear Regression
lr = Ridge()
lr.fit(df_train_x, df_train_y)
y_pred = lr.predict(df_test_x)
y_pred_train = lr.predict(df_train_x)
rmse = np.sqrt(mean_squared_error(df_test_y, y_pred))
rmse_train = np.sqrt(mean_squared_error(df_train_y, y_pred_train))
train_acc_LinReg = lr.score(df_train_x, df_train_y)
test_acc_LinReg = lr.score(df_test_x, df_test_y)

print("Linear Regression - Train accuracy: ",train_acc_LinReg )
print("Linear Regression - Test accuracy: ",test_acc_LinReg)
print ("LR RMSE: ", rmse)
print ("LR RMSE train: ", rmse_train)

#### Logistic Regression
logr = LogisticRegression(C=1)
logr.fit(df_train_x, df_train_y)

train_acc_LogReg = logr.score(df_train_x, df_train_y)
test_acc_LogReg = logr.score(df_test_x, df_test_y)

print("Logistic Regression - Train accuracy: ",train_acc_LogReg )
print("Logistic Regression - Test accuracy: ",test_acc_LogReg )

### SVR
svr = SVR(C=10, epsilon=0.2 , kernel = 'poly', gamma=15.0)
svr.fit(df_train_x, df_train_y)
y_pred = svr.predict(df_test_x)
y_pred_train = svr.predict(df_train_x)
rmse = np.sqrt(mean_squared_error(df_test_y, y_pred))
rmse_train = np.sqrt(mean_squared_error(df_train_y, y_pred_train))
train_acc_svr = svr.score(df_train_x, df_train_y)
test_acc_svr = svr.score(df_test_x, df_test_y)

print("SVR - Train accuracy: ",train_acc_svr)
print("SVR - Test accuracy: ",test_acc_svr)
print ("SVR RMSE: ", rmse)
print ("SVR RMSE train: ", rmse_train)
