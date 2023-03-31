'''
NAME
    T2_ContarATGC   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa cuenta el total de A, C, G y T que hay en una secuencia de DNA ingresada por el
        usuario.
    

'''
# ===========================================================================
# =                            main
# ===========================================================================


# pedri secuendia de DNA al usuario
print("==================================== \n  Ingrese una secuencia de DNA (ATGC): ")
dna= input()

# pasar la secuencia ingresada a mayusculas
dna=dna.upper()

# imprimir la secuencia ingresada por el usuario
print("\n Secuencia ingresada: ",dna)

# contar el total de A, T, G y C
a=dna.count('A')
t=dna.count('T')
g=dna.count('G')
c=dna.count('C')

# imprimir el total de A, T, G y C
print("\n El total de cada nucleotido es: \n A: ",a,"\n T: ",t,"\n G: ",g,"\n C: ",c)

# Probar programa con la secuencias AGCTTTTCATTC
# debe dar: A: 2    T: 6    C: 3   G: 1