#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:54:56 2018

@author: deepika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
import operator 
import itertools

df = pd.read_csv("/Users/deepikakanade/Documents/EE_500/Project/Data/clean_data.csv")

### inner material

median_inner_material = {}
for key in df["inner material"].unique():
     median_inner_material[key] =  df.loc[df["inner material"] == key, "price"].median()

plt.figure()
plt.bar(range(len(median_inner_material)), median_inner_material.values(), align='center')
plt.xticks(range(len(median_inner_material)), list(median_inner_material.keys()))


### hardware - metal type

median_hardware_metal_type = {}
for key in df["hardware - metal type"].unique():
     median_hardware_metal_type[key] =  df.loc[df["hardware - metal type"] == key, "price"].median()

plt.figure()
plt.bar(range(len(median_hardware_metal_type)), median_hardware_metal_type.values(), align='center')
plt.xticks(range(len(median_hardware_metal_type)), list(median_hardware_metal_type.keys()))


### hardware - strap type

median_hardware_strap_type = {}
for key in df["hardware - strap type"].unique():
     median_hardware_strap_type[key] =  df.loc[df["hardware - strap type"] == key, "price"].median()

plt.figure()
plt.bar(range(len(median_hardware_strap_type)), median_hardware_strap_type.values(), align='center')
plt.xticks(range(len(median_hardware_strap_type)), list(median_hardware_strap_type.keys()))


### brand

median_brand = {}
for key in df["brand"].unique():
     median_brand[key] =  df.loc[df["brand"] == key, "price"].median()

plt.figure()
plt.bar(range(len(median_brand)), median_brand.values(), align='center')
plt.ylabel('Price')
plt.xticks(range(len(median_brand)), list(median_brand.keys()))

### skin_type

median_skin_type = {}
for key in df["skin type"].unique():
     median_skin_type[key] =  df.loc[df["skin type"] == key, "price"].median()

plt.figure()
plt.bar(range(len(median_skin_type)), median_skin_type.values(), align='center')
plt.ylabel('Price')
plt.xticks(range(len(median_skin_type)), list(median_skin_type.keys()), rotation=45)
