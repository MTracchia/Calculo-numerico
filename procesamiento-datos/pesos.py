#Para asiganarle los correspondientes pesos a las imágenes de cattlerscanner y separar 
#aquellas que no los tienen
import os
import cv2

#Variables y listas
timestamp = []
weights = []
font = cv2.FONT_HERSHEY_SIMPLEX

#Rutas
path = "device60003"

#Directorios
os.mkdir("vacas_con_pesos") #Ojo! con incluir dentro del for. El directorio se tiene que generar una vez.
os.mkdir("vacas_sin_pesos")

for file in os.listdir(path): #Empieza agarrando los archivos en otro orden / investigar cómo itera listdir
	if file.endswith(".csv") == True:
		with open("csv/"+str(file))	as file_csv:
		for linea in file_csv:
			columna = linea.split(",")
			timestamp.append(columna[0])
			weights.append(columna[1])
	else:
		pass

datos = dict(zip(timestamp,weights))

for file in os.listdir(path):
	if file.endswith(".png") == True:
		file_name = os.path.splitext(file)[0]
		img = cv2.imread(path+str(file))
		if (file_name in datos) == True:
			cv2.putText(img,datos[file_name]+' Kg',(10,50), font, 1,(0,0,0),2)
			cv2.imwrite("vacas_con_pesos/" + str(file),img)
		else:
			if (file_name in datos) == False:
				cv2.imwrite("vacas_sin_pesos/" + str(file),img)
	else:
		pass

