# -*- coding: utf-8 -*-
from numpy import *

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
f, ax = plt.subplots(1,2,figsize=(2*0.8*4,1*0.8*3))
plt.gcf().subplots_adjust(bottom=0.15)

data = loadtxt("../resources/data_194.txt")
data = data.reshape(data.shape[0]*data.shape[1])
l = 1./mean(data)
p, bins, patches = ax[0].hist( data ,bins=arange(min(data), max(data) + 0.05, 0.2), normed=True, facecolor="white")
ax[0].plot(bins[:-1], l*exp(-l*bins[:-1]), "k--",linewidth = 1.5, label=ur"$\beta \exp(-\beta m)$, $\beta = %.2f$" % l)
ax[0].set_xlim(0,10)
ax[1].hist( data ,bins=linspace(0, 10, 45), normed=True,facecolor="white")
ax[1].set_yscale("log")
ax[0].set_ylabel("$P(m)$")
ax[0].set_xlabel("$m$")
ax[1].set_xlabel("$m$")
ax[0].legend(fontsize=11)
ax[0].set_title(ur"Empirical distrb. ($\alpha$-model)", fontsize=11)
ax[1].set_title(ur"log-transformed distrbution", fontsize=11)
ax[1].set_xlim(0,10)
plt.savefig("../benchmark/fig3.png")
plt.savefig("../benchmark/fig3.pgf")




