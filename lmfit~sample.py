#!/usr/bin/python
#-*-coding: utf-8 -*-

"""
本程序用于展示如何利用lmfit进行高斯拟合

Author:Enbo Yang
License: GPLv2

"""

#Module Preparing
import numpy as np
import matplotlib.pyplot as plt
'''
也可以使用import pylab as pl
'''

from lmfit.models import GaussianModel

#Read data from file
data=np.loadtxt('**实验数据文件**')
x=data[:,0]
y=data[:,1]

#Preparing the Model
model=GaussianModel()
pars=model.guess(y,x=x)

#Do the fit
result=model.fit(y,pars,x=x)

#Print the fit result
print(result.fit_report(min_correl=0.25))

#Draw the plot
pl.plot(x,y,color='red',linestyle='--')

pl.plot(x,result.best_fit,color='blue',linestyle='-')

#Tobe Continue
