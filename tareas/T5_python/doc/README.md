# T5_python
Autor: Camila Villazon Soto Innes
Version: 14/05/2023

## Introducción
Al desarrollar software, siempre hay que considerar el manejo de errores. Para ello se debe pensar en cuales son las situaciones que pueden causar un problema, identificar el tipo de error y tomar las medidas correspondientes para que el usuario sepa que es lo que el código espera. 
Entre los errores más comunes tenemos el paso de archivos. En este caso la ruta al archivo puede estar mal, el contenido del documento puede venir vacío o no contener información que permita trabajar al programa. 
Debido a lo anterior, se pondrá en práctica el manejo de excepciones. 

## Problema
Modificar los programas:

a. Contar As, Ts, Gs, Cs (count_atgc.py)  
b. Contenido de ATs y GCs (at_gc_content.py)  
c. From raw to fasTA (mk-fasta-format.py)

Para integrar:
- Leer la secuencia desde un archivo aplicalo a todos los programas. 
- Se debe validar que el archivo de la secuencia exista. ¿Qué pasa si existe y viene vacío?
- La secuencia puede venir en 1 linea o en multiples lineas
- Se debe validar que la secuencia solo sean caracteres ATGC y no otros.
- Valida cualquier otro dato que consideres necesario.

## Metodología o Algoritmo

### T5_count_atgc
1. La secuencia de DNA proporcionada por el usuario se almacena en la variable dna
2. Para asegurar que la secuencia esté en mayúsculas se usa la función upper
3. Se imprime la secuencia
4. Para contar la ocurrencia de cada nucleotido se usa la función count, y se almacena en una variable correspondiente a, t, g, y c
5. Se imprime el resultado con print

### T5_at_gc_content

### T5_mk-fasta-format
El programa `T5_mk-fasta-format` hace lo siguiente:

1. Pedir al usuario el path del archivo tipo .txt con una secuencia de DNA, que se almacena en la variable archivo_original.  
    (Se recomienda que para probar el programa, se utilice el archivo dna.txt encontrado en la carpeta data)
2. Pedir el nombre de la secuencia de DNA al usuario, que será usado como identificador de la secuencia.
3. Leer la secuencia de dna del archivo de entrada
7. Formatear la secuencia de formato plano a format fasta
8. Guardar la secuencia fasta en el archivo de salida



## Resultados y Pruebas

### T5_count_atgc
#### Caso 1. El archivo de secuencia existe y se genera un archivo en formato fastA

archivo de entrada: data/dna.txt
descripción: 

1. El programa se ejecuta 
```% py scr/T5_count_atgc.py  ```

2. El programa debe pedir lo siguiente:

```path  ```

3. El resultado se vería en pantalla
``` ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
descripción: el programa arroja la leyenda "Archivo vacío"


#### Caso 3. El archivo de secuencia no existe
archivo de entrada: data/dna_con_N.txt
descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"



### T5_at_gc_content
#### Caso 1. El archivo de secuencia existe y se genera un archivo en formato fastA

archivo de entrada: data/dna.txt
archivo de salida: results/ejemplo-fasta
descripción: 

1. El programa se ejecuta 
```% py scr/T5_at_gc_content.py  ```

2. El programa debe pedir lo siguiente:

```path```

3. El resultado se vería en pantalla
``` ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
descripción: el programa arroja la leyenda "Archivo vacío"

#### Caso 3. El archivo de secuencia no existe
archivo de entrada: data/dna_con_N.txt
descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"



### T5_mk-fasta-format

#### Caso 1. El archivo de secuencia existe y se genera un archivo en formato fastA

archivo de entrada: data/dna.txt
archivo de salida: results/ejemplo-fasta
descripción: 

1. El programa se ejecuta 
```% py scr/T5_mk-fasta-format.py  ```

2. El programa debe pedir lo siguiente:

```path nombre_secuencia path_salida ```

3. El resultado esta en el archivo ejemplo.fasta y el contenido se vería
``` ```

#### Caso 2. El archivo de secuencia viene vacio 
archivo de entrada: data/dna_vacio.txt
archivo de salida: results/dna_vacio.fasta
descripción: el programa arroja la leyenda "Archivo vacío"



#### Caso 3. El archivo de secuencia no existe
archivo de entrada: data/dna_con_N.txt
archivo de salida: reults/dna_con_N.fasta
descripción: el programa arroja "ValueError: Su archivo contiene 6 N's"