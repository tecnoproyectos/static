"""
Renombra todos los archivos del directorio y subdirectorios
"""

import os
import re
import unicodedata


comunidades = [
    'andalucia', 'aragon', 'asturias', 'baleares',
    'canarias', 'cantabria', 'clm', 'cyl',
    'catalunya', 'valencia', 'extremadura', 'galicia',
    'madrid', 'murcia', 'navarra', 'paisvasco',
    'rioja', 'uned',
    ]


def main():
    renombrar_archivos('.')
    input('Pulsa Enter')


def normalizar_nombre(nombre):
    nombre = nombre.lower()
    # Sustituir ñ y Ñ antes de eliminar acentos
    nombre = nombre.replace("ñ", "ni").replace("Ñ", "ni")

    # Eliminar tildes
    nombre = unicodedata.normalize("NFD", nombre)
    nombre = "".join(c for c in nombre if unicodedata.category(c) != "Mn")
    nombre = unicodedata.normalize("NFC", nombre)

    # Eliminar espacios
    nombre = re.sub('[_ \t]+', '-', nombre)

    # Minúsculas
    nombre = nombre.lower()
    
    return nombre


def renombrar(nombre):
    if not re.search('tein', nombre):
        nombre = 'tein-' + nombre
    for comunidad in comunidades:
        if re.search(comunidad, nombre):
            nombre =  comunidad + '-' + re.sub(comunidad, '', nombre)
    if not re.search('pau', nombre):
        nombre = 'pau-' + nombre
    return re.sub('-+', '-', nombre)


def renombrar_archivos(directorio):
    for raiz, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo[-4:].lower() != '.pdf':
                continue
            nuevo_nombre = renombrar(normalizar_nombre(archivo))
            if archivo == nuevo_nombre:
                continue
            origen = os.path.join(raiz, archivo)
            destino = os.path.join(raiz, nuevo_nombre)
            if os.path.exists(destino):
                continue
            os.rename(origen, destino)
            print(f"{origen} -> {destino}")


if __name__ == "__main__":
    main()
