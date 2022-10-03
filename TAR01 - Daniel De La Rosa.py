
# Primero se asignan las variables y los numeros que utilizaremos

numero1 = int(input("Ingrese un numero:  "))
numero2 = int(input("Ingrese otro numero: "))

# Asignamos una variable para seleccionar la operacion que deseemos realizar

operacion = input("¿Que operacion aritmetica desea realizar, suma, resta, multiplicacion o division? ") 


# Luego le asignamos a la variable que operacion realizara al seleccionar cualquiera de las opciones

if operacion == "suma":
    print("El resultado de la suma es:",numero1+numero2)

elif operacion == "resta":
    print("El resultado de la resta es:",numero1-numero2)

elif operacion == "multiplicacion":
    print("El resultado de la multiplicacion es:",numero1*numero2)

elif operacion == "division":
    print("El resultado de la division es:",numero1/numero2)
    
    