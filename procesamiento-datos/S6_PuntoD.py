
'''
Serie 6 - Punto D (script). Marcos Tracchia
'''

import numpy as np
import matplotlib.pylab as plb
import sys

'''
IMPORTANTE: Para compilar este script escribir en una terminal 
"python3 S6_PuntoD.py <valores de a>". Por ejemplo "python3 S6_PuntoD.py 1 2 3 0.5". 
No importa la cantidad de valores de "a" que se ingresen. En cuanto al comando 
está referido solo para cualquier distro de LINUX. Desconozco si funciona en Windows.
Usar Python 3.
'''

#Ingreso por consola los valores de "a"
a_s = np.array(sys.argv[1:], dtype=np.float64)
print("Valores ingresados: {}".format(a_s))

#Defino la longitud de los intervalos y la cantidad de valores de "k" y "x"
N=10000
k = np.linspace(-4, 4, N) 
x = np.linspace(-4, 4, N)

#Ubico los gráficos en el 0 del sistema de coordenadas
k0 = 0

#Gráficos:
for a in a_s:

	#-X-
	plb.subplot(121)
	exponente = -((np.sqrt(2)*x/a)**2)
	A = 2 / (a*(np.sqrt(2*np.pi)))
	PSI_modcdr = A*np.exp(exponente)
	plb.xlabel("$x$",fontweight='bold',size=20)
	plb.ylabel("$|\psi(x,0)|^{2}$",fontweight='bold',size=20)
	plb.plot(x,PSI_modcdr,lw=3)
	#Para la cuadrícula
	plb.grid(b=True, which='major', color='k', linestyle='-')
	plb.minorticks_on()
	plb.grid(b=True, which='minor', color='k', linestyle=':', alpha=1)
	#Para la leyenda
	plb.legend([r"$a=%.2f$" %(i) for i in a_s], loc = "upper right")
	

	#-K-
	plb.subplot(122)
	exponente = ((-(a**2)/2))*((k-k0)**2)
	A = a / (np.sqrt(2*np.pi))
	PHI_modcdr = A*(np.exp(exponente))
	plb.xlabel("$k$",fontweight='bold',size=20)
	plb.ylabel("$|\phi(k)|^{2}$",fontweight='bold',size=20)
	plb.plot(k,PHI_modcdr,lw=3)
	#Para la cuadrícula
	plb.grid(b=True, which='major', color='k', linestyle='-')
	plb.minorticks_on()
	plb.grid(b=True, which='minor', color='k', linestyle=':', alpha=1)
	#Para la leyenda
	plb.legend([r"$a=%.2f$" %(i) for i in a_s], loc = "upper right")

plb.show()




