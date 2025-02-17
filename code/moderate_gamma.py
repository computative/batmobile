# -*- coding: utf-8 -*-
from os import popen

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
f, ax = plt.subplots(4,2,figsize=(2*0.8*4,3.8*0.8*3))


A = [1,2]
Gamma = [0,1,2,3,4]
Style = [[1000],[1,1],[2,2],[4,4],[8, 4, 2, 4, 2, 4]]
for k in arange(4):
    for i in range(len(A)):
        for j in range(len(Gamma)):
            data = loadtxt("../resources/Data" + str(int(1 + floor(k/2.))) + "_g%f_a%f.txt" % (Gamma[j], A[i]))
            data = data.reshape( data.shape[0]*data.shape[1] )
            pmd, bins = histogram(data, density=True, bins=logspace(-3,3,500))
            ax[k][i].plot(bins[:-1], pmd, label=ur"$\gamma="+str(Gamma[j])+"$", dashes=Style[j])
        ax[k][i].set_yscale("log")
        ax[k][i].set_xscale("log")
        ax[k][0].set_ylabel(ur"$P(m)$")
        ax[0][i].set_xlim(0.001,1000)
        ax[0][i].set_ylim(1e-6,7)
        ax[1][i].set_xlim(1,10)
        ax[1][i].set_ylim(1e-3,1)
        ax[2][i].set_xlim(0.001,1000)
        ax[2][i].set_ylim(1e-6,10)
        ax[3][i].set_xlim(1,10)
        ax[3][i].set_ylim(1e-2,10)
ax[0][0].set_title(ur"$P(m)$, $\delta$-model, $\alpha=1$",fontsize=11)
ax[0][1].set_title(ur"$P(m)$, $\delta$-model, $\alpha=2$",fontsize=11)
ax[3][0].set_xlabel(ur"$m$")
ax[3][1].set_xlabel(ur"$m$")
ax[0][0].legend(fontsize=11,loc=3)

plt.savefig("../benchmark/fig2.png")
plt.savefig("../benchmark/fig2.pgf")
