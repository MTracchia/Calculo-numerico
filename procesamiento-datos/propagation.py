from uncertainties import ufloat
from uncertainties.umath import *  # Imports sin(), etc.
import numpy as np
import math


'''
L=ufloat(0.255,0.002)
d=ufloat(0.0046,0.0002)
den=8730
w=ufloat(203.07,0.44)
#w=ufloat(203.07,0.44)

I=np.pi*(pow(d,4))/64.0
K1=1.875104/L
K2=4.694091/L
den_lineal=den*(np.pi*((d/2.0)**2))


print(den_lineal)
print(w**2)
print(I)
print(K2)
print(np.sqrt(K2))

E=((w**2)*den_lineal)/(I*(pow(K1,4)))

print(E) #imprime el error
#print(repr(<medicion indirecta>)) #imprime el error con mucha mas precision
'''
Lfit=607.9103214173336  
Lerr=2.379221058926942

Cfit=1.662007865933048e-14  
Cerr=6.504649452987045e-17

Rfit=5968.82040679501  
Rerr=60.87552048827508

C2fit= 2.2237270775855564e-12  
C2err=1.165489714175789e-13



L=ufloat(Lfit, Lerr)
C=ufloat(Cfit, Cerr)
R=ufloat(Rfit, Rerr)
C2=ufloat(C2fit, C2err)

ws=1/sqrt(L*C)

Q= ws*L/(10000+R)

wp=sqrt(((1/C)+(1/C2))*1/L)


print(f"ws: {repr(ws)}\n")
print(f"Q: {repr(Q)}\n")
print(f"wp: {repr(wp)}\n")