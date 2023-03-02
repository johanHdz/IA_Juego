import pygame as pg

ANCHO = 1000
ALTO = 700


class Personaje(pg.sprite.Sprite):

    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectangulo del personaje
        self.image = pg.image.load("src/sol_1.png").convert()
        self.image.set_colorkey((255, 255, 255))
        # Obtener el renctangulo (Sprite)
        self.rect = self.image.get_rect()
        # Posicionamiento del personaje
        self.rect.center = (0, 0)
        # Velocidad del personaje (inicial)
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        # Velocidad predeterminada cada vuelta del bucle si no se pulsa nada
        self.velocidad_x = 0
        self.velocidad_y = 0

        # Guardar la tecla que es siendo pulsada
        teclas = pg.key.get_pressed()

        # Movimiento hacía la izq
        if teclas[pg.K_a]:
            self.velocidad_x = -65
        # Movimiento hacía la der
        if teclas[pg.K_d]:
            self.velocidad_x = 65
        # Movimiento hacía arriba
        if teclas[pg.K_s]:
            self.velocidad_y = 65
        # Movimiento hacpia abajo
        if teclas[pg.K_w]:
            self.velocidad_y = -65

        # Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        # Limites de margen
        # Izquierdo
        if self.rect.left <= 30:
            self.rect.left = 30
        # Derecho
        if self.rect.right >= 675:
            self.rect.right = 675
        # Superior
        if self.rect.top <= 30:
            self.rect.top = 30
        # Inferior
        if self.rect.bottom >= 675:
            self.rect.bottom = 675
