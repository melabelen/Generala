#EN ESTE ARCHIVO HAY FUNCIONES CON RESPECTO A LA CREACION DE UNA LISTA DE JUGADORES

names = []
def playersList(quantity):

    print("A continuacion, ingrese los nombres de los jugadores: ")
    while quantity != 0:
        names.append(input("Ingrese un nombre: "))
        quantity -= 1

    return names
def playersSet():
    quant = int(input("Ingrese la cantidad de jugadores: "))
    playersList(quant)