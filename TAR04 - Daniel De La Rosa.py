# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
# Daniel Arturo De La Rosa 21-1799


# Primero se asigna la variable en donde ira la cantidad de palabras que habra en la lista

CantidadPalabras = int(input("¿Que cantidad de palabras contiene la lista? "))


# Luego ponemos una condicion para verificar las cantidades de listas
if CantidadPalabras < 1:
    print("Error, no es la cantidad correcta")
else:
    ListaPalabras = []

# Luego asignamos la condicion for para poder añadir palabras a la lista que estamos creando

    for a in range(CantidadPalabras):
        Palabras = input(f"Introduzca la palabra que desea poner {a+1}: ")
        ListaPalabras += [Palabras]


# Luego de poner la palabra que deseamos pues le damos un print diciendo que palabra es
    print("La palabra añadida es: ", ListaPalabras)


# Asignamos otra variable que permitira buscar la palabra que deseemos

BuscarPalabra = input("Introduzca la palabra que desea buscar: ")

# Asignamos una variable que sera el contador de palabras

ContadorPalabras = 0

# Aplicamos las condiciones para cuando encontremos una palabra en una lista o no logremos encontrarla

for a in ListaPalabras:
    if a == BuscarPalabra:
        ContadorPalabras += 1
    if ContadorPalabras == 0:
        print(
            f"La palabra que asigno como '{BuscarPalabra}' esta en la lista!")
    elif ContadorPalabras == 1:
        print(
            f"La palabra que asigno como '{BuscarPalabra}' no se encuentra en la lista ):")
    else:
        print(
            f"La palabra que asigno como '{BuscarPalabra}' aparece {ContadorPalabras} veces en esta lista")


# FIN :)
