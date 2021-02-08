
"""
GRUPO 11
Objetivo: procesamiento de imágenes con patrones de difracción y adquisición de los mínimos
correspondientes a las interfranjas.
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy import ndimage
import cv2

#Defino variables y parámetros
x_i=1315
x_f=1385
y_i=1700
y_f=2000
range_graphic_x=100
range_graphic_y=100
columns=x_f-x_i
count = 1
minimum_sum = 0


#Proceso imagen
img_rgb = imageio.imread("a4.jpg")
img_rgb_rotated = ndimage.rotate(img_rgb, 2.5) #Roto imagen sentido antihorario
#Proceso matrices
img_frame = img_rgb_rotated[:,:,0]
matrix = img_frame[y_i:y_f,x_i:x_f] #tomo matriz de perfiles
sum=np.sum(matrix,axis=1) #sumo elementos de cada fila de la matriz de perfiles
average_map = map(lambda x: x/columns, sum) #calculo el promedio de cada fila sumada
average_list = list(average_map) #average_map es un map objetc, no podría graficarlo si no lo listeo

#Proceso gráficos
plt.subplot(121)
plt.imshow(cv2.rectangle(img_rgb_rotated,(x_i,y_i),(x_f,y_f),(255,255,255),2))
plt.title("Patrón de difracción-original")
plt.xlim(x_i-range_graphic_x,x_f+range_graphic_y)
plt.ylim(y_i-range_graphic_x,y_f+range_graphic_y)
#Referencia para la rotacion de la imagen
#plt.axvline(x=1334,color="red")
plt.subplot(122)
plt.plot(average_list,"b")
plt.title("Patrón de difracción")
plt.xlabel("Posición (px)")
plt.ylabel("Intensidad (promedio en píxeles)")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='k', linestyle=':', alpha=1)

#Para la adquisición de datos
while True:
	x = plt.ginput(2,0)
	minimum_dist= abs( (x[0])[0]-(x[1])[0] )
	minimum_sum+=minimum_dist
	print("coordenada-mínimos:Z(1):{:.2f}, Z(2):{:.2f} - distancia:{:.2f}".format((x [0])[0],(x[1])[0],minimum_dist))
	print("promedio total:{:.2f}".format(minimum_sum/count))
	count+=1

plt.show()
