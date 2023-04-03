'''
NAME
    T1_SecuenciaRNA    

AUTHOR
      Camila Villazon Soto Innes  

DESCRIPTION
        Este programa regresa la posición del codón inicial y donde termina el codón de término de una secuencia
        de DNA.     

'''
# ===========================================================================
# =                            main
# ===========================================================================

print("==================================================== \n\n Este programa indica la posicion del codón de inicio,"+
      "\n asi como la secuencia entre el codon de inicio y el de paro\n")


# secuencia de DNA
dna= 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
print("La secuencia de DNA implementada es: " + dna)

# codon de inicio complementario a ATG
inicio_codon= 'TAC'

# almacenar posicion del codon de inicio
pos_inicio_codon= dna.find(inicio_codon)

# imprimir posicion del codon de inicio
print('\n El codon de inicio esta en la posicion: ', pos_inicio_codon)

# codon de paro
paro_codon= 'ATT'

# almacenar posicion del codon de paro
pos_paro_codon= dna.find(paro_codon)

# imprimir del codon de inicio hasta donde termina el codon de paro
print('\n El fragmento que sera RNA es: ', dna [pos_inicio_codon:pos_paro_codon])



