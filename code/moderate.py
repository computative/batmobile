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
mpl.rcParams['axes.color_cycle'] = ['k', 'k','k', 'k', 'k', 'k', 'k', 'k', 'k', 'k' ]

import matplotlib.pyplot as plt
f, ax = plt.subplots(2,2,figsize=(2*0.8*4,2*0.8*3))
plt.gcf().subplots_adjust(bottom=0.15)

nums = ["0.500000_78","1.000000_622","1.500000_351","2.000000_111"]
A = [.5,1,1.5,2.]
styles = [[1000],[2,2],[4,4],[8, 4, 2, 4, 2, 4]]
for n, a, style in zip(nums,A,styles):
    data = loadtxt("../resources/data_" + str(n)  + ".txt")
    data = data.reshape( data.shape[0]*data.shape[1] )
    pmd, bins = histogram(data, density=True, bins=logspace(-3,3,500))
    ax[0][0].plot(bins[:-1], pmd, label=ur"$\alpha="+str(a)+"$", dashes=style)
ax[0][0].set_xlim(0.001,1000)
ax[0][0].set_ylim(1e-6,10)
ax[0][0].set_yscale("log");
ax[0][0].set_xscale("log")
ax[0][0].legend(fontsize=11,loc=3)
ax[0][0].set_ylabel(ur"$P(m)$")
ax[0][0].set_title(ur"$P(m)$, $\gamma$-model ($N$=1024)",fontsize=11)

nums = ["0.500000_187","1.000000_430","1.500000_147","2.000000_107"]
A = [.5,1,1.5,2.]
styles = [[1000],[2,2],[4,4],[8, 4, 2, 4, 2, 4]]
for n, a, style in zip(nums,A,styles):
    data = loadtxt("../resources/data_" + str(n)  + ".txt")
    data = data.reshape( data.shape[0]*data.shape[1] )
    pmd, bins = histogram(data, density=True, bins=logspace(-3,3,500))
    ax[0][1].plot(bins[:-1], pmd, label=ur"$\alpha="+str(a)+"$", dashes=style)
ax[0][1].set_xlim(0.001,1000)
ax[0][1].set_ylim(1e-6,10)
ax[0][1].set_yscale("log");
ax[0][1].set_xscale("log")
ax[0][1].set_title(ur"$P(m)$, $\gamma$-model ($N$=512)",fontsize=11)

# new row

nums = ["datal0.500000a0.500000n1024", "datal0.500000a1.000000n1024", "datal0.500000a1.500000n1024","datal0.500000a2.000000n1024"]
A = [.5,1,1.5,2.]
styles = [[1000],[2,2],[4,4],[8, 4, 2, 4, 2, 4]]
for n, a, style in zip(nums,A,styles):
    data = loadtxt("../resources/" + str(n)  + ".txt")
    data = data.reshape( data.shape[0]*data.shape[1] )
    pmd, bins = histogram(data, density=True, bins=logspace(-3,3,500))
    ax[1][0].plot(bins[:-1], pmd, label=ur"$\alpha="+str(a)+"$", dashes=style)
ax[1][0].set_xlim(0.001,1000)
ax[1][0].set_ylim(1e-4,10)
ax[1][0].set_yscale("log");
ax[1][0].set_xscale("log")
ax[1][0].set_xlabel(ur"$m$")
ax[1][0].set_ylabel(ur"$P(m)$")

nums = ["datal0.500000a0.500000n512","datal0.500000a1.000000n512","datal0.500000a1.500000n512","datal0.500000a2.000000n512"]
A = [.5,1,1.5,2.]
styles = [[1000],[2,2],[4,4],[8, 4, 2, 4, 2, 4]]
for n, a, style in zip(nums,A,styles):
    data = loadtxt("../resources/" + str(n)  + ".txt")
    data = data.reshape( data.shape[0]*data.shape[1] )
    pmd, bins = histogram(data, density=True, bins=logspace(-3,3,500))
    ax[1][1].plot(bins[:-1], pmd, label=ur"$\alpha="+str(a)+"$", dashes=style)
ax[1][1].set_xlim(0.001,1000)
ax[1][1].set_ylim(1e-4,10)
ax[1][1].set_yscale("log");
ax[1][1].set_xscale("log")
ax[1][1].set_xlabel(ur"$m$")

plt.savefig("../benchmark/fig1.png")
plt.savefig("../benchmark/fig1.pgf")
