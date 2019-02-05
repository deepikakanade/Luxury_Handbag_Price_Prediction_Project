#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:00:05 2018

@author: abinaya
"""

import numpy as np
import pandas as pd
import math


def gauss_approx(xin, yin, gauss_par, NUMRULES):
    
    num=0.0
    dengs = 0.0
    
    xmdgs = np.zeros(NUMRULES)
    ymdgs = np.zeros(NUMRULES)
    a = np.zeros(NUMRULES)

    for i in range(NUMRULES):
        mean_x = gauss_par[i,0]
        mean_y = gauss_par[i,1]
        disp_x = gauss_par[i,2]
        disp_y = gauss_par[i,3]
        centroid = gauss_par[i,4]
        volume = gauss_par[i,5]
        			                     
        xmdgs[i] = (xin- mean_x) / disp_x                       
        ymdgs[i] = (yin- mean_y) / disp_y                                
        a[i] = np.exp(-(xmdgs[i] * xmdgs[i]) - (ymdgs[i] * ymdgs[i])) 
        av = a[i] * volume              
        dengs = dengs + av			  
        num = num + av * centroid		  
    
    if (dengs != 0.0): 
        return num/dengs
    else:
        return 0.0

def cauchy_approx(xin, yin, gauss_par, NUMRULES):
    denchy = 0.0
    num = 0.0
    xmdchy = np.zeros(NUMRULES)
    ymdchy = np.zeros(NUMRULES)
    a = np.zeros(NUMRULES)
    
    for i in range(NUMRULES): 
        mean_x = gauss_par[i,0]
        mean_y = gauss_par[i,1]
        disp_x = gauss_par[i,2]
        disp_y = gauss_par[i,3]
        centroid = gauss_par[i,4]
        volume = gauss_par[i,5]
        
        xmdchy[i] = (xin - mean_x) / disp_x
        ymdchy[i] = (yin - mean_y) / disp_y
        cx = 1.0/(1.0 + xmdchy[i]*xmdchy[i])
        cy = 1.0/(1.0 + ymdchy[i]*ymdchy[i])

        a[i] = cx * cy;
        av = a[i] * volume
        denchy = denchy+av;
        num = num + av * centroid
        
    if (denchy != 0.0):
        return num/denchy;
    else:
        return 0.0;


def sinc_approx(xin, yin, gauss_par, NUMRULES): 
    num=0.0
    av=0
    num=0
    densinc = 0
    xmdsinc = np.zeros(NUMRULES)
    ymdsinc = np.zeros(NUMRULES)
    a = np.zeros(NUMRULES)

    for i in range(NUMRULES):
        mean_x = gauss_par[i,0]
        mean_y = gauss_par[i,1]
        disp_x = gauss_par[i,2]
        disp_y = gauss_par[i,3]
        centroid = gauss_par[i,4]
        volume = gauss_par[i,5]

        xmdsinc[i] = (xin - mean_x)/disp_x
        ymdsinc[i] = (yin - mean_y)/disp_y
		  
        if (xmdsinc[i] == 0.0):
            sx = 1.0;
        else:
            sx = math.sin(xmdsinc[i])/xmdsinc[i]; 
        if(ymdsinc[i] == 0.0):
            sy = 1.0;
        else:
            sy = math.sin(ymdsinc[i])/ymdsinc[i];
    
        a[i] = sx * sy;
        av = a[i] * volume
        densinc = densinc + av
        num = num + av * centroid
        
    if (densinc != 0.0):
        return num/densinc
    else:
        return 0.0 
    
    