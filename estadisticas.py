estadisticas_enemigos = {
    "Nor": { #Zombie normal
        "vida": 5,
        "velocidad": 10,
        "dano": 1,
        "recompensa": 5,
        "imagen": "assets/imagenes/zombies/zombie_normal.png",
        },
    "Len": { #Zombie lento, con mayor vida
        "vida": 25,
        "velocidad": 5,
        "dano": 3,
        "recompensa": 30,
        "imagen": "assets/imagenes/zombies/zombie_lento.png",
        },
    "Rap": { #Zombie rapido, con misma vida
        "vida": 5,
        "velocidad": 2.8,
        "dano": 3,
        "recompensa": 10,
        "imagen": "assets/imagenes/zombies/zombie_rapido.png",
        },
    "Jf1": { #Primer jefe, posee muchisima vida. Hace dano a la torre segun la vida que tenga en ese momento.
        "vida": 100,
        "velocidad": 1.3,
        "dano": "Igual a la vida final",
        "recompensa": 100,
        "imagen": "imagen",
        },
    "Mar": { #Zombie ligeramente más rapido
        "vida": 70,
        "velocidad": 2.1,
        "dano": 10,
        "recompensa": 70,
        "imagen": "la imagen",
        },
    "Base": { #Copia y pega
        "vida": 0,
        "velocidad": 0,
        "dano": 0,
        "recompensa": 0,
        "imagen": "imagen",
        },
}

estadisticas_torretas = {
    "Flecha": { #Dispara a los enemigos uno por uno
        "costo": 15,
        "dano": 5,
        "espera": 1.5,
        },
    "Base": { #Copia y pega
        "costo": 0,
        "dano": 0,
        "espera": 0,
        },
}

estadisticas_jugador = {
    "vida": 0,
    "dinero": 0,
}