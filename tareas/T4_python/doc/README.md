# T4_RawToFastA

## Autor: Camila Villazon Soto Innes

### Version: 30/03/2023

# Introducción
En Python se puede trabajar con archivos de texto. El usuario puede ingresarlos como input, se pueden abrir, leer, cerrar e incluso escribir. Para ello se usan los siguientes comandos y métodos:

- open("path_del_archivo") para acceder al archivo
- read() para leer 
- rstrip() para quitar el caracter al final de la cadena
- close() para cerrar el archivo

# Problema
Para practicar se resuelve el Problema:
Crear un archivo fasta a partir de la secuencia de DNA que está en `dna.txt`

# Metodología
1. Pedir al usuario el path del archivo tipo .txt con una secuencia de DNA, que se almacena en la variable archivo_original. Se recomienda que el usuario utilice el archivo dna.txt encontrado en la carpeta data
2. Pedir el nombre de la secuencia de DNA al usuario, que se almacena en nombre_seq
3. Se abre el archivo con la variable archivo_abierto, 
4. Se lee el archivo en la variable dna_contenido
5. Se remueve el último caracter de la cadena
6. Se crea el archivo fasta con la variable archivo_fasta
7. Para escribir en el archivo se concatena el nombre de la secuencia y el contenido del archivo .txt
8. Se cierra el archivo fasta


# Resultados
El resultado está en la carpeta results. 
