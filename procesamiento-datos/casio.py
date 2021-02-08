# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:19:34 2020

@author: corir
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

datos_12 = np.genfromtxt('prueba_cas_2.csv', delimiter=',')

F1=datos_12[:,0]
T1=datos_12[:,2]
T1err=datos_12[:,3]
Theta1=datos_12[:,4]
Theta1err=datos_12[:,5]

#def resonancia (w, R, R2, L, C):
#    a=R2/(np.sqrt(((R+R2)**2)+((L**2*(w-(1.0/(w*C*L)))**2))))
#    return(a)

#aca buscamos R, L y C, dejando fijo R2 porque sino da errores horribles
#el scipt donde sacamos el valor estimado de R, L y C es otro

R2=10000
def resonancia (w,R, L, C):
    a=R2/(np.sqrt(((R+R2)**2)+((L**2*(w-(1.0/(w*C*L)))**2))))
    return(a)    
    
R_i = 6000
R2_i = 10000
L_i=619.68
#L_i=750
#C_i=1.0120999999999999e-11/L_i
C_i=1.6304556865338472e-14
t = np.linspace(300158,316102, num = 10000)

#ajuste = resonancia (t, R_i, R2_i)#, Lfit, Cfit)
#ajuste = resonancia (2*3.14*F1, R_i, R2_i, L_i, C_i)

#plt.clf()
#plt.plot(2*3.14*F1, ajuste, '-', label = 'Ajuste con L y C')
plt.legend(loc='upper right')

#%% da bien la forma de la curva ahora vemos si se pega mas o menos a los datos
plt.errorbar(F1*2*3.14,T1,yerr=T1err,fmt=".-", ecolor='r', color='mediumblue', elinewidth=1.5, label = '0,1 V')


#%% este es el ajuste en R2, que da feo
initguess = np.array([R_i, R2_i, L_i, C_i])

#indices=np.nonzero(T1err<1e-5)
#T1err[indices]=1e-5

popt, pcov = curve_fit(resonancia, 2*3.14*F1, T1, p0= initguess, maxfev= 10000)
perr = np.sqrt(np.diag(pcov))


Rfit = popt[0]
R2fit= popt[1]
Lfit = popt[2]
Cfit= popt[3]

Rerr= perr[0]
R2err = perr[1]
Lerr= perr[2]
Cerr = perr[3]

t = np.linspace(314158,315102, num = 10000)
ajuste_posta = resonancia (t, Rfit, R2fit, Lfit, Cfit)


plt.plot(t, ajuste_posta, 'r-', label = 'Ajuste posta con L y C')
plt.legend(loc='upper right')

#%% ajuste sin R2, de aca sacamos los valores de L R y C que vamos a usar, y su error
initguess = np.array([R_i, L_i, C_i])

#indices=np.nonzero(T1err<1e-5)
#T1err[indices]=1e-5

popt, pcov = curve_fit(resonancia, 2*3.14*F1, T1, p0= initguess, maxfev= 10000)
perr = np.sqrt(np.diag(pcov))

Rfit = popt[0]
Lfit = popt[1]
Cfit= popt[2]

Rerr= perr[0]
Lerr= perr[1]
Cerr = perr[2]

t = np.linspace(314158,315102, num = 10000)
ajuste_posta = resonancia (t,Rfit, Lfit, Cfit)


plt.plot(t, ajuste_posta, 'r-', label = 'Ajuste posta con L y C')
plt.legend(loc='upper right')

print(Rfit, Rerr, Lfit, Lerr, Cfit, Cerr)

#%% Ahora agregamos al modelo c2
#datos_13 = np.genfromtxt('prueba_cas_3.csv', delimiter=',') #ya no es necesario, pero lo dejo por las dudas
datos = np.loadtxt('prubeba2y3.txt',   delimiter=',') #este txt tiene la curva de resonancia y antiresonancia

F2=datos[:,0]
T2=datos[:,2]
T2err=datos[:,3]
Theta2=datos[:,4]
Theta2err=datos[:,5]

plt.errorbar(F2*2*3.14,T2,yerr=T2err,fmt="-", ecolor='r', color='green', elinewidth=1.5, label = '0,1 V')

wp=315785.5
C2_ii=1/(Lfit*wp**2 -1/Cfit)
print(C2_ii)

R2=10000
#este es con las 4 libres
#def resonancia2 (w,R, L, C, C2):
#    a= w*L - 1/(w*C)
#    b=R**2 + a**2
#    c=(w*C2*R)**2 + (1 - w*C2*a)**2
#    d=np.sqrt(b/c)
#    z=R2/(d+R2)
#    return(z)
#x = np.linspace(314158,316520, num = 15000) 
#buscando_C2i=resonancia2(x,Rfit,Lfit,Cfit,C2_ii)   
#plt.plot(x, buscando_C2i, '-', label='Buscando C2_i') #C2_ii ya da re bien
#plt.grid(True)
#plt.ylabel('Transferencia ')
#plt.xlabel('Frecuencia (Hz)')
#plt.legend(loc='upper right')
#plt.yscale('log')
#plt.show()

#este es fijando R
#R=Rfit
#def resonancia2 (w, L, C, C2):
#    a= w*L - 1/(w*C)
#    b=R**2 + a**2
#    c=(w*C2*R)**2 + (1 - w*C2*a)**2
#    d=np.sqrt(b/c)
#    z=R2/(d+R2)
#    return(z)
#x = np.linspace(314158,316520, num = 15000) 
#buscando_C2i=resonancia2(x,Lfit,Cfit,C2_ii)   
#plt.plot(x, buscando_C2i, '-', label='Buscando C2_i') #C2_ii ya da re bien
#plt.grid(True)
#plt.ylabel('Transferencia ')
#plt.xlabel('Frecuencia (Hz)')
#plt.legend(loc='upper right')
#plt.yscale('log')
#plt.show()

#este es dejando solo C2 libre
R=Rfit
L=Lfit
C=Cfit
def resonancia2 (w, C2):
    a= w*L - 1/(w*C)
    b=R**2 + a**2
    c=(w*C2*R)**2 + (1 - w*C2*a)**2
    d=np.sqrt(b/c)
    z=R2/(d+R2)
    return(z)
x = np.linspace(314158,316520, num = 15000) 
buscando_C2i=resonancia2(x, C2_ii)   
plt.plot(x, buscando_C2i, '-', label='Buscando C2_i') #C2_ii ya da re bien
plt.grid(True)
plt.ylabel('Transferencia ')
plt.xlabel('Frecuencia (Hz)')
plt.legend(loc='upper right')
plt.yscale('log')
plt.show()
#%% ajuste con las 4 libres
initguess1 = np.array([Rfit, Lfit, Cfit,C2_ii])

#indices=np.nonzero(T2err<10)
#T2err[indices]=1e-7
#Falsoerr=[]


popt, pcov = curve_fit(resonancia2, 2*3.14*(F2), (T2), p0= initguess1, sigma= T2err,maxfev= 10000)
perr = np.sqrt(np.diag(pcov))

Rfit1 = popt[0]
Lfit1 = popt[1]
Cfit1= popt[2]
C2fit= popt[3]

Rerr1= perr[0]
Lerr1= perr[1]
Cerr1 = perr[2]
C2err = perr[3]

t = np.linspace(314158,316520, num = 10000)
ajuste_conC2 = resonancia2 (t,Rfit1, Lfit1, Cfit1, C2fit)


plt.plot(t, ajuste_conC2, '-o', label = 'Ajuste posta con C2')
plt.legend(loc='upper right')

print(Rfit1, Rerr1, Lfit1, Lerr1, Cfit1, Cerr1, C2fit, C2err)

#%%ajuste sin R

initguess1 = np.array([Lfit, Cfit,C2_ii])

#indices=np.nonzero(T1err<1e-5)
#T1err[indices]=1e-5

popt, pcov = curve_fit(resonancia2, 2*3.14*(F2), (T2), p0= initguess1, maxfev= 10000)
perr = np.sqrt(np.diag(pcov))

#Rfit1 = popt[0]
Lfit1 = popt[0]
Cfit1= popt[1]
C2fit= popt[2]

#Rerr1= perr[0]
Lerr1= perr[0]
Cerr1 = perr[1]
C2err = perr[2]

t = np.linspace(314158,316520, num = 10000)
ajuste_conC2 = resonancia2 (t, Lfit1, Cfit1, C2fit)


plt.plot(t, ajuste_conC2, '-o', label = 'Ajuste posta con C2')
plt.legend(loc='upper right')

print( Lfit1, Lerr1, Cfit1, Cerr1, C2fit, C2err)

#%%ajuste solo con C2
initguess1 = np.array([C2_ii])

#indices=np.nonzero(T1err<1e-5)
#T1err[indices]=1e-5
#el error no se lo puse, porque grafica feo

popt, pcov = curve_fit(resonancia2, 2*3.14*(F2), (T2), p0= initguess1, maxfev= 10000)
perr = np.sqrt(np.diag(pcov))


C2fit= popt[0]


C2err = perr[0]

t = np.linspace(314158,316520, num = 10000)
ajuste_conC2 = resonancia2 (t, C2fit)


plt.plot(t, ajuste_conC2, '-', label = 'Ajuste posta con C2')
plt.legend(loc='upper right')

print(C2fit, C2err)