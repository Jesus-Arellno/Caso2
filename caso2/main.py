# importacion de herramientas
import csv
import operator

def Star():
  archivo = open("synergy_logistics_database.csv")
  lector = csv.reader(archivo)

  index = 0
  data = {}
  rutas = []
  routservis = {}
  servismax = {}
  for row in lector:
    if row[4] == '2015':
      index += 1
      data[index] = row
  for row in data.items():
    rout = row[1][2] + ' - ' + row[1][3]
    if rout not in rutas:
      rutas.append(rout)
  for rout in rutas:
    servicios = []
    for servis in data.items():
      if rout == servis[1][2] + ' - ' + servis[1][3]:
        servicios.append(servis)
        routservis[rout] = servicios
  for servicios in routservis.items():
    servisall = {}
    for servis in servicios[1]:
      servisall[servis[0]] = servis[1][9]
      maximo = max(servisall.items(),key=operator.itemgetter(1))
      servismax[maximo[0]] = maximo[1]
  for q in range(0,len(servismax)):
    if q + 1 <= 64:
      minimo = min(servismax.items(),key=operator.itemgetter(1))
      servismax.pop(minimo[0])
  print(" Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más demandadas. Acorde a los flujos tanto de importación como de exportación, indica:")
  for servisall in servismax.items():
    print(data[servisall[0]])

Star()