import os
niveles = 0

def obtener_ruta_archivo(numero_ronda):
    nombre_archivo_ronda = "ronda_" + numero_ronda + ".txt"
    ruta_carpeta_actual = os.path.dirname(__file__)
    ruta_carpeta_rondas = os.path.join(ruta_carpeta_actual, "rondas")
    ruta_archivo_ronda = os.path.join(ruta_carpeta_rondas, nombre_archivo_ronda)
    return ruta_archivo_ronda

def procesar_rondas(numero_de_ronda):
    lista_enemigos = []
    ruta_archivo_ronda = obtener_ruta_archivo(str(numero_de_ronda))
    with open(ruta_archivo_ronda, "r") as ronda:
        for oleada in ronda:
            dic_enemigos = crear_diccionarios_enemigos(oleada)
            lista_enemigos.append(dic_enemigos)
    return lista_enemigos

def crear_diccionarios_enemigos(oleada):
    diccionario_enemigos = {}
    oleada = oleada.split()
    for enemy in oleada:
        zombie, cantidad = enemy.split("_")
        diccionario_enemigos.update({zombie: int(cantidad)})
    return diccionario_enemigos