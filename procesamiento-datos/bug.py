
import csv

count = 0
elements_row = []
elements_per_row = []
list_of_rows = []

with open("reportes.csv","r") as reports:
	reader = csv.reader(reports) #reader (objeto iterable) me permite tener acceso a las filas del csv.	
	#con row me itero sobre las filas del csv
	for row in reader:
		#itero sobre los elementos de cada fila
		for ele_row in row:
			elements_row.append(ele_row)


with open("csvNew.csv","w") as file:
	file_w = csv.writer(file)
	#Para meter una lista dentro de otra lista
	#cada 19 elementos, meto "elements_per_row" en "list_of_rows", reinicio "elements_per_row" y el contador
	for ele in elements_row:
		count+=1
		elements_per_row.append(ele)
		if count == 19:
			list_of_rows.append(elements_per_row)
			elements_per_row = []
			count = 0

	#Escribo sobre el .csv creado
	for id in list_of_rows:
		file_w.writerow(id)

#print(ord("\n"))--es el 10/chr
