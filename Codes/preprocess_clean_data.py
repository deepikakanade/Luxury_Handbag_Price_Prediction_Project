#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:52:39 2018

@author: deepika
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split



def preprocess_clean_data(df, train_for_index, test_for_index, process_continuous):
    
    continuous_features_all = ["hardware - num zips", "strap length", "num compartments", "num components", "num colors", "volume", "num functionality"]
    categorical_ordered_features_all = ["hardware - metal type", "hardware - strap type", "inner material"]
    categorical_unordered_features_all = ["accessories", "bag style", "major color"]
    #categorical_unordered_features_all = ["accessories", "bag style", "major color"]
    others_all = ["skin type"]
    #others_all = []
    
    continuous_features = list(set(df.columns) & set(continuous_features_all))
    categorical_ordered_features = list(set(df.columns) & set(categorical_ordered_features_all))
    categorical_unordered_features = list(set(df.columns) & set(categorical_unordered_features_all))
    others = list(set(df.columns) & set(others_all))
        
    ### One hot encoding Categorical Un-ordered Features  
    if len(categorical_unordered_features) > 0:
        for feat in categorical_unordered_features:
            print ("\n--------- One Hot Encoding feature --------- ",feat)
            one_hot_encoded_df = pd.get_dummies(df[feat], prefix=feat)
            df = pd.concat([df,one_hot_encoded_df], axis=1) #concatenate old columns with new one hot encoded columns
        df = df.drop(categorical_unordered_features, axis=1)
        
        
    ### Label Categorical Ordered Features
    if len(categorical_ordered_features) > 0:
        label_dict = {'hardware - metal type':{'None':0, 'Leather':1, 'Silver':2, 'Brass':3, 'Ruthenium':4, 'Gold':5, 'Palladium':6},
                      'hardware - strap type':{'None':0, 'Metal':1, 'Metal,Leather':2, 'Leather':3},
                      'inner material':{'Sheep':0, 'Seude':1, 'Others':2, 'Microfiber':3, 'Satin':4, 'Calf':5}}
                      #'skin type' : {'Calf, Others':0, 'Leather, Embroidery':1, 'Canvas, Embroidery':2, 'Python':3, 'Canvas':4, 'Epi':5, 'Leather':6 , 'Embroidery, Crystal, Others':7, 'Snake':8, 'Calf':9, 'Lamb':10, 'Embroidery, Crystal':11,
                      #'Embroidery, Others':12, 'Others' :13, 'Calf, Python' :14, 'Lizard':15, 'Lamb, Python':16, 'Lizard, Lamb':17, 'Crystal':18, 'Crystal, Others':19, 'Embroidery':20, 'Alligator':21 , 'Crocodile':22},
                      #'brand' : {'Louis Vitton':0, 'Gucci':1, 'Celine':2, 'Tom Ford':3, 'Hermes':4, 'Chanel':5}}
        
        for feat in categorical_ordered_features:
            print ("\n--------- Labelling feature --------- ",feat)
            df = df.replace({feat:label_dict[feat]})
            print ("Labelled as: ",label_dict[feat])
            
    
    ### fix skin types            
    if len(others) > 0:
        print ("\n--------- One hot encoding - skin type --------- ")
        # Unique skin types
        skin_types = df['skin type'].unique()
        unique_skin_type = []
        for i in range(len(skin_types)):
            unique_skin_type += skin_types[i].split(", ")
            
        unique_skin_type = np.unique(unique_skin_type)
        unique_skin_type = ["skin type_"+i for i in unique_skin_type]
        # encode skin types
        df_skin = pd.DataFrame(columns=unique_skin_type)
        for index in range(len(df)):
            skin_list = df.loc[index, "skin type"].split(", ")
            skin_list = ["skin type_"+i for i in skin_list]
            df_skin.loc[index, skin_list] = 1
        df_skin = df_skin.fillna(0)
        #add and drop
        df = pd.concat([df,df_skin], axis=1)
        df = df.drop('skin type', axis=1)
        
    
    ### split train and test data
    df_train = df.loc[train_for_index.index] 
    df_test = df.loc[test_for_index.index]   
    
    
    ### Normalization or Standardization of Continuous Features    
    if len(continuous_features) > 0:
        if process_continuous == "Standardize":
            print ("\n--------- Standardizing Continuous Features (Mean=0, Standard Deviation=1) --------- ")
            standardization = StandardScaler()
            standardization.fit(df_train[continuous_features])
            df_train[continuous_features] = standardization.transform(df_train[continuous_features])
            df_test[continuous_features] = standardization.transform(df_test[continuous_features])
        
        elif process_continuous == "Normalize":
            print ("\n--------- Normalizing Continuous Features (Min=0, Max=1) --------- ")
            min_max_scaling = MinMaxScaler()
            min_max_scaling.fit(df[continuous_features])
            df_train[continuous_features] = min_max_scaling.transform(df_train[continuous_features])
            df_test[continuous_features] = min_max_scaling.transform(df_test[continuous_features])
        
    
    ### save
    df.to_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/preprocessed.csv")
    df_train.to_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/train.csv")
    df_test.to_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/test.csv")
    
    return df, df_train, df_test


df = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/clean_data.csv")
train_for_index, test_for_index = train_test_split(df, test_size=0.2, random_state=0, stratify=df[["brand"]])

selected_columns = ["hardware - num zips", "strap length", "num compartments", "num components", "num colors", "volume", "num functionality", "hardware - metal type", "hardware - strap type", "inner material", 
                    "accessories", "bag style", "major color","skin type" ]

df = df[selected_columns+["price"]]

df_preprocess, df_train, df_test = preprocess_clean_data(df, train_for_index, test_for_index, "Standardize")

                                                     
