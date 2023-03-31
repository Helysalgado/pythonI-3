# T2_ContenidoAT_GC

## Autor: Camila Villazon Soto Innes

### Version: 30/03/2023

# Introducción
En Python es posible trabajar con el contenido de un archivo. Para ello se utilizan los métodos:
- open(): para acceder al contenido
- read(): para leer el contenido
Para poder ocupar un archivo, es necesarioindicar la ruta o path del archivo.

De igual manera, cuando se trabaja con un string, el método count nos permite fácilmente contar la ocurrencia de un caracter en especial. 

# Problema
A manera de practicar estos comandos y diferentes operadores se resuelve el siguiente problema:
Escribir un programa que regrese el porcentaje de AT y GC de una secuencia de DNA almacenada en un archivo .txt proporcionado por el usuario. 

# Metodología
1. Se almacena el archivo proporcionado por el usuario en la variable archivo_original. Se recomienda que el usuario utilice el archivo dna.txt encontrado en la carpeta data
2. Se abre el archivo con la variable archivo_abierto
3. Se lee el archivo con la variable dna_contenido
4. Se elimina el ultimo caracter de la cadena con .rstrip
5. Se cuenta la ocurrencia de cada nucleótido en el string, que se almacenan en las variables a, t, g, c, respectivamente.
6. Se calcula el total de nucleótidos sumando las cuatro variables a, t, g, y c. 
7. El porcentaje de AT se calgula sumando a y t, dividiendo entre el total de nucleótidos, y el resultado multiplicado por 100.
8. El porcentaje de GC se calgula sumando g y c, dividiendo entre el total de nucleótidos, y el resultado multiplicado por 100.


# Resultados
Al usar el archivo dna.txt de la carpeta data, el resultado debe ser: 
El porcentaje de AT es :  51.07398568019092  %
El porcentaje de GC es:  48.92601431980907  %