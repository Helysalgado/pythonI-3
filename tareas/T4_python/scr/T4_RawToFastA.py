'''
NAME
    T4_RawToFastA   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa crea un archivo fasta a partir de la secuencia de DNA en formato .txt
    

'''
# ===========================================================================
# =                            main
# ===========================================================================


#pedrir archivo con la secuendia de DNA al usuario y el nombre de la secuencia de DNA
print("==================================== \n  Ingrese el nombre o la ruta de un archivo tipo .txt con una secuencia de DNA: ")
archivo_original= input()
print("\n Ingrese el nombre de la secuencia de DNA:  ")
nombre_seq= input()

#abrir y leer archivo
archivo_abierto= open(archivo_original) 
dna_contenido= archivo_abierto.read()

#quitar el caracter de nueva linea
dna_contenido=dna_contenido.rstrip("\n")

#crear archivo fasta
archivo_fasta=open("dna.fasta" , "w")

#escribir el archivo fasta
archivo_fasta.write(">"+ nombre_seq + "\n" + dna_contenido)
print("\n\n Se creo el archivo fasta dna.fasta. ")

#cerrar archivo
archivo_fasta.close()