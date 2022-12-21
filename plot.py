import numpy as np
import matplotlib.pylab as plt


def pltNormal():
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['figure.subplot.bottom'] = 0.2
    plt.rcParams['figure.subplot.left'] = 0.2
    #plt.rcParams['font.family'] = 'Arial'
    plt.rcParams["font.size"]=10

def axNormal(ax):
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')


pltNormal()

'''
fig, axs = plt.subplots(3,3,figsize=(10,10),sharey=True,sharex=True)
for i in axs.flat:
    axNormal(i)

index=["a","b","c","d","e","f","g","h","i"]
for i in np.arange(9):
    data=np.loadtxt("dists_low.dat")
    axs.flat[i].bar(np.arange(40),data.T[i],color="black",alpha=0.5)
    axs.flat[i].set_yscale("log")
    axs.flat[i].set_title("("+index[i]+") "+str(int(i*10))+" ns",loc="left",size=18)

plt.yscale("log")
#plt.savefig("dist_low.png", dpi=1000)
#plt.show()

##############################################################################

fig, axs = plt.subplots(3,3,figsize=(10,10),sharey=True,sharex=True)
for i in axs.flat:
    axNormal(i)

index=["a","b","c","d","e","f","g","h","i"]
for i in np.arange(9):
    data=np.loadtxt("dists.dat")
    axs.flat[i].bar(np.arange(40),data.T[i],color="black",alpha=0.5)
    axs.flat[i].set_yscale("log")
    axs.flat[i].set_title("("+index[i]+") "+str(int(i*10))+" ns",loc="left",size=18)

plt.yscale("log")
#plt.savefig("dist.png", dpi=1000)
#plt.show()

##############################################################################

fig, axs = plt.subplots(1,1,figsize=(5,5))
axNormal(axs)
cm = plt.get_cmap("gnuplot")
data=np.loadtxt("S10_N2_low.dat")
axs.plot(data.T[0]*0.001,data.T[2],c=cm(0.1))
axs.plot(data.T[0]*0.001,data.T[5],c=cm(0.5))
axs.plot(data.T[0]*0.001,data.T[3],c=cm(0.3))
axs.plot(data.T[0]*0.001,data.T[7],c=cm(0.7))
axs.plot(data.T[0]*0.001,data.T[9],c=cm(0.9))
axs.set_yscale("log")

plt.savefig("S10_N2_low.png", dpi=1000)
plt.show()


##############################################################################

fig, axs = plt.subplots(1,1,figsize=(5,5))
axNormal(axs)
cm = plt.get_cmap("gnuplot")
data=np.loadtxt("S10_N2.dat")
axs.plot(data.T[0]*0.001,data.T[2],c=cm(0.1))
axs.plot(data.T[0]*0.001,data.T[5],c=cm(0.5))
axs.plot(data.T[0]*0.001,data.T[3],c=cm(0.3))
axs.plot(data.T[0]*0.001,data.T[7],c=cm(0.7))
axs.plot(data.T[0]*0.001,data.T[9],c=cm(0.9))
axs.set_yscale("log")

plt.savefig("S10_N2.png", dpi=1000)
plt.show()
'''
##############################################################################

fig, axs = plt.subplots(1,1,figsize=(5,5))
axNormal(axs)
ax2 = axs.twinx()
V=50e-9**3
kb=1.38e-23
T=300
data=np.loadtxt("S10_N2.dat")
p=(data.T[1])/V*kb*T
ps=3170
S=p/ps
axs.plot(data.T[0]*0.001,S,c="black")
#axs.plot(data.T[0]*0.001,S*0+10/np.max(S),c="black",linestyle="--",linewidth=0.5)
#axs.plot(data.T[0]*0.001,S*0+8.5/np.max(S),c="black",linestyle="--",linewidth=0.5)

T=275
data=np.loadtxt("S10_N2_low.dat")
p=(data.T[1])/V*kb*T
ps=960
S=p/ps
ax2.plot(data.T[0]*0.001,S,c="red")
ax2.tick_params(axis='y', colors='red')
#axs.plot(data.T[0]*0.001,S*0+30/np.max(S),c="red",linestyle="--",linewidth=0.5)
#axs.plot(data.T[0]*0.001,S*0+21/np.max(S),c="red",linestyle="--",linewidth=0.5)
axs.set_ylabel("Saturation ratio (300 K) [-]",size=15)
ax2.set_ylabel("Saturation ratio (275 K) [-]",color="red",size=15)
axs.set_xlabel("Time [ns]",size=15)
plt.savefig("S.png", dpi=1000)
plt.show()
