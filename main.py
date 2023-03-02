import pygame as pg
import Personaje
import sys


# Dibujo de las casillas
def dibujar_tablero():
    # Rellemos la ventana de un color
    #               R    G    B
    pantalla.fill(VerdeFondo)

    x = 30
    y = 30
    band = 1
    for i in range(1, 11):
        for j in range(1, 11):
            if band == 1:
                pg.draw.rect(pantalla, VerdeCasillas, (x, y, 60, 60))
                band *= -1
            else:
                pg.draw.rect(pantalla, VerdeCasillas, (x, y, 60, 60))
                band *= -1
            x = x + 65
        y = y + 65
        x = 30
        band *= -1


# Variables
Ancho, Alto = 1000, 700
FPS = 15
Reloj = pg.time.Clock()

# Paleta de colores
Blanco = (255, 255, 255)
Negro = (0, 0, 0)
VerdeCasillas = (105, 217, 73)
VerdeFondo = (170, 244, 88)

# Inicialización de Pygame
pg.init()

# Creación de ventana con dimensiones en pixeles
#                              Ancho  Alto
pantalla = pg.display.set_mode((Ancho, Alto))
# Titulo de la ventana
pg.display.set_caption('Juego Test')

pg.draw.rect(pantalla, VerdeCasillas, (30, 30, 60, 60))

# Carga y asignación del icono de ventana
icono = pg.image.load("src/icon.png")
pg.display.set_icon(icono)

# Grupo de Sprites, instancia del objeto personaje
sprites = pg.sprite.Group()
personaje = Personaje.Personaje()
sprites.add(personaje)

Ejecuta = True

# Bucle de acciones
while Ejecuta:
    #  FPS
    Reloj.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Ejecuta = False

    # Control de FPS
    Reloj.tick(FPS)
    # Dibujar el tablero
    dibujar_tablero()
    # Dibuja el sprite
    sprites.draw(pantalla)
    # Actualización de los sprites
    sprites.update()
    # Actualización de la ventana
    pg.display.update()

# Fin del juego
pg.quit()
