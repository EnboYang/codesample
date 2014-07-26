!/usr/bin/python

#We need this two module in this sample

import numpy as np
import pylab as pl

#define the varialbes
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)

#define the figure indexes

pl.figure(figsize=(8,6),dpi=80)
#figure size with the unit
#are inch

pl.subplot(1,1,1)
#this line is usually used for draw more
#than one pictures

#draw part
pl.plot(x,c,color='blue',linewidth=1.0,linestyle='-')
pl.plot(x,s,color='red',linewidth=2.0,linestyle='--')

#setting the range of X & Y
pl.xlim(x.min()*1.1,x.max()*1.1)
pl.ylim(c.min()*1.1,c.max()*1.1)

#settiong the ticks
pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.yticks(np.linspace(-1,1,5,endpoint=True))
#or we can tell python which ticks shoule be displayed
'''
pl.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
pl.yticks([-1,0,1])
#pay attention to the '[]',it's very important
'''

