enemigos = {
    "Nor": { #Zombie normal
        "vida": 12,
        "velocidad": 1.5,
        "dano": 1,
        "recompensa": 75,
        "imagen": "assets/imagenes/zombies/zombie_normal.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_normal_auch.png",
        },
    "Len": { #Zombie lento, con mayor vida
        "vida": 60,
        "velocidad": 0.7,
        "dano": 5,
        "recompensa": 150,
        "imagen": "assets/imagenes/zombies/zombie_lento.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_lento_auch.png",
        },
    "Rap": { #Zombie rapido, con misma vida
        "vida": 18,
        "velocidad": 2.8,
        "dano": 3,
        "recompensa": 100,
        "imagen": "assets/imagenes/zombies/zombie_rapido.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_rapido_auch.png",
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

torretas = {
    "Tanque":
    [
        {
            "dano": 2,
            "rango": 130,
            "espera": 1300,
            "precio": 150,
            "imagen": "assets/imagenes/torretas/torreta_tanque_I.png",
        },
        {
            "dano": 5,
            "rango": 140,
            "espera": 1000,
            "precio": 600,
            "imagen": "assets/imagenes/torretas/torreta_tanque_II.png",
        },
        {
            "dano": 15,
            "rango": 150,
            "espera": 800,
            "precio": 3000,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        }
    ],
    "Lanzallamas":
    [
        {
            "dano": 1,
            "rango": 115,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_lanzallamas_I.png",
        },
        {
            "dano": 0,
            "rango": 130,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_bomba_II.png",
        },
        {
            "dano": 0,
            "rango": 170,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_bomba_III.png",
        },
    ],
    "Base":
    [
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
    ]
}

jugador = {
    "vida": 100,
    "dinero": 525,
}