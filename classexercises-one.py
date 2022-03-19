# 1- Cambiar un texto
# Necesitamos mostrar en nuestra web la sinopsis de las películas. El problema es que tenemos los textos separados por pipes ("|") en lugar de saltos de línea.
string = 'Sinopsis | Marty McFly, un típico adolescente americano de los años ochenta, '\
'es accidentalmente enviado de vuelta a 1955 en una "máquina del tiempo" realizada con'\
'un DeLorean inventada por un científico un poco loco. | En este viaje, Marty debe '\
'asegurarse de que sus padres se encuentren y se enamoren, para que pueda volver a su tiempo. '

string = string.replace("|", "\n")
print(string)



# 2 - Crear un acrónimo
# Ahora nos piden crear un acrónimo (una palabra compuesta por la primera letra de cada palabra) de cada título. Pero antes de eso es necesario que transformemos los títulos a "title case" porque no todos van a llegar prolijos. Entonces, el acrónimo de "Volver al futuro" debería ser "VAF".

titulo = 'Volver al futuro'.title().split()
acronimo = ''

for i in titulo:
  acronimo += i[0]

print(acronimo)


# Pegar la siguiente variable en una celda y completar el código de manera que Python imprima los nombres de las personas cuyos documentos sean mayores o iguales a treinta millones, ¿se animan?

dnis = {'Conti': 35678456, 'Rafecas': 21435786, 'Neuer': 2876898, 'Hernández': 18565999, 'Arminia': 42375814, 'Díaz': 19678933, 'González': 25678433, 'Stark': 378974327}

for dni in dnis:
  if dnis[dni] >= 30000000:
    print('DNI de esta persona es mayor a 30000000:', dni)
  
