"""
Convierte el listado de todos los archivos PDF de este directorio
en una tabla de reStructuredText
"""
import os
import re

comunidades = [
   ['andalucia',     'Andalucía'],
   ['aragon',        'Aragón'],
   ['asturias',      'Asturias'],
   ['baleares',      'Baleares'],
   ['canarias',      'Canarias'],
   ['Cantabria',     'Cantabria'],
   ['castillalamancha', 'Castilla la Mancha'],
   ['castillayleon', 'Castilla y León'],
   ['catalunya',     'Cataluña'],
   ['catalunya',     'Cataluña'],
   ['valencia',      'Comunidad Valenciana'],
   ['extremadura',   'Extremadura'],
   ['galicia',       'Galicia'],
   ['madrid',        'Madrid'],
   ['murcia',        'Murcia'],
   ['navarra',       'Navarra'],
   ['paisvasco',     'País Vasco'],
   ['rioja',         'Rioja'],
   ]


materias = [
    ['tecnologia-ingenieria-ii', 'Tecnología e Ingeniería II'],
    ]


tipo_examenes = [
    ['-extra', 'Extraordinaria'],
    ['-modelo', 'Modelo'],
    ['-ordinaria', 'Ordinaria'],
    ['-coincide', 'Coincidentes'],
    ['-solucion', 'Soluciones'],
    ]

table_header = '''.. list-table:: Exámenes PAU
   :header-rows: 1
   :widths: auto
   :align: center

   * - Comunidad
     - Curso
     - Materia
     - Examen
'''


def main():
    table = [table_header]
    file_names = read_file_names()
    for file_name in file_names:
        comunidad = rename_comunidad(file_name.split('-')[1])
        curso = '20' + '-'.join(file_name.split('-')[2:4])
        materia = read_materia(file_name)
        examen = read_tipo_examen(file_name)
        table.append(f'   * - { comunidad }\n' +
           f'     - { curso }\n' +
           f'     - `{ materia } - { examen }\n' +
           f'       </static/pau/{ file_name }>`__\n')
    write_file('tabla.rst', ''.join(table))


def write_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as fo:
        fo.write(data)


def read_tipo_examen(file_name):
    tipos = []
    for tipo_examen in tipo_examenes:
        if re.search(tipo_examen[0], file_name):
            tipos.append(tipo_examen[1])
    return ' '.join(tipos)


def read_materia(file_name):
    for materia in materias:
        if re.search(materia[0], file_name):
            return materia[1]
    return 'No reconocida'


def rename_comunidad(text):
    for comunidad in comunidades:
        text = re.sub(comunidad[0], comunidad[1], text)
    return text


def read_file_names():
    file_names = [f for f in os.listdir('.') if f[-4:].lower() == '.pdf']
    return sorted(file_names, reverse=True)


main()
