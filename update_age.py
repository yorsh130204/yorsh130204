# update_age.py

import datetime

# Obtener la fecha actual
now = datetime.datetime.now()

# Verificar si es el 13 de febrero
if now.month == 2 and now.day == 13:
    # Incrementar la edad
    age = 20  # Tu edad actual
    new_age = age + 1

    # Leer el archivo README.md
    with open('README.md', 'r') as file:
        data = file.readlines()

    # Buscar la línea donde está la edad y actualizarla
    for i in range(len(data)):
        if 'I\'m currently' in data[i]:
            data[i] = f'I\'m currently {new_age} years old and pursuing my studies in multiplatform software development at UTCH.\n'
            break

    # Escribir los cambios de vuelta al archivo
    with open('README.md', 'w') as file:
        file.writelines(data)
