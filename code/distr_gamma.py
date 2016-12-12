# -*- coding: utf-8 -*-
from numpy import *
from scipy.stats import pareto, expon

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
f, ax = plt.subplots(2,2,figsize=(2*0.8*4,2*0.8*3))

data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/data_2.000000_111.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[0][0].hist(data, bins=linspace(0,100,1000), normed=True, facecolor="white")
m = linspace(0,10,1000)
ax[0][0].plot(m, pareto.pdf(m,3.5, loc=-1 ),'k--',label=ur"$a = 3.5$",linewidth=1.5)
ax[0][0].set_xlim(0,3)
ax[0][0].legend(fontsize=11)

data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/data_1.500000_351.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[0][1].hist(data, bins=linspace(0,100,800), normed=True, facecolor="white")
m = linspace(0,10,1000)
ax[0][1].plot(m, pareto.pdf(m,2.5,loc=-1 ),'k--',label=ur"$a = 2.5$",linewidth=1.5)
ax[0][1].set_xlim(0,4)
ax[0][1].legend(fontsize=11)

data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/data_1.000000_622.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[1][0].hist(data, bins=linspace(0,100,700), normed=True, facecolor="white")
m = linspace(0,10,1000)
ax[1][0].plot(m, pareto.pdf(m,2, loc=-1 ),'k--',label=ur"$a = 2$",linewidth=1.5)
ax[1][0].set_xlim(0,5)
ax[1][0].legend(fontsize=11)


data = loadtxt("/home/marius/Dokumenter/fys4150/batmobile/resources/data_0.500000_78.txt")
data = data.reshape( data.shape[0]*data.shape[1] )
ax[1][1].hist(data, bins=linspace(0,100,550), normed=True, facecolor="white")
m = linspace(0,10,1000)

ax[1][1].plot(m, pareto.pdf(m, 1.6,loc=-1 ),'k--',label=ur"$a = 1.6$",linewidth=1.5)
ax[1][1].set_xlim(0,6)
ax[1][1].legend(fontsize=11)

ax[0][0].set_ylabel(ur"$P(m)$")
ax[1][0].set_ylabel(ur"$P(m)$")

ax[1][0].set_xlabel(ur"$m$")
ax[1][1].set_xlabel(ur"$m$")

plt.savefig("../benchmark/fig5.png")
plt.savefig("../benchmark/fig5.pgf")
