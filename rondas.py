import os

def obtener_ruta_archivo(numero_ronda):
    nombre_archivo_ronda = "ronda_" + numero_ronda + ".txt"
    ruta_carpeta_actual = os.path.dirname(__file__)
    ruta_carpeta_rondas = os.path.join(ruta_carpeta_actual, "rondas")
    ruta_archivo_ronda = os.path.join(ruta_carpeta_rondas, nombre_archivo_ronda)
    return ruta_archivo_ronda

def procesar_rondas(numero_de_ronda):
    diccionarios_enemigos = []
    ruta_archivo_ronda = obtener_ruta_archivo(numero_de_ronda)
    with open(ruta_archivo_ronda, "r") as ronda:
        for oleada in ronda:
            diccionario_enemigos = crear_diccionarios_enemigos(oleada)
            diccionarios_enemigos.append(diccionario_enemigos)
    return diccionarios_enemigos

def crear_diccionarios_enemigos(oleada):
    diccionario_enemigos = {}
    oleada = oleada.split()
    for enemigo in oleada:
        enemigo = enemigo.split("_")
        tipo_enemigo = enemigo[0]
        cantidad_enemigo = int(enemigo[1])
        diccionario_enemigos.update({tipo_enemigo: cantidad_enemigo})
    return diccionario_enemigos

enemy_spawn_data = procesar_rondas("1")