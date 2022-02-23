import csv
import collections

archivo_global = open('global.csv', 'w')
archivo_hashtags = open('hashtags.csv', 'w')
archivo_menciones = open('menciones.csv', 'w')
archivo_cantidad = open('total.csv', 'w')
archivo_horas = open('horas.csv', 'w')

archivo_global.write('identificador,dia,hora,user,texto'+'\n')
archivo_hashtags.write('hashtag,cantidad'+'\n')
archivo_menciones.write('usuario,cantidad'+'\n')
archivo_cantidad.write('tuits,total'+'\n')
archivo_horas.write('hora,cantidad'+'\n')

hashtags = {}
primera = True
with open('./../hashtags.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      hashtag = row[1]
      try:
        hashtags[hashtag] += 1
      except:
        hashtags[hashtag] = 0

for attribute, value in hashtags.items():
  archivo_hashtags.write(attribute+','+str(value)+'\n')

hashtags = {}
primera = True
with open('./../menciones.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      hashtag = row[1]
      try:
        hashtags[hashtag] += 1
      except:
        hashtags[hashtag] = 0

for attribute, value in hashtags.items():
  archivo_menciones.write(attribute+','+str(value)+'\n')


tuits = []
horas = {}
with open('./../global.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      identificador = row[0]
      hora = row[2]
      hora = hora[0:5]
      try:
        horas[hora] += 1
      except:
        horas[hora] = 0
      if (identificador not in tuits):
        archivo_global.write((',').join(row)+'\n')
        tuits.append(identificador)

archivo_cantidad.write('total'+','+str(len(tuits)))
for attribute, value in horas.items():
  archivo_horas.write(attribute+','+str(value)+'\n')

print('ok')
