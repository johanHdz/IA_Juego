import pygame as pg
#inizializar
pg.init()

#Medidas
ANCHO = 1280
LARGO = 720

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
AMARILLO=(255,255,0)

#mapas
mapa = ["XXXXXXXXXXXXXXXX",
        "X   F          X",
        "X XXXXXXX XXXX X",
        "XX      F      X",
        "X XXXXXX XXX XXX",
        "XX  XX         X",
        "X XX  XXXXFXXX X",
        "X        F     X",
        "XXXXXXXXXXXXXXXX"]

#funciones
def dibujarMuro(superficie, rectangulo):
    pg.draw.rect(superficie, BLANCO, rectangulo)

def dibujarPersonaje(superficie, rectangulo):
    pg.draw.rect(superficie, VERDE, rectangulo)

def dibujarPremio(superficie, rectangulo):
    pg.draw.rect(superficie, AMARILLO, rectangulo)

def dibujarMurosI(superficie, posx, posy):
    image = pg.image.load("src/pared_chiquita.jpeg").convert()

    superficie.blit(image, (posx, posy))


def construirMapa(mapa, ventana):
    muros = []
    premios = []
    imgMuro = pg.image.load("src/pared_chiquita.jpeg").convert()
    x = 0
    y = 0
    for fila in mapa:
        for baldosa in fila:
            if baldosa == "X":
                muros.append(pg.Rect(x,y,80,80))
                #ventana.blit(imgMuro, (x, y))
                pg.draw.rect(ventana, BLANCO, (x, y, 60, 60))
            if baldosa == "F":
                premios.append(pg.Rect(x,y,60,60))
            x = x + 80
        x = 0
        y = y + 80
    pg.display.flip()
    return muros, premios

def dibujarMapa(superficie, muros, premios):
    #for muro in muros:
        #dibujarMuro(superficie, muro)
    for premio in premios:
        dibujarPremio(superficie, premio)


#ventana
ventana = pg.display.set_mode((ANCHO,LARGO))

#puntacion
fuenteLetra = pg.font.SysFont("console", 25)
texto = fuenteLetra.render("JUEGO DIVERTIDO", True, BLANCO)
reloj = pg.time.Clock()

#Datos
muros, premios = construirMapa(mapa, ventana)

personaje = pg.Rect(600, 400, 50,50)
personajeVelocidadX = 0
personajeVelocidadY = 0
#premios
premiosFaltantes = str(len(premios))

#bucle principal
jugando = True
pantallaFinal = False
while jugando:
    reloj.tick(60)
    #pantalla de final
    #pantallaFinal = False
    #eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            jugando=False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                jugando = False
            if event.key == pg.K_RIGHT:
                direccion = "derecha"
                personajeVelocidadX = 5
                personajeVelocidadY = 0
            if event.key == pg.K_LEFT:
                direccion = "izquierda"
                personajeVelocidadX = -5
                personajeVelocidadY = 0
            if event.key == pg.K_DOWN:
                direccion = "abajo"
                personajeVelocidadY = 5
                personajeVelocidadX = 0
            if event.key == pg.K_UP:
                direccion = "arriba"
                personajeVelocidadY = -5
                personajeVelocidadX = 0

        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                personajeVelocidadX = 0
            if event.key == pg.K_LEFT:
                personajeVelocidadX = 0
            if event.key == pg.K_DOWN:
                personajeVelocidadY = 0
            if event.key == pg.K_UP:
                personajeVelocidadY = 0

    #logica
    personaje.x = personaje.x +personajeVelocidadX
    personaje.y = personaje.y + personajeVelocidadY

    if personaje.x > ANCHO - personaje.width:
        personaje.x = ANCHO -personaje.width
    if personaje.x < 0:
        personaje.x = 0
    if personaje.y > LARGO - personaje.height:
        personaje.y = LARGO - personaje.height
    if personaje.y < 0:
        personaje.y = 0

    for muro in muros:
        if personaje.colliderect(muro):
            if direccion =="derecha":
                personaje.right =  muro.left
            if direccion =="izquierda":
                personaje.left = muro.right
            if direccion == "abajo":
                personaje.bottom = muro.top
            if direccion == "arriba":
                personaje.top = muro.bottom

    #colicion premio
    for premio in list(premios):
        if personaje.collidepoint(premio.centerx, premio.centery):
            premios.remove(premio)

    #puntacion
    textoPuntacion = fuenteLetra.render("Cuadros faltantes: " + str(len(premios)), True, BLANCO)
    #para pantalla final
    if len(premios) == 0:
        pantallaFinal = True
        jugando = False

    #dibujo
    ventana.fill(NEGRO)
    #mapa
    dibujarMapa(ventana, muros, premios)

    #texto v
    ventana.blit(texto,(10, 10))
    ventana.blit(textoPuntacion,(900 ,20))

    dibujarPersonaje(ventana, personaje)

    #image = pg.image.load("src/pared_chiquita.jpeg")
    #rect = image.get_rect()
    #rect.center((100, 100))

    #para pantalla final
    while pantallaFinal:
        #jugando = False

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    jugando = True
                    print(jugando)
                    pantallaFinal = False
                    print(pantallaFinal)

            if event.type == pg.QUIT:
                jugando = False
                pantallaFinal = False


        ventana.fill(NEGRO)

        mensajeFinal = ["Jugar de nuevo?",
                        "Presione barra espaciadora"]
        y = 80
        for i in mensajeFinal:
            mensaje = fuenteLetra.render(i, True, BLANCO)
            ventana.blit(mensaje, (350, y))
            y = y + 80
        pg.display.update()




    pg.display.update()