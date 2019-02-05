#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:20:03 2018

@author: deepikakanade
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


brand_list = ['Tom Ford', 'Louis Vitton', 'Gucci', 'Celine', 'Hermes', 'Chanel']

for brand in brand_list:
    print ('\n\n')
    print ('Brand is:' , brand)
    df_train = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/train.csv")
    df_test = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/test.csv")

    del df_train["Unnamed: 0"]
    del df_test["Unnamed: 0"]
    
    df_train = df_train[df_train["brand"] == brand]
    df_test = df_test[df_test["brand"] == brand]
    
    df_train_y = df_train["price"]
    df_train_x = df_train.drop(["price", "brand"], axis=1)

    df_test_y = df_test["price"]
    df_test_x = df_test.drop(["price", "brand"], axis=1)

    ### Linear Regression
    lr = Ridge(alpha = 3)
    lr.fit(df_train_x, df_train_y)
    y_pred = lr.predict(df_test_x)
    rmse = np.sqrt(mean_squared_error(df_test_y, y_pred))
    train_acc_LinReg = lr.score(df_train_x, df_train_y)
    test_acc_LinReg = lr.score(df_test_x, df_test_y)
    
    print("Linear Regression - Train accuracy: ",train_acc_LinReg )
    print("Linear Regression - Test accuracy: ",test_acc_LinReg )
    print ("LR RMSE: ", rmse)
    
    ### Logistic Regression
    logr = LogisticRegression(C=1)
    logr.fit(df_train_x, df_train_y)
    y_pred = logr.predict(df_test_x)
    rmse = np.sqrt(mean_squared_error(df_test_y, y_pred))
    train_acc_LogReg = logr.score(df_train_x, df_train_y)
    test_acc_LogReg = logr.score(df_test_x, df_test_y)
    
    print("Logistic Regression - Train accuracy: ",train_acc_LogReg )
    print("Logistic Regression - Test accuracy: ",test_acc_LogReg )
    print ("LogR RMSE: ", rmse)
    
    ### SVR
    svr = SVR(C=0.95, epsilon=0.2, kernel = 'poly',gamma=15.0)
    svr.fit(df_train_x, df_train_y)
    y_pred = svr.predict(df_test_x)
    y_pred = svr.predict(df_test_x)
    rmse = np.sqrt(mean_squared_error(df_test_y, y_pred))
    train_acc_svr = svr.score(df_train_x, df_train_y)
    test_acc_svr = svr.score(df_test_x, df_test_y)
    
    print("SVR - Train accuracy: ",train_acc_svr)
    print("SVR - Test accuracy: ",test_acc_svr)
    print ("SVR RMSE: ", rmse)