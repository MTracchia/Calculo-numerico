
from datetime import datetime
import datetime as dt




count=1
aux=True
lineas = []
rfids = []
with open("rfid_completo.log","r") as log:

	for linea in log:
		
		if ((count%2) == 1 and (aux==False)):
		
			columna=linea.split(" ")
			fecha=(columna[0].split("["))[1]
			hora=(columna[1].split("."))[0]
			rfid = columna[2]	
			
			timestamp=fecha+" "+hora
			format_date = datetime.strptime(timestamp,"%d/%m/%Y %H:%M:%S")
			timestamp_utc = format_date + dt.timedelta(hours=3)
			format_date1 = datetime.strptime(str(timestamp_utc),"%Y-%m-%d %H:%M:%S").strftime('%Y%m%d-%H%M%S')
		
			with open("frames.csv","r") as file_frames:
				for linea_csv in file_frames:
					columna_csv=linea_csv.split(",")
					if (format_date1==columna_csv[1] and (linea_csv not in lineas)):
						lineas.append(linea_csv)
						rfids.append(rfid)
						
		if (count==4909):
			aux=False

		count+=1


file = open("rfidyframes.csv","w")
for i,j in zip(lineas,rfids):
	file.write("{},{}".format(i,j))
file.close()



'''
for linea in file_frames:
	columna=linea.split(",")
	format_date = datetime.strptime(timestamp,"%d/%m/%Y %H:%M:%S").strftime('%Y%m%d-%H%M%S')
	if (columna[1]==format_date):
		print(linea)
		print(format_date)
'''
