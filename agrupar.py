import csv
import collections

archivo_global = open('global.csv', 'w')
archivo_hashtags = open('hashtags.csv', 'w')
archivo_menciones = open('menciones.csv', 'w')
archivo_cantidad = open('total.csv', 'w')
archivo_horas = open('horasRefinado.csv', 'w')
archivo_usuarios = open('usuarios.csv', 'w')
archivo_manini = open('manini.csv', 'w')

archivo_global.write('identificador,dia,hora,user,texto'+'\n')
archivo_hashtags.write('hashtag,cantidad'+'\n')
archivo_menciones.write('usuario,cantidad'+'\n')
archivo_cantidad.write('tuits,total'+'\n')
archivo_horas.write('hora,cantidad'+'\n')
archivo_usuarios.write('usuario,cantidad'+'\n')
archivo_manini.write('candidato,cantidad'+'\n')

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
        hashtags[hashtag] = 1

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
        hashtags[hashtag] = 1

for attribute, value in hashtags.items():
  archivo_menciones.write('@'+attribute+','+str(value)+'\n')


tuits = []
horas = {}
usuarios = {}
with open('./../global.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      identificador = row[0]
      if (identificador not in tuits):
        hora = row[2]
        hora = hora[0:4]
        try:
          horas[hora] += 1
        except:
          horas[hora] = 1
        user = row[3]
        try:
          usuarios[user] += 1
        except:
          usuarios[user] = 1
        archivo_global.write((',').join(row)+'\n')
        tuits.append(identificador)

archivo_cantidad.write('total'+','+str(len(tuits)))
for attribute, value in horas.items():
  archivo_horas.write(attribute+'0,'+str(value)+'\n')
for attribute, value in usuarios.items():
  archivo_usuarios.write('@'+attribute+','+str(value)+'\n')


manini = []
primera = True
with open('./../manini.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      identificador = row[0]
      if (identificador not in manini):
        manini.append(identificador)
archivo_manini.write('manini'+','+str(len(manini)))

andrade = []
primera = True
with open('./../andrade.csv') as input_file:
  for row in csv.reader(input_file, delimiter=','):
    if primera:
      primera = False
    else:
      identificador = row[0]
      if (identificador not in andrade):
        andrade.append(identificador)
archivo_manini.write('andrade'+','+str(len(andrade)))

print('ok')
