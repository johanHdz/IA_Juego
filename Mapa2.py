import pygame
import random

# Inicializar pygame
pygame.init()

# Medidas de la ventana
Ancho, Largo = 1280, 600

# Mapa
mapa = ["1011110000",
        "1001000010",
        "1011101110",
        "1000100010",
        "1010101100",
        "1110001001",
        "0000101011",
        "1110111000",
        "1000000010",
        "1011010111"]


# Funciones
def construir_mapa(mapa):
    muros = []
    camino = []
    x, y = 0, 0

    for fila in mapa:
        for baldosa in fila:
            if baldosa == "1":
                muros.append(pygame.Rect(x, y, 60, 60))
            elif baldosa == "0":
                camino.append([x, y])
            x = x + 60
        x = 0
        y = y + 60
    return muros, camino

def dibujar_mapa(vent):
    x, y = 0, 0
    imgMuro = pygame.image.load("src/agua.jpg").convert()
    imgSuelo = pygame.image.load("src/suelo.png").convert()

    for fila in mapa:
        for baldosa in fila:
            if baldosa == "1":
                vent.blit(imgMuro, (x, y))
            else:
                pygame.draw.rect(vent, (0, 0, 0), (x, y, 60, 60))
                # pygame.draw.rect(vent, (113, 250, 95), (x, y, 60, 60))
                # vent.blit(imgSuelo, (x, y))
            x = x + 60
        x = 0
        y = y + 60

def dibujar_personaje(ventana, objeto):
    psj = pygame.image.load("src/fiaun_chiquito.jpg").convert()
    ventana.blit(psj, (objeto.x, objeto.y))

def dibujar_objetivo(ventana, objeto):
    objetivo = pygame.image.load("src/meta.jpg")
    objetivo.set_colorkey((30, 255, 0))
    ventana.blit(objetivo, (objeto.x, objeto.y))


# Ventana
ventana = pygame.display.set_mode((Ancho, Largo))

# Variables
muros, camino = construir_mapa(mapa)
randPsj = random.randint(0, (len(camino)-1))
randObj = random.randint(0, (len(camino)-1))
reloj = pygame.time.Clock()
personaje = pygame.Rect(camino[randPsj][0], camino[randPsj][1], 60, 60)
personajeVelocidadX, personajeVelocidadY = 0, 0
direccion = None
objetivos = []

while True:
    if randPsj == randObj:
        randObj = random.randint(0, (len(camino) - 1))
    else:
        metaObj = pygame.Rect(camino[randObj][0], camino[randObj][1], 60, 60)
        metaObj.x, metaObj.y = camino[randObj][0], camino[randObj][1]
        objetivos.append(metaObj)
        break


# Bucle principal donde se ejecutara el juego
jugando = True
pantallaFinal = False

while jugando:
    reloj.tick(15)
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

        # Movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                direccion = "derecha"
                personajeVelocidadX = 60
                personajeVelocidadY = 0
            if event.key == pygame.K_LEFT:
                direccion = "izquierda"
                personajeVelocidadX = -60
                personajeVelocidadY = 0
            if event.key == pygame.K_DOWN:
                direccion = "abajo"
                personajeVelocidadX = 0
                personajeVelocidadY = 60
            if event.key == pygame.K_UP:
                direccion = "arriba"
                personajeVelocidadX = 0
                personajeVelocidadY = -60

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                personajeVelocidadX = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                personajeVelocidadY = 0

    # Lógica
    personaje.x = personaje.x + personajeVelocidadX
    personaje.y = personaje.y + personajeVelocidadY

    if personaje.x > 600 - personaje.width:
        personaje.x = 600 - personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > 600 - personaje.height:
        personaje.y = 600 - personaje.height
    if personaje.y < 0:
        personaje.y = 0

    # Colision
    for muro in muros:
        if personaje.colliderect(muro):
            if direccion == "derecha":
                personaje.right = muro.left
            if direccion == "izquierda":
                personaje.left = muro.right
            if direccion == "abajo":
                personaje.bottom = muro.top
            if direccion == "arriba":
                personaje.top = muro.bottom

    for premio in objetivos:
        if personaje.collidepoint(premio.centerx, premio.centery):
            objetivos.remove(premio)

    # Mapa
    ventana.fill((255, 255, 255))
    dibujar_mapa(ventana)
    dibujar_personaje(ventana, personaje)
    if len(objetivos) != 0:
        dibujar_objetivo(ventana, metaObj)
    pygame.display.flip()
    pygame.display.update()
