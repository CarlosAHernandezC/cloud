import os

# Directorio de trabajo donde se ubicará el archivo (directorio actual)
directorio_trabajo = os.getcwd()

# Asegúrate de que el directorio exista
os.makedirs(directorio_trabajo, exist_ok=True)

# Ruta completa al archivo en el directorio de trabajo
ruta_archivo = os.path.join(directorio_trabajo, 'numeros2.txt')

with open(ruta_archivo, 'w') as file:
    for i in range(1, 100001):
        file.write(str(i) + '\n')
