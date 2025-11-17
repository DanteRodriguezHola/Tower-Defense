from config import pg

jugando = True
estado = "menu"

tiempo_spawn_enemigos = 1500
ultimo_spawn_enemigo = pg.time.get_ticks()
nivel_iniciado = False

creando_torretas = False
torreta_seleccionada = None

velocidad_juego = 1
