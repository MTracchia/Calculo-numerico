#Para asiganarle los correspondientes pesos a las imágenes de cattlerscanner
import os
import cv2

timestamp = []
weights = []

file1 = open("report_20200701-131430.csv","r")
file2 = open("report_20200703-101254.csv","r")

#Paso los datos de timestamp y weight a dos listas para poder manejarlos aparte
for linea1 in file1:
	columna1 = linea1.split(",")
	timestamp.append(columna1[0])
	weights.append(columna1[1])

for linea2 in file2:
	columna2 = linea2.split(",")
	timestamp.append(columna2[0])
	weights.append(columna2[1])

#Elimino los headers "weight" y "timestamp"
weights.remove(' weight')
weights.remove(' weight')
timestamp.remove('timestamp')
timestamp.remove('timestamp')

#Junto los datos y los diccionarizo
datos = dict(zip(timestamp,weights))

#Edito imágenes
font = cv2.FONT_HERSHEY_SIMPLEX
for file in os.listdir("imagenes/cattlescanner_data"):
	file_name = os.path.splitext(file)[0]
	img = cv2.imread("imagenes/cattlescanner_data/"+str(file))
	if (file_name in datos) == True:
		cv2.putText(img,datos[file_name]+' Kg',(10,50), font, 1,(0,0,0),2)
		cv2.imwrite("imagenes/vacas_con_pesos/" + str(file),img)
	else:
		if (file_name in datos) == False:
			cv2.imwrite("imagenes/vacas_sin_pesos/" + str(file),img)

'''
el hamiltoniano es un observable
'''
file1.close()
file2.close()