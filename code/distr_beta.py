# -*- coding: utf-8 -*-
from numpy import *
from scipy.stats import dweibull

import matplotlib as mpl
mpl.use("pgf")
pgf_with_pdflatex = {
    "font.family": "serif",
    "font.serif": [],
    "font.size" : 11.0,
    "pgf.preamble": [
         r"\usepackage[utf8]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
         r"\usepackage{newtxtext}",
         r"\usepackage{bm}",
         r"\usepackage{amsmath,amsthm}"
         ]
}
mpl.rcParams.update(pgf_with_pdflatex)
# blue, violet, green, brown, red ,orange
mpl.rcParams['axes.color_cycle'] = ['k', 'k','k', 'k', 'k', 'k']
import matplotlib.pyplot as plt
f, ax = plt.subplots(1,3,figsize=(2*0.8*4,1*0.8*3))

plt.gcf().subplots_adjust(bottom=0.15)
data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/Data_l_0.250000.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[0].hist(data, bins=linspace(0,5,18), normed=True, facecolor="white")

m = linspace(0,10,3000)
ax[0].plot(m, 2*dweibull.pdf(m, 1.5,0,1),"k--", linewidth=1.5)
ax[0].set_ylim(0,0.9)
ax[0].set_xlabel(ur"$m$")
ax[0].set_ylabel(ur"$P(m)$")
print 1.5,1

data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/Data_l_0.500000.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[1].hist(data, bins=linspace(0,5,30), normed=True, facecolor="white")

m = linspace(0,10,3000)
ax[1].plot(m, 2.1*dweibull.pdf(m, 2.1,0.0,1.1),"k--", linewidth=1.5)
ax[1].set_xlim(0,5)
ax[1].set_title(ur"Model $\beta$ Weibull comparison", fontsize=11)
ax[1].set_ylim(0,1)
ax[1].set_xlabel(ur"$m$")
print 2.1,1.1

data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/Data_l_0.900000.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[2].hist(data, bins=linspace(0,5,50), normed=True, facecolor="white")

m = linspace(0.45,10,3000)
ax[2].plot(m, 2.1*dweibull.pdf(m, 3,0.45,.6),"k--", linewidth=1.5)
ax[2].set_xlim(0,3)
ax[2].set_xlabel(ur"$m$")
print 3,0.6
plt.savefig("../benchmark/fig4.png")
plt.savefig("../benchmark/fig4.pgf")





