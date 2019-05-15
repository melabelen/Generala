import shots,variables

#EN ESTE ARCHIVO HAY FUNCIONES RELACIONADAS CON LOS DADOS Y COMO SABER SI HAY UNA JUGADA VALIDA

def diceReset():



#VER, NO TERMINADA
def dicePlay():
    jugada = diceRoll()
    while tiradas < 3:
        question = int(input("Quiere tirar los dados de vuelta? Si es así, ingrese un 1" ))
        if question == 1:
            input("Ingrese los dados que quiere volver a tirar: ")
            jugada = diceRoll()  #DEPENDE DE LO QUE VAYA EN DICEROLL
            tiradas +=1
        else:
            diceSayOptions(jugada)
            answer= input("Ingrese la opcion por la que anotara puntos (También escriba el nombre "
                          "de uno de los juegos si tachará una de las opciones: ")
            upper(answer)


#HACER Y VER FUNCION QUE HACE LOS VALORES DE LOS DADOS
def diceRoll():
    insert = 1

#jugada son los dados y tiros son la cantidad de tiradas que se han hecho
def diceEvaluate(jugada):
    shot = {"GENERALA":juegos.shotsGenerala(jugada), "FULL":juegos.shotsFull(jugada), "POKER":juegos.shotsPoker(jugada),
             "ESCALERA" : juegos.shotsEscalera(jugada), "DOBLE GENERALA": juegos.shotsDobleGenerala(jugada), "1": juegos.shotsAlNumero(jugada,1)
             , "2": juegos.shotsAlNumero(jugada, 2), "3": juegos.shotsAlNumero(jugada,3), "4": juegos.shotsAlNumero(jugada,4),
             "5": juegos.shotsAlNumero(jugada,5), "6": juegos.shotsAlNumero(jugada,6)}
    return shot

#VER SI YA ESTA ANOTADA LA JUGADA
def diceSayOptions(jugada):
    shotvalues = diceEvaluate(jugada)
    for key,value in shotvalues.items():
        if value == True:
            print("Usted puede anotarse puntos para {} ".format(key))

#VER QUE ONDA SI ES SERVIDO
def dicePointsValues(jugada):
    options = diceEvaluate()
    points = {"Generala": 50 if options["Generala"]==True else 0, "Full": 35 if options["Full"]==True else 0, "Poker": 45 if options["Poker"]==True else 0,
              "Escalera" : 25 if options["Escalera"]==True else 0, "Doble Generala": 60 if options["Doble Generala"]==True else 0,
              "1": juegos.shotsAppearences(jugada,1) if options["1"]==True else 0, "2": juegos.shotsAppearences(jugada, 2) if options["2"]==True else 0,
              "3": juegos.shotsAppearences(jugada,3) if options["3"]==True else 0, "4": juegos.shotsAppearences(jugada,4) if options["4"]==True else 0,
             "5": juegos.shotsAppearences(jugada,5) if options["5"]==True else 0, "6": juegos.shotsAppearences(jugada,6) if options["6"]==True else 0}
    return points

def diceSavePoints(jugada):
    puntos = 1


