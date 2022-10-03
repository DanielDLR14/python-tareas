#Escribir un programa que capture una lista de caracteres.

#Indicaciones:

    #La longitud de la lista debe ser dinámica (capturada).
    #Si el usuario ingresa un dígito (cualquiera), se debe terminar la ejecución del programa con el mensaje: "Lo sentimos, no se permiten dígitos.", y mostrar la lista con los caracteres que se lograron capturar (en caso de que se hayan capturado).
    #Si el usuario ingresa una palabra, se debe de omitir y continuar con el bucle.
    #Mostra la lista con los caracteres capturados y el total.

#Daniel Arturo De La Rosa 21-1799


# Se ccra una variable en donde se almacenara La caputra de la lista
CapturaLista = []
# Asignamosuna varible en donde iran llos caracteres
Caracterlimite = int(input("Porfavor inserte los caracteres que desee"))


# se asignan la un while donde se pondra que no se aceptan digitos sino solo caracteres
while len (CapturaLista) != Caracterlimite:



# se asigna una variable en donde se almacenara los caracteres o el caracter
    Letras = input("Porfavor inserte un caracter: ")
    if Letras == "0" or Letras == "1" or Letras == "2" or Letras == "3" or Letras == "4" or Letras == "5" or Letras == "6" or Letras == "7" or Letras == "8" or Letras == "9":
        print("Error no se aceptan digitos") 
# se asigna un brake para detener el proceso   
        break
    elif len(Letras) > 1:
# si al momento de inserter x cosa y sale caracter tipo letra pues se continuara con el proceso 
        continue
    else: 
        CapturaLista.append(Letras)
    print(CapturaLista)
    print(len(CapturaLista))
