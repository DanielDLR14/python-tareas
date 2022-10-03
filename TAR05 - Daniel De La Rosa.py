#Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor
#Daniel Arturo De La Rosa 21-1799

# Creamos la lista que vamos a utilizar

NumerosLista = []

# Ponemos la cantidad de numeros que se van a utilizar luego poder introducir por teclado
for a in range(8):
    NumerosLista.append(int(input("Introduzca el numero ganador: ")))  

# Lo siguiente sera poner un sort el cual modifica la lista

NumerosLista.sort()

# Lo siguiente sera poner un print en donde saldran los numeros ganadores ordenadamente

print(*NumerosLista, sep = ", ")

print(f'Números ganadores: {", ".join(str(x) for x in NumerosLista)}')

print("Felicidadess!, estos son los numeros ganadores: {} {} {} {} {} {} {} {}".format(*NumerosLista))
