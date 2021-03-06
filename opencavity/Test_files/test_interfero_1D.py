# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 15:56:29 2014

@author: Mohamed
"""
from opencavity.beams import HgBasis
from opencavity.propagators import FresnelProp
import numpy as np
import matplotlib.pylab as plt


H=HgBasis(1,3,3) #creating the Hermite-Gauss basis with initial waist equals to 100 microns
z=0.000000000000000001
W_lc=H.Wx(z) #we simply measure the waist of the beam to adapt the plot window
print W_lc
x=np.linspace(-50*W_lc, 50*W_lc,400); y=x
tem00=H.generate_hg(0,0, x,0, z) # the TEM00 gaussian beam for y=0 so no y component and for z=0 so at the waist.
tem00=H.generate_hg(0,0, x-30,0, z)+H.generate_hg(0,0, x+30,0, z)
#tem00=np.zeros(400);
#tem00[150:250]=1; 
#tem00[180:181]=1; #tem00[220:221]=1;

plt.Figure()
plt.plot(x,np.abs(tem00),'r')



# create an ABCD matrix to propagate the beam 
L1=20*1e3;# mm
f=-20*1e3; #mm converging lens FL
#R=-0.2*1e3; dn=0.5;  #n2-n1=1.5-1
#f=R/(2*dn); 

L2=10e3;# mm
#  definition of the ABCD matrices     
M1=np.array([[1, L1],[0, 1]]); M2=np.array([[1, 0],[-1/f, 1]]); M3=np.array([[1, L2],[0, 1]])
#M=M3.dot(M2).dot(M1) # calculating the global matrix 
#M=M3.dot(M1)


opSys=FresnelProp()

T_lens=np.exp((1j*opSys.k/(2*f))*(x-0)**2);
opSys.set_start_beam(tem00, x)
opSys.set_ABCD(M1)
#opSys.apply_mask1D(T_lens)
opSys.propagate1D_ABCD(x2=3*x)
opSys.show_result_beam(what='intensity')
opSys.show_result_beam(what='phase')

opSys.yz_prop_chart(5e3,L1,100,3*x)
opSys.show_prop_yz()
opSys.show_prop_yz(what='intensity')
plt.show()