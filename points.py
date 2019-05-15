import shots, Paso2,variables

#EN ESTE ARCHIVO HAY FUNCIONES RELACIONADAS A LOS PUNTOS DE LOS JUGADORES
generala = []
doblegenerala = []
full = []
poker = []
escalera = []
uno = []
dos = []
tres = []
cuatro = []
cinco = []
seis = []

#Esta funcion inicializa la lista de los puntos que tiene cada jugador por cada juego, para una partida nueva.
#VER SI LE PASO EL VALOR A ADJUNTAR TENIENDO EN CUENTA SI SE REANUDA UNA PARTIDA.
def pointsInitialize():
    value = '-'
    for x in Paso2.name:
        generala.append(value)
        doblegenerala.append(value)
        full.append(value)
        poker.append(value)
        escalera.append(value)
        uno.append(value)
        dos.append(value)
        tres.append(value)
        cuatro.append(value)
        cinco.append(value)
        seis.append(value)

def pointsList():
    i = 1

def pointsUpdate():
    i = 1