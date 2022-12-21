import numpy as np
import os
from scipy.optimize import minimize
import itertools
import collections
import matplotlib.pylab as plt

dir="/media/tama3rdgen/6TB/water-SP/"
subDir="S10_N2/"

# From simulation
no=1000
LH=253.67852117
L=LH*2
times=np.arange(0,9000,10)
# For postprocessing
rcut=5
rcut2=rcut*rcut
output=np.zeros((10,np.size(times)))
output[0]=times
Nmax=40
dists=np.zeros((Nmax,np.size(times)))
N=np.zeros(0)
loop=0

def periodic(dx):
    if(dx<-LH):
        dx+=L
    if(dx>LH):
        dx-=L

for it in times:
    row0=9*(it+1)+no*3*it
    data=np.loadtxt(dir+subDir+"a.dump", max_rows=no*3, skiprows=row0)
    Oatom=np.where(data.T[1]==1)
    data=data[Oatom]
    clusterID=np.arange(no)
    for i in np.arange(no-1):
        for j in np.arange(i+1,no):
            dr=data[i][3:6]-data[j][3:6]
            dy=data[i][4]-data[j][4]
            dz=data[i][5]-data[j][5]
            periodic(dr[0]),periodic(dr[1]),periodic(dr[2])
            dr2=dr*dr
            if(np.sum(dr2)<rcut2):
                clusterID[j]=clusterID[i]
    cluster=[]
    for i in np.unique(clusterID):
        loc=np.arange(no)[np.where(clusterID==i)]
        cluster.append(loc)
    n=[len(v) for v in cluster]
    for i in n:
        if(i>Nmax):
            i=Nmax-1
        dists[i][loop]+=1
    output[1][loop]=np.size(np.unique(clusterID))
    output[2][loop]=sum(x>5 for x in n)
    output[3][loop]=sum(x>10 for x in n)
    output[4][loop]=sum(x>15 for x in n)
    output[5][loop]=sum(x>20 for x in n)
    output[6][loop]=sum(x>25 for x in n)
    output[7][loop]=sum(x>30 for x in n)
    output[8][loop]=sum(x>35 for x in n)
    output[9][loop]=sum(x>40 for x in n)
    loop+=1
#np.savetxt("S10_N2.dat",)
np.savetxt("S10_N2.dat",output.T)
