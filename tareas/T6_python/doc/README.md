T6_piedra-papel-tijera
Autor: Camila Villazon Soto Innes
Version: 10/05/2023

## Introducción

Piedra, papel o tijera(s), es un juego de manos en el que existen tres elementos: la piedra, que vence a la tijera rompiéndola, la tijera, que vence al papel cortándolo, y el papel, que vence a la piedra envolviéndola. Se utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se hace a veces usando una moneda, o para dirimir algún asunto, ver https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera. 

Este programa simula el juego de piedra papel o tijera. El usuario podrá jugar con la computadora.

Al jugar debe obtener los siguientes resultados:
  Usuario: papel, Computadora: piedra= gana usuario.
  Usuario: papel, Computadora: tijera= pierde usuario.

  Usuario: piedra, Computadora: tijera= gana usuario.
  Usuario: piedra pierde ante papel= pierde usuario.

  Usuario: tijera, Computadora: papel= gana usuario.
  Usuario: tijera, Computadora: piedra= pierde usuario.

  Si las dos opciones son iguales es empate.

## Instalación 

El programa esta hecho en python, asi que es necesario que tengas instalado python en tu computadora.
Podrás clonar este repositorio o copiar el programa a un archivo de texto en tu computadora.


## Cómo correr el programa

El programa tiene una interfaz Command Line (CLI) por lo que debe ejecutarse de la siguiente manera desde una terminal:

```
python T6_piedra-papel-tijera.py
```

El programa `T6_piedra-papel-tijera` hace lo siguiente:

1. Pedir al usuario su nombre y una opción 'piedra', 'papel' o 'tijera'.
2. El programa genera una opción al azar
3. La elección del usuario y la generada por el programa son evaluadas para determinar si el usuario gana, pierde o empata.


```
================================== 
 Bienvenido al juego de Piedra, Papel o Tijera 
 
 ¿Cómo te llamas?: 
hely


 Hola hely! 
   Para jugar debes  ingresar la palabra 'piedra', 'papel' o 'tijera'. 
    La computadora elige una opción al azar.
    Suerte! 

Ingresa tu opción: 

```

Mostramos algunos ejemplos de la respuesta del programa para el juego

a. El usuario da la opción *papel*, la computadora *piedra*. El usuario debería ganar.

```
Ingresa tu opción: 
papel

 hely :  papel

 Computadora: piedra

 Ganaste!

============================================

 Deseas velver a jugar? 
 sí= 1 
 no= 0 
 : 

```

b. Cuando es un empate, se mostraría:

```
Ingresa tu opción: 
papel

 hely :  papel

 Computadora: papel

 Empate, ésto no se puede quedar así!

============================================

 Deseas velver a jugar? 
 sí= 1 
 no= 0 
 : 

```

El programa termina al dar la opción 0 cuando pregunta si se desea volver a jugar.


