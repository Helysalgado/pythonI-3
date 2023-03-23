# Tarea 2: Comparar Versiones y restaurar Archivos

### Camila Villazón Soto Innes

## Introducción
Github es una plataforma que permite almacenar, llevar un seguimiento y colaborar en proyectos de software. 
En conjunto con git, se abre la posibilidad de subir y bajar los cambios que se realizan a los archivos, permitiendo trabajar desde cualquier parte.

En esta tarea se refuerzan los comandos:
`git diff` para observar la diferencia entre dos versiones de un archivo guardadas en el repositorio.
`git checkout` para restaurar una versión de un archivo.

## Problema
Necesitamos probar que nuestro programa reverse-complement trabaja correctamente con 2 secuencias. Haz lo siguiente:

1. En el archivo de DNA que ya tienes creado, agrega la secuencia del gene araB en formato Fasta.
2. Sube los cambios a git y confirmalos.
3. Simula que el gene araC ha sufrido 3 mutaciones en su secuencia, cambia 3 nucleótidos.
4. Agrega los cambios a git y confirmalos.
5. Haz las siguientes comparaciones del archivo: última vs penútima y última vs antepenúltima.
6. Restaura la versión del archivo que no tiene las mutaciones.
7. En un reporte en markdown indica lo que hiciste y los comandos que ejecutaste.

## Métodos y Resultados
````
 #Ingresar al repositorio pythonI en la carpeta 
 #project/reverse_complement
 #editar archivo araC_coli.txt
 #añadir secuencia araB con:

 nano araC_coli.txt

 #Subir cambios y confirmar
 git add data/araC_coli.txt
 git commit -m "se añadio secuencia de araB"
 
 #confirmar que se guardó el cambio
 git log --oneline
 
 #simular 3 mutaciones en araC
 #Subir cambios y confirmar
 git add data/araC_coli.txt
 git commit -m "se cambiaron 3 nt de la secuencia de araC"
 
 #comparar última versión con la penúltima
  git diff head~1 data/araC_coli.txt
 #muestra la diferencia entre los nucleotidos modificados
  
 #comparar la última con la antepenúltima
 git diff head~2 data/araC_coli.txt
 #muestra los nucleotidos mutados y la adicion de araB
 
 #restaurar versión sin mutaciones usando el ID del commit
  git checkout 3a8a24c data/araC_coli.txt
  
 #guardar cambios
 git commit -m "restauracion de secuencia araC sin mutaciones"
 
 #subir cambios a github
 git push origin master
 
 
````

## Conclusión
Se reforzaron los comandos para comparar versiones y restaurarlas. Estos dos comandos deben ir de la mano, ya que permite ver las diferencias entre las versiones de un archivo que se han guardado, de tal forma que, en el caso de un código, se puede ver que cambio hizo que dejara de funcionar. Una vez encontrado, se puede restaurar esa version para seguir trabajando con ella.


## Referencias

Juviler, J. (2022). What is GitHub? (And what is it used for). https://blog.hubspot.com/website/what-is-github-used-for?hubs_content=blog.hubspot.com%2Fwebsite%2Fwhat-is-github-used-for&hubs_content-cta=What%20is%20GitHub%3F
