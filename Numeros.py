# Archivo: generar_numeros.py
import os

# Directorio de trabajo donde se ubicará el archivo
directorio_trabajo = 'C:/Users/ch_us/OneDrive - Universidad San Sebastian/Diplomado Cloud/Material/Clase_24'  # Reemplaza con la ruta deseada

# Asegúrate de que el directorio exista
os.makedirs(directorio_trabajo, exist_ok=True)

# Ruta completa al archivo
ruta_archivo = os.path.join(directorio_trabajo, 'numeros.txt')

with open(ruta_archivo, 'w') as file:
    for i in range(1, 100001):
        file.write(str(i) + '\n')

