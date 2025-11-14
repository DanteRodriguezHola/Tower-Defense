from spritesheet import Spritesheet
import config as c

spritesheet_torreta_tanque = Spritesheet("assets/imagenes/torretas/spritesheet_torreta_tanque.png")

enemigos = {
    "Nor": { #Zombie normal
        "vida": 12,
        "velocidad": 1.5,
        "dano": 5,
        "recompensa": 25,
        "imagen": "assets/imagenes/zombies/zombie_normal.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_normal_auch.png",
        },

    "Len": { #Zombie lento, con mayor vida
        "vida": 50,
        "velocidad": 0.7,
        "dano": 7,
        "recompensa": 50,
        "imagen": "assets/imagenes/zombies/zombie_lento.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_lento_auch.png",
        },

    "Rap": { #Zombie rapido, con misma vida
        "vida": 10,
        "velocidad": 3.3,
        "dano": 3,
        "recompensa": 25,
        "imagen": "assets/imagenes/zombies/zombie_rapido.png",
        "imagen_auch": "assets/imagenes/zombies/zombie_rapido_auch.png",
        },

    "Jf1": { #Primer jefe, posee muchisima vida. Hace dano al jugador según la vida que tenga en ese momento.
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
            "espera": 1800,
            "precio": 150,
            "reembolso": 50,
            "imagen": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 0, 0),
            "imagen_mejora": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 50, 0),
        },
        {
            "dano": 5,
            "rango": 145,
            "espera": 1200,
            "precio": 600,
            "reembolso": 200,
            "imagen": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 0, 50),
            "imagen_mejora": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 50, 50),
        },
        {
            "dano": 10,
            "rango": 150,
            "espera": 800,
            "precio": 3000,
            "reembolso": 1000,
            "imagen": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 0, 100),
            "imagen_mejora": spritesheet_torreta_tanque.obtener_imagen(c.ancho_torreta, c.alto_torreta, 50, 100),
        }
    ],
    "Explosivos":
    [
        {
            "dano": 0,
            "rango": 115,
            "espera": 0,
            "precio": 1000,
            "reembolso": 300,
            "imagen": "assets/imagenes/torretas/torreta_dinamita_I.png",
        },
        {
            "dano": 0,
            "rango": 130,
            "espera": 0,
            "precio": 0,
            "reembolso": 0,
            "imagen": "assets/imagenes/torretas/torreta_dinamita_II.png",
        },
        {
            "dano": 0,
            "rango": 170,
            "espera": 0,
            "precio": 0,
            "reembolso": 0,
            "imagen": "assets/imagenes/torretas/torreta_dinamita_III.png",
        },
    ],
    "Base":
    [
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "reembolso": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "reembolso": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
        {
            "dano": 0,
            "rango": 0,
            "espera": 0,
            "precio": 0,
            "reembolso": 0,
            "imagen": "assets/imagenes/torretas/torreta_tanque_III.png",
        },
    ]
}

jugador = {
    "vida": 100,
    "dinero": 500,
}