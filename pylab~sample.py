!/usr/bin/python

#We need this two module in this sample

import numpy as np
import pylab as pl

#define the varialbes
x=np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s=np.cos(x),np.sin(x)

#define the figure indexes

pl.figure(figsize=(8,6),dpi=80)
pl.subplot(1,1,1)
pl.plot(x,c,color='blue',linewidth=1.0,linestyle='-')
pl.plot(x,s,color='red',linewidth=2.0,linestyle='--')
pl.xlim(-4,4)
pl.ylim(-1,1)
pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.yticks(np.linspace(-1,1,5,endpoint=True))


