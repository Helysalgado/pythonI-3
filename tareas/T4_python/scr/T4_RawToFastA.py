'''
NAME
    T4_RawToFastA   

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa crea un archivo fasta a partir de la secuencia de DNA en formato .txt
    
        
USAGE
    % py T4_RawToFastA.py
    
'''
# ===========================================================================
# =                            main
# ===========================================================================


#pedir archivo con la secuendia de DNA 
print("==================================== \n  Ingrese el nombre o la ruta de un archivo tipo .txt con una secuencia de DNA: ")
nombre_archivo_entrada = input()

# pedir el nombre de la secuencia de DNA -identificador
print("\n Ingrese el nombre de la secuencia de DNA:  ")
nombre_seq = input()

#abrir y leer archivo de secuencia
archivo_entrada = open(nombre_archivo_entrada) 
dna_seq = archivo_entrada.read()
dna_seq = dna_seq.rstrip("\n")
archivo_entrada.close()

#crear archivo fasta
archivo_fasta=open("dna.fasta" , "w")

#escribir el archivo fasta
archivo_fasta.write(">" + nombre_seq + "\n" + dna_seq)
print("\n\n Se creo el archivo fasta dna.fasta")

#cerrar archivo
archivo_fasta.close()
