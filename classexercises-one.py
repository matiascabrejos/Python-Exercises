# 2 - Crear un acrónimo
# Ahora nos piden crear un acrónimo (una palabra compuesta por la primera letra de cada palabra) de cada título. Pero antes de eso es necesario que transformemos los títulos a "title case" porque no todos van a llegar prolijos. Entonces, el acrónimo de "Volver al futuro" debería ser "VAF".

titulo = 'Volver al futuro'.title().split()
acronimo = ''

for i in titulo:
  acronimo += i[0]

print(acronimo)
