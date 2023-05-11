'''
NAME
    T6_piedra-papel-tijera   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este script permire al usuario jugar piedra, papel o tijera con la computadora.
        El programa pide al usuario su opción y la computadora aleatoriamente eligirá su opción.
    
        
USAGE
    % py T6_piedra-papel-tijera.py
    
'''
# ===========================================================================
# =                            main
# ===========================================================================

import random

#pedir el nombre del usuario y explicar reglas del juego
print ("================================== \n",
       "Bienvenido al juego de Piedra, Papel o Tijera \n \n",
            "¿Cómo te llamas?: ")
name= input()
print ("\n\n Hola "+ name + "!","\n   Para jugar debes  ingresar la palabra 'piedra', 'papel' o 'tijera'. \n",
            "   La computadora elige una opción al azar.\n", 
            "   Suerte! \n")
play_again=2
while play_again: 
    print ("Ingresa tu opción: ")
    users_choice= input()
    users_choice= users_choice.lower()
    print ("\n", name, ": ", users_choice)

    #generar la poción de la computadora
    options= ["piedra", "papel", "tijera"]
    num= random.randint(0,2)
    computers_choice= options[num]
    print("\n Computadora: "+ computers_choice)

    #Ver quien gana
    if users_choice == "papel" and computers_choice== "piedra":
        print("\n Ganaste!")
    elif users_choice == "piedra" and computers_choice== "tijera":
        print("\n Ganaste!")
    elif users_choice == "tijera" and computers_choice== "papel":
        print("\n Ganaste!")
    elif users_choice == "papel" and computers_choice== "tijera":
        print("\n Perdeiste, suerte a la proxima...")
    elif users_choice == "piedra" and computers_choice== "papel":
        print("\n Perdeiste, suerte a la proxima...")
    elif users_choice == "tijera" and computers_choice== "piedra":
        print("\n Perdeiste, suerte a la proxima...")
    else: print("\n Empate, ésto no se puede quedar así!")

    print("\n============================================")

    play_again=2
    #Preguntar al usuario si quiere jugar otra vez
    while play_again and play_again!=1:
        print("\n Deseas velver a jugar? \n sí= 1 \n no= 0 \n : ")
        play_again= input()
        play_again=int(play_again)
        if play_again<0 or play_again>1:
            print("\n Perdón, no entendí.")


print("\n Hasta la próxima "+ name+ "\n")


    