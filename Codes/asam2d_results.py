#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:46:26 2018

@author: abinaya
"""

import numpy as np
import pandas as pd
from os import listdir
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso


results_path = "/Users/abinaya/USC/Studies/NLCI/Project/ASAM-2D-Results/"
results_folders = listdir(results_path)

actual_df = pd.read_csv("/Users/abinaya/USC/Studies/NLCI/Project/Data/continuous_data/test_cont_hardware_-_num_zips_num_colors.csv", header=None)
actual_price = actual_df[2].values


r2_score_df = pd.DataFrame(columns=["Gauss", "Cauchy", "Sinc"])

approx_df = pd.DataFrame()


for folder in results_folders:
    
    print folder
    
    gauss = np.genfromtxt(results_path+folder+'/Gauss/fuzzyFGauss-10000.dat')
    cauchy = np.genfromtxt(results_path+folder+'/Cauchy/fuzzyFCauchy-10000.dat')
    sinc = np.genfromtxt(results_path+folder+'/Sinc/fuzzyFSinc-10000.dat')
    
    gauss_price = gauss[:,2]
    cauchy_price = cauchy[:,2]
    sinc_price = sinc[:,2]
    
    gauss_price = gauss_price[~np.isnan(gauss_price)]
    cauchy_price = cauchy_price[~np.isnan(cauchy_price)]
    sinc_price = sinc_price[~np.isnan(sinc_price)]
    
    r2_score_gauss = r2_score(actual_price, gauss_price)
    r2_score_cauchy = r2_score(actual_price, cauchy_price)
    r2_score_sinc = r2_score(actual_price, sinc_price)
    
    r2_score_df.loc[folder, "Gauss"] = r2_score_gauss
    r2_score_df.loc[folder, "Cauchy"] = r2_score_cauchy
    r2_score_df.loc[folder, "Sinc"] = r2_score_sinc
    
    #approx_df[folder] = cauchy_price
    
    
    if (r2_score_gauss > r2_score_cauchy) & (r2_score_gauss > r2_score_sinc):
        print "gauss"
        approx_df[folder] = gauss_price
    elif (r2_score_cauchy > r2_score_gauss) & (r2_score_cauchy > r2_score_sinc):
        print "cauchy"
        approx_df[folder] = cauchy_price
    elif (r2_score_sinc > r2_score_gauss) & (r2_score_sinc > r2_score_cauchy):
        print "sinc"
        approx_df[folder] = sinc_price
    
    

mean_pred = approx_df.mean(axis=1)
r2_score_mean = r2_score(actual_price, mean_pred)
print(r2_score_mean)  
    
### Linear Regression
lr = Ridge()
lr.fit(approx_df, actual_price)

train_acc_LinReg = lr.score(approx_df, actual_price)

print("Linear Regression - Train accuracy: ",train_acc_LinReg )
