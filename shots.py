import variables

#Ver el tema de las tiradas por si algo es servido.
#Ver el tema de la generala doble ya que depende del puntaje del jugador.

#ESTE ES EL ARCHIVO CON FUNCIONES SOBRETODO LO REFERIDO A LAS JUGADAS Y COMO SE OBTIENEN

#-----------------------------------------------------------------------
# #jugada es una lista con los dados que haya tirado el jugador
#numero es el valor de dado para el que se hara la jugada
#quantity es la variable para contar las apariciones del numero.
def shotsAppearences(jugada,numero):
    quantity = 0
    for i in range(0,len(jugada)):
        if numero == jugada[i]:
            quantity += 1
    return quantity

#indica si un numero se encuentra entre la jugada de dados
def shotsAlNumero(jugada, numero):
    return True if numero in jugada else False

#jugada es una lista con los dados que haya tirado el jugador
#define si los dados de la jugada hacen algun juego
#valor1 es la cantidad de veces que tiene tiene que haber dados iguales de un tipo para hacer X juego
#valor2 es la cantidad de veces que tiene tiene que haber dados iguales de otro tipo para hacer X juego
#resultado representa el resultado que tiene que dar la suma entre la cantidad de dados que tengan el mismo valor
#que el dado que se encuentra primero y ultimo (teniendo en cuenta que la jugada está ordenada)
def shotsJuego (jugada,valor1,valor2,resultado):
    jugada.sort()
    a = shotsAppearences(jugada, jugada[0])
    b = shotsAppearences(jugada, jugada[4])
    if ((a == valor1 or a == valor2) and a + b == resultado):
        return True
    return False

def shotsFull(jugada):
    return shotsJuego(jugada,2,3,5)

def shotsPoker(jugada):
    return shotsJuego(jugada,1,4,5)

def shotsGenerala(jugada):
    return shotsJuego(jugada, 5, 5, 10)

#HACER
def shotsDobleGenerala(jugada):
    jugada =1

#jugada es una lista con los dados que haya tirado el jugador
def shotsEscalera(jugada):
    jugada.sort()
    for i in range(0,len(jugada) - 1):
        if jugada[i] != jugada[i + 1]-1:
            return False
    return True