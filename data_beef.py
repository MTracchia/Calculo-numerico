
import os
import PIL.Image
from PIL.ExifTags import TAGS

with open("data_beef.csv","w") as data_beef:

	#Escribo el header
	data_beef.write("filename,izq/der,EV,color carne,color grasa,marmolado")
	data_beef.write("\n")

	#Recorro sobre los subdirectorios del directorio "bifes"
	for folder in sorted(os.listdir("bifes")): #Ojo! mucho cuidado con los nombres de los subdirectorios
		path = os.path.join("bifes",folder)
		for img in sorted(os.listdir(path)): #Recorro sobre los archivos de los subdirectorios
			file_name_png = os.path.splitext(img)[0]
			img = PIL.Image.open(os.path.join(path,img))
			exif_data = img.getexif() #Extraigo metadata
			EV = exif_data[33434] #33434 es la clave del diccionario cuyo valor es el EV
			EV = str(EV[0])+"/"+(str(EV[1])) #Al ser EV una tupla, convierto sus dos valores en un solo string. Sin esto hay problemas en el .csv
			data_beef.write("{}, ,{}".format(file_name_png,EV))
			data_beef.write("\n")

#ESTO ES PARA TAGEAR LA METADATA (sobre una sola imagen-ver el path)
'''
img = PIL.Image.open("bifes/SmartBeef Carga día 1 20200825/DSC00101.JPG")
exif_data = img.getexif()
#print(exif_data)
for tag_id in exif_data:
	tag=TAGS.get(tag_id,tag_id)
	data=exif_data.get(tag_id)
	if isinstance(data, bytes):
		data = data.decode()
	print(f"{tag:25}: {data}")
'''

