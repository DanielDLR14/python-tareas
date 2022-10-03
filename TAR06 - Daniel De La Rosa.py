#Realizar un programa el cual determine el tiempo en meses para pagar un préstamo.
#Indicaciones:
# El monto del préstamo debe ser solicitado.
# Se debe solicitar la cantidad mensual que se desea pagar.
# Mediante el uso de while, determinar los meses (total) en los que se completará el pago del préstamo.

# Daniel De La Rosa 21-1799



# Primero asignamos una variable con la cantidad de meses
MesesPrestamo = 12

# Asignamos una variable donde se introducira la cantidad que deseemos tomar como prestamo
PrestamoMonto = float(input("¿De cuanto desea tomar su prestamo? "))

print("De acuerdo, su prestamo tomado fue de: $",PrestamoMonto)

# Aignamos otra variable en donde estara almacenada la cantidad que deseemos pagar el prestamo
CantidadMensual = float(input("¿Que cantidad desea pagar?: "))
print(f"De acuerdo, usted pagara {CantidadMensual} al mes.")

# Usamos un ciclo while en donde se calculara el monto del prestamo
while PrestamoMonto >= 1 :
# Finalmente nos dara un print con los calculos totales y en donde se vera la cantidad de meses en que tomara poder pagar
    print(f"El total de meses que usted completara el pago es de {PrestamoMonto/CantidadMensual:.1f} meses")
    break



    
