#daniel arturo 21-1799

#primero importamos la libreria math
import math

#luego asignamos las variables en donde van a estar los numeros

VarNum1 = int(input("Inserte un numero deseado"))
VarNum2 = int(input("Inserte otro numero deseado"))

# luego se realizan las declaraciones para las operaciones

NumExponente1 = VarNum1**2
NumExponente2 = VarNum2**2

# se asigna la delcarcion de suma en las potencias

ExponenteSuma = NumExponente1+NumExponente2

# ya como siguiente paso ponemos como seran los resultados de las operaciones

print("El numero 1 su valor al cuadrado es: ", NumExponente1)
print("El numero 2 su valor al cuadrado es: ", NumExponente2)

# despues como ultimo paso pues se pone la suma de lso totales y la raiz cuadrada

print ("La suma tiene como resultado: ", ExponenteSuma)
print ("La raiz cuadrada del numero es:", math.sqrt(ExponenteSuma))

