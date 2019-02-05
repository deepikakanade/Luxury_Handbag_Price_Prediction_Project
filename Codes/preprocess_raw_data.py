#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 14:22:45 2018

@author: deepika
"""

import pandas as pd
import numpy as np

df_raw = pd.read_excel("/Users/deepikakanade/Documents/EE_500/Project/Data/raw_data.xlsx")

# delete columns
df_raw.drop(['s no', 'bag name', 'usage type', 'launch season', 'launch year', 
             'production type','place of manufacture', 'demand', 'num hours', 'num people',
            'skin source', 'description', 'URL'], axis=1, inplace=True)

# brand
df_raw.loc[df_raw["brand"] == "chanel", "brand"] = "Chanel" 

# bag style
df_raw.loc[df_raw["bag style"] == "Shoulder bag", "bag style"] = "Shoulder Bag"
df_raw.loc[df_raw["bag style"] == "shoulder bag", "bag style"] = "Shoulder Bag"
df_raw.loc[df_raw["bag style"] == "shoulder Bag", "bag style"] = "Shoulder Bag"
df_raw.loc[df_raw["bag style"] == "Handle bag", "bag style"] = "Handle Bag"
df_raw.loc[df_raw["bag style"] == "purse", "bag style"] = "Purse"
df_raw.loc[df_raw["bag style"] == "Hatbox", "bag style"] = "Shoulder Bag"
df_raw["bag style"] = df_raw["bag style"].fillna("Clutch")

# hardware - metal type
df_raw.loc[df_raw["hardware - metal type"] == "gold", "hardware - metal type"] = "Gold"
df_raw.loc[df_raw["hardware - metal type"] == "Palladium, Ruthenium", "hardware - metal type"] = "Ruthenium"
df_raw.loc[df_raw["hardware - metal type"] == "silver", "hardware - metal type"] = "Silver"
df_raw.loc[df_raw["hardware - metal type"] == "Silver/Gold", "hardware - metal type"] = "Silver"
df_raw.loc[df_raw["hardware - metal type"] == "Gold Brass", "hardware - metal type"] = "Gold"
df_raw.loc[df_raw["hardware - metal type"] == "gold, ruthenium", "hardware - metal type"] = "Ruthenium"
df_raw.loc[df_raw["hardware - metal type"] == "ruthenium", "hardware - metal type"] = "Ruthenium"
df_raw.loc[df_raw["hardware - metal type"] == "Gold-", "hardware - metal type"] = "Gold"
df_raw.loc[df_raw["hardware - metal type"] == "Silver, Gold", "hardware - metal type"] = "Silver"
df_raw.loc[df_raw["hardware - metal type"] == "Gold, resin", "hardware - metal type"] = "Gold"
df_raw.loc[df_raw["hardware - metal type"] == "Permabrass", "hardware - metal type"] = "Brass"
df_raw.loc[df_raw["hardware - metal type"] == "Aluminium", "hardware - metal type"] = "Ruthenium"
df_raw.loc[df_raw["hardware - metal type"] == "Aluminium, Ruthenium", "hardware - metal type"] = "Ruthenium"
df_raw.loc[df_raw["hardware - metal type"] == "Gold ", "hardware - metal type"] = "Gold"
df_raw["hardware - metal type"] = df_raw["hardware - metal type"].fillna("None")

# hardware - strap type
df_raw.loc[df_raw["hardware - strap type"] == "metal, Leather", "hardware - strap type"] = "Metal,Leather"
df_raw.loc[df_raw["hardware - strap type"] == "Metal, Leather", "hardware - strap type"] = "Metal,Leather"
df_raw.loc[df_raw["hardware - strap type"] == "metal", "hardware - strap type"] = "Metal"
df_raw.loc[df_raw["hardware - strap type"] == "leather", "hardware - strap type"] = "Leather"

#df_raw = df_raw.loc[df_raw["hardware - strap type"]!="Bamboo"]
df_raw["hardware - strap type"] = df_raw["hardware - strap type"].fillna("None")


# strap length
df_raw["strap length"] = df_raw["strap length"].fillna(20)


# major color
df_raw.loc[df_raw["major color"] == "black" ,"major color"] = "Black"
df_raw.loc[df_raw["major color"] == "red" ,"major color"] = "Red"
df_raw.loc[df_raw["major color"] == "white" ,"major color"] = "White"
df_raw.loc[df_raw["major color"] == "pink" ,"major color"] = "Pink"
df_raw.loc[df_raw["major color"] == "yellow" ,"major color"] = "Yellow"
df_raw.loc[df_raw["major color"] == "green" ,"major color"] = "Green"
df_raw.loc[df_raw["major color"] == "blue" ,"major color"] = "Blue"
df_raw.loc[df_raw["major color"] == "orange" ,"major color"] = "Orange"
df_raw.loc[df_raw["major color"] == "Multicolored" ,"major color"] = "Multicolor"


# convert height, width and breadth
df_raw.loc[df_raw["brand"] == "Tom Ford", "height"] = df_raw.loc[df_raw["brand"] == "Tom Ford", "height"] *  0.394
df_raw.loc[df_raw["brand"] == "Tom Ford", "width"] = df_raw.loc[df_raw["brand"] == "Tom Ford", "width"] *  0.394
df_raw.loc[df_raw["brand"] == "Tom Ford", "breadth"] = df_raw.loc[df_raw["brand"] == "Tom Ford", "breadth"] *  0.394

# volume 
df_raw["volume"] = df_raw["height"] * df_raw["width"] * df_raw["breadth"]

# delete height, width and breadth
df_raw.drop(['height', 'width', 'breadth'], axis=1, inplace=True)

# inner material
df_raw.loc[df_raw["inner material"] == "satin" ,"inner material"] = "Satin"
df_raw.loc[df_raw["inner material"] == "Sheepskin" ,"inner material"] = "Sheep"
df_raw.loc[df_raw["inner material"] == "Leather" ,"inner material"] = "Calf"
df_raw.loc[df_raw["inner material"] == "leather" ,"inner material"] = "Calf"
df_raw.loc[df_raw["inner material"] == "Sheep Leather" ,"inner material"] = "Sheep"
df_raw.loc[df_raw["inner material"] == "Leather and Viscose" ,"inner material"] = "Calf"
df_raw.loc[df_raw["inner material"] == "Leather " ,"inner material"] = "Calf"
df_raw.loc[df_raw["inner material"] == "Camel microfiber" ,"inner material"] = "Camel"
df_raw.loc[df_raw["inner material"] == "Lambskin" ,"inner material"] = "Lamb"
df_raw.loc[df_raw["inner material"] == "Cowhide" ,"inner material"] = "Calf"
df_raw.loc[df_raw["inner material"] == "Alcantraa" ,"inner material"] = "Seude"
df_raw.loc[df_raw["inner material"].isin(["Silk","Cotton","Wool","tweed","Textile","Malletage","Camel","Lamb"]),"inner material"] = "Others"
df_raw["inner material"] = df_raw["inner material"].fillna("Others")

df_raw.to_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/clean_data.csv")

'''
# Unique skin types
skin_types = df_raw['skin type'].unique()
unique_skin_type = []
for i in range(len(skin_types)):
    unique_skin_type += skin_types[i].split(", ")
    
unique_skin_type = np.unique(unique_skin_type)
'''
