#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 23:40:17 2018

@author: deepikakanade
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.neural_network import MLPRegressor

df_train = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/train.csv")
df_test = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/test.csv")

del df_train["Unnamed: 0"]
del df_test["Unnamed: 0"]

df_train_y = df_train["price"]
df_train_x = df_train.drop("price", axis=1)

df_test_y = df_test["price"]
df_test_x = df_test.drop("price", axis=1)

Hidden_layer_sizes = [(100,), (100,2), (100,3), (250,2), (250,)]
activation = ["identity", "logistic", "tanh", "relu"]
solver = ["lbfgs", "sgd", "adam"]
alpha = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5]
learning_rate = ["invscaling"]

train_acc_MLPReg =[]
test_acc_MLPReg = []

### MLP
for hls in Hidden_layer_sizes:
    for act in activation:
        for sol in solver:
            for al in alpha:
                for lr in learning_rate:
                    print(hls, act, sol, al, lr)
                    lr = MLPRegressor(hidden_layer_sizes = (100,2), activation = act, solver = sol, alpha = al, learning_rate = lr)
                    lr.fit(df_train_x, df_train_y)
                    
                    #print(df_train_x.isnull().any().any(), df_train_y.isnull().any().any())
                        
                    train_acc_MLPReg.append(lr.score(df_train_x, df_train_y))
                    test_acc_MLPReg.append(lr.score(df_test_x, df_test_y))

print("MLP Regression - Train accuracy: ",max(train_acc_MLPReg))
print("MLP Regression - Test accuracy: ",max(test_acc_MLPReg))



#lr = MLPRegressor(hidden_layer_sizes = (100,2), activation = "relu", solver = "lbfgs", alpha = 0.001, learning_rate = "invscaling")
#lr.fit(df_train_x, df_train_y)
#
#train_acc_MLPReg = lr.score(df_train_x, df_train_y)
#test_acc_MLPReg = lr.score(df_test_x, df_test_y)
#
#
#print("MLP Regression - Train accuracy: ",train_acc_MLPReg)
#print("MLP Regression - Test accuracy: ",test_acc_MLPReg)