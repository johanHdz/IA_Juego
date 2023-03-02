import pygame as pg
import sys


class Maze:
    def __init__(self):
        self.M = 10
        self.N = 10
        self.muros = []
        self.maze = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
                     1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
                     1, 0, 1, 1, 1, 0, 1, 1, 1, 0,
                     1, 0, 0, 0, 1, 0, 0, 0, 1, 0,
                     1, 0, 1, 0, 1, 0, 1, 1, 0, 0,
                     1, 1, 1, 0, 0, 0, 1, 0, 0, 1,
                     0, 0, 0, 0, 1, 0, 1, 0, 1, 1,
                     1, 1, 1, 0, 1, 1, 1, 0, 0, 0,
                     1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                     1, 0, 1, 1, 0, 1, 0, 1, 1, 1]

    def dibujarMaze(self, pantalla, image_surf):
        bx = 0
        by = 0
        for i in range(0, self.M * self.N):
            if self.maze[bx + (by * self.M)] == 1:
                pantalla.blit(image_surf, (bx * 60, by * 60))

            bx = bx + 1
            if bx > self.M - 1:
                bx = 0
                by = by + 1


class Game:
    def colision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False


class Personaje:
    x = 60
    y = 60
    vel = 0.5
    direccion = ""

    def movIzq(self):
        self.direccion = "izquierda"
        self.x = self.x - self.vel
        self.y = self.y

    def movDer(self):
        self.direccion = "derecha"
        self.x = self.x + self.vel

    def movArriba(self):
        self.direccion = "arriba"
        self.y = self.y - self.vel

    def movAbajo(self):
        self.direccion = "abajo"
        self.y = self.y + self.vel


class Juego:
    Ancho, Alto = 600, 600
    personaje = 0

    def __init__(self):
        self._ejecutando = True
        self._pantalla = None
        self._image_surf = None
        self.personaje = Personaje()
        self._muro = None
        self.maze = Maze()

    def inicializar(self):
        pg.init()
        self._pantalla = pg.display.set_mode((self.Ancho, self.Alto))

        pg.display.set_caption("Prueba Maze")
        self._ejecutando = True
        self._image_surf = pg.image.load("src/fiaun_chiquito.jpg").convert()
        self._muro = pg.image.load("src/pared_chiquita.jpeg").convert()

    def on_loop(self):
        # Colisión con paredes
        #for muro in self.maze.muros:
         #   if self.personaje.
          #  if self.personaje.direccion == "izquierda":



        pass

    def on_render(self):
        self._pantalla.fill((0, 0, 0))
        self._pantalla.blit(self._image_surf, (self.personaje.x, self.personaje.y))
        self.maze.dibujarMaze(self._pantalla, self._muro)
        pg.display.flip()

    def terminar(self):
        pg.quit()

    def on_execute(self):
        if self.inicializar() == False:
            self._ejecutando = False

        while self._ejecutando:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self._ejecutando = False

            pg.event.pump()
            keys = pg.key.get_pressed()

            if keys[pg.K_RIGHT]:
                self.personaje.movDer()

            if keys[pg.K_LEFT]:
                self.personaje.movIzq()

            if keys[pg.K_UP]:
                self.personaje.movArriba()

            if keys[pg.K_DOWN]:
                self.personaje.movAbajo()
            self.on_loop()
            self.on_render()
        self.terminar()


juego = Juego()
juego.on_execute()
