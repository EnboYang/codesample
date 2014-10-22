#!/usr/bin/python

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
pl.plot(x,c,color='blue',linewidth=1.0,linestyle='-',label='cosine')
pl.plot(x,s,color='red',linewidth=2.0,linestyle='--',label='sine')
pl.legend(loc='upper left')

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
  #If you set the tick labels, use this
'''
  pl.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],['$-\pi$','$\pi$','$0$','$\pi/2$','$\pi$'])
  pl.yticks([-1,0,1],['$-1$','$0$','$+1$'])
'''

#Moving the spines
ax=pl.gca()#gca stands for the current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')#let the 'right' & 'top' hided
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
	# change the position of spines
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#Annoatate some points
t=2*np.pi/3
pl.plot([t,t],[0,np.cos(t)],color='blue',linewidth=2.5,linestyle='--')
pl.scatter([t,],[np.cos(t),],50,color='blue')

pl.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',xy=(t, np.sin(t)), xycoords='data',xytext=(+10, +30), textcoords='offset points', fontsize=16,arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#change the details of ticks

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.65))


