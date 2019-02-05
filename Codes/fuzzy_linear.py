#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:39:06 2018

@author: abinaya
"""

import numpy as np
import pandas as pd
from os import listdir
from asam_pred import gauss_approx, cauchy_approx, sinc_approx
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR

### continuous fuzzy

results_path = "/Users/abinaya/USC/Studies/NLCI/Project/ASAM-2D-Results/"
results_folders = listdir(results_path)

#results_folders = ['cont_strap_length_volume','cont_num_components_num_colors','cont_strap_length_num_components',
                  #'cont_num_components_volume','cont_num_compartments_num_components']

results_folders = ['cont_num_components_volume']

df_train_approx = pd.DataFrame()    
df_test_approx = pd.DataFrame()    

for folder in results_folders:
    folder = folder[5:]
    print "----------", folder
    
    gauss_par = np.genfromtxt("/Users/abinaya/USC/Studies/NLCI/Project/ASAM-2D-Results/cont_" + folder + "/Gauss/Parameters.par")
    cauchy_par = np.genfromtxt("/Users/abinaya/USC/Studies/NLCI/Project/ASAM-2D-Results/cont_" + folder + "/Cauchy/Parameters.par")
    sinc_par = np.genfromtxt("/Users/abinaya/USC/Studies/NLCI/Project/ASAM-2D-Results/cont_" + folder + "/Sinc/Parameters.par")
    
    
    train_df = pd.read_csv("/Users/abinaya/USC/Studies/NLCI/Project/Data/continuous_data/train_cont_" + folder + ".csv", header=None)
    test_df = pd.read_csv("/Users/abinaya/USC/Studies/NLCI/Project/Data/continuous_data/test_cont_" + folder + ".csv", header=None)
    
    #print train_df.describe()
    #print test_df.describe()
    
    gauss_train_pred = []
    for i in range(0,train_df.shape[0]):
        gauss_train_pred.append(gauss_approx(train_df.iloc[i,0], train_df.iloc[i,1], gauss_par, gauss_par.shape[0]))
    
    cauchy_train_pred = []
    for i in range(0,train_df.shape[0]):
        cauchy_train_pred.append(cauchy_approx(train_df.iloc[i,0], train_df.iloc[i,1], cauchy_par, cauchy_par.shape[0]))
    
    sinc_train_pred = []
    for i in range(0,train_df.shape[0]):
        sinc_train_pred.append(sinc_approx(train_df.iloc[i,0], train_df.iloc[i,1], sinc_par, sinc_par.shape[0]))
    
    
    gauss_test_pred = []
    for i in range(0,test_df.shape[0]):
        gauss_test_pred.append(gauss_approx(test_df.iloc[i,0], test_df.iloc[i,1], gauss_par, gauss_par.shape[0]))
    
    cauchy_test_pred = []
    for i in range(0,test_df.shape[0]):
        cauchy_test_pred.append(cauchy_approx(test_df.iloc[i,0], test_df.iloc[i,1], cauchy_par, cauchy_par.shape[0]))
    
    sinc_test_pred = []
    for i in range(0,test_df.shape[0]):
        sinc_test_pred.append(sinc_approx(test_df.iloc[i,0], test_df.iloc[i,1], sinc_par, sinc_par.shape[0]))
      
    '''
    mse_train_gauss = mean_squared_error(train_df[2], gauss_train_pred)
    mse_train_cauchy = mean_squared_error(train_df[2], cauchy_train_pred)
    mse_train_sinc = mean_squared_error(train_df[2], sinc_train_pred)
    
    if (mse_train_gauss > mse_train_cauchy) & (mse_train_gauss > mse_train_sinc):
        print "gauss"
        df_train_approx[folder] = gauss_train_pred
        df_test_approx[folder] = gauss_test_pred
        
    elif (mse_train_cauchy > mse_train_gauss) & (mse_train_cauchy > mse_train_sinc):
        print "cauchy"
        df_train_approx[folder] = cauchy_train_pred
        df_test_approx[folder] = cauchy_test_pred
        
    elif (mse_train_sinc > mse_train_gauss) & (mse_train_sinc > mse_train_cauchy):
        print "sinc"
        df_train_approx[folder] = sinc_train_pred
        df_test_approx[folder] = sinc_test_pred
    '''
    df_train_approx[folder] = cauchy_train_pred
    df_test_approx[folder] = cauchy_test_pred        


    
### load categorical data    

df_train_categ = pd.read_csv("/Users/abinaya/USC/Studies/NLCI/Project/Data/categorical_data/train_categ_brand_skin_type.csv")
df_test_categ = pd.read_csv("/Users/abinaya/USC/Studies/NLCI/Project/Data/categorical_data/test_categ_brand_skin_type.csv")

df_train_y = df_train_categ["price"]
df_train_categ_x = df_train_categ.drop("price", axis=1)

df_test_y = df_test_categ["price"]
df_test_categ_x = df_test_categ.drop("price", axis=1)


### combine categorical with fuzzy approximation

df_train_x = pd.concat([df_train_categ_x, df_train_approx], axis=1)
df_test_x = pd.concat([df_test_categ_x, df_test_approx], axis=1)
    
### Linear Regression
lr = Lasso()
lr.fit(df_train_x, df_train_y)

train_predict = lr.predict(df_train_x)
test_predict = lr.predict(df_test_x)

train_acc_LinReg = np.sqrt(mean_squared_error(df_train_y, train_predict))
test_acc_LinReg = np.sqrt(mean_squared_error(df_test_y, test_predict))

print("Linear Regression - Train accuracy: ",train_acc_LinReg )
print("Linear Regression - Test accuracy: ",test_acc_LinReg )
