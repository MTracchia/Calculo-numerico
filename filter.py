
#Filtro para los frames de cattlesacanner
count_cows = 0
count_frames = 0
lista = []

header = "file, timestamp, frame, cow_id, weight, QArea,QHeight-100,QHeight-50,QHeight-80,QHeight-90,QHeightSect-0-25,QHeightSect-25-75,QHeightSect-75-100,QLength,QVolume,QWidth-100,QWidth-50,QWidth-80,QWidth-90,QWidthSect-0-25,QWidthSect-25-75,QWidthSect-75-100\n"
	
file = open("report_20201120-113629.csv","r")
file_aux = open("frames_filtrados.csv","w")

for linea in file:

	if linea == header:
		pass
	else:	
		columna=linea.split(",")
		if(int(columna[3]) != count_cows):
			
			file_aux.write("{}".format(lista[count_frames]))
			#print(lista[int(count_frames)])
			count_cows+=1
			count_frames=0
			lista=[]
		if(int(columna[2]) == count_frames):
			lista.append(linea)
		else:
			file_aux.write("{}".format(lista[count_frames]))
			#print(lista[count_frames])
			lista = []
			lista.append(linea)
			count_frames += 1	

file_aux.write("{}".format(lista[int(columna[2])]))
#print(lista[int(columna[2])])

file_aux.close()
file.close()