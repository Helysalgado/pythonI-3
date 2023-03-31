# T1_SecuenciaRNA

## Autor: Camila Villazon Soto Innes

### Version: 30/03/2023

# Introducción
El tipo de dato string es una clase que se puede manipular a conveniencia gracias a los multiples métodos que posee.
Algunos de estos métodos son: 
- 'find()': que permite encontrar la posicion de un caracter determinado
- '+': no es un método, pero es un operador que nos permite concatenar diferentes variables

# Problema
Para ejercitar la manipulación de cadenas se plantea el siguiente problema: 
Encontrar la posición del codón de inicio en la secuencia AAGGTACGTCGCGCGTTATTAGCCTAAT. De igul forma, imprimir la secuencia entre el codón de inicio y el codón de paro.

# Metodología
1. Se almacena la secuencia en la variable dna
2. Se establece que el codón de inicio complementario es TAC. Se encuentra su posición con la función 'find'
3. Se imprime la posición 
4. Buscar la posición del codón de paro con 'find'
5. Se imprime la secuencia entre el codón de paro y de inicio, ya que se puede imprimir la cadena indicando la posicion [inicio:fin]


# Resultados
Este programa arroja el siguiente resultado:

El codon de inicio esta en la posicion:  4

El fragmento que sera RNA es:  TACGTCGCGCGTT