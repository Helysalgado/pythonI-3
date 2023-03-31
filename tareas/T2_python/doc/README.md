# T2_ContarATGC

## Autor: Camila Villazon Soto Innes

### Version: 30/03/2023

# Introducción
Python puede manipular cadenas de texto o strings, que se almacenan en variables por practicidad. 
En esta tarea se ejercita el nombrado consistente de variables y la manipulación de string, que incluyen: concatenación (por medio de sumas), multiplicación y manipulación por métodos de la clase cadena.

# Problema
Para poner a prueba estos elementos se resuelve el problema: 
Pedir una secuencia de DNA al usuario y contar el total de cada nucleótido (A, T, G, C).

# Metodología
1. La secuencia de DNA proporcionada por el usuario se almacena en la variable dna
2. Para asegurar que la secuencia esté en mayúsculas se usa la función upper
3. Se imprime la secuencia
4. Para contar la ocurrencia de cada nucleotido se usa la función count, y se almacena en una variable correspondiente a, t, g, y c
5. Se imprime el resultado con print

# Resultados
Se recomienda que el usuario pruebe con la secuencia: 
AGCTTTTCATTC

Que debe resultar en 
A: 2  
T: 6  
C: 3  
G: 1