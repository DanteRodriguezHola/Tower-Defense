estadisticas_enemigos = {
    "Nor": { #Zombie normal
        "vida": 5,
        "velocidad": 1.5,
        "dano": 1,
        "recompensa": 5,
        "imagen": "assets/imagenes/zombies/zombie_normal.png",
        },
    "Len": { #Zombie lento, con mayor vida
        "vida": 25,
        "velocidad": 0.7,
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
    "Tanque":
    [
        {
            "dano": 2,
            "rango": 130,
            "espera": 0,
            "costo": 150,
            "imagen": "assets/imagenes/torretas/torreta_tanque_I.png",
        },
        {
            "dano": 5,
            "rango": 140,
            "espera": 0,
            "costo": 1250,
            "imagen": "assets/imagenes/torretas/torreta_tanque_II.png",
        },
        {
            "dano": 15,
            "rango": 150,
            "espera": 0,
            "costo": 5000,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        }
    ],
    "Lanzallamas":
    [
        {
            "dano": 0,
            "rango": 115,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_lanzallamas_I.png",
        },
        {
            "dano": 0,
            "rango": 130,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_bomba_II.png",
        },
        {
            "dano": 0,
            "rango": 170,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_bomba_III.png",
        },
    ],
    "Base":
    [
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "costo": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
    ]
}

estadisticas_jugador = {
    "vida": 1000,
    "dinero": 500,
}