"""
GRUPO 11
Objetivo: calibración píxel/centímetro para los patrones de difracción.
"""
import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy import ndimage

#Defino variables y parámetros
x_i=830
x_f=1255
y_i=1590
y_f=1650
rows=y_f-y_i
count = 1
minimum_sum = 0

#Proceso imagen
img_rgb = imageio.imread("papela.jpg")
img_rgb_rotated = ndimage.rotate(img_rgb, 3.6) #Roto imagen sentido antihorario
img_rgb_rotated_segment=img_rgb_rotated[y_i:y_f,x_i:x_f]
img_rgb_rotated_segment_green = img_rgb_rotated_segment[:,:,0]

#Proceso matrices
sum=np.sum(img_rgb_rotated_segment_green,axis=0) 
average_map = map(lambda x: x/rows, sum) 
average_list = list(average_map) 
plt.plot(average_list,"r")
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
