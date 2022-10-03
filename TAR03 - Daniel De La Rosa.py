#Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios. Calcule el precio a pagar de acuerdo con la siguiente tabla
# Daniel Arturo De La Rosa 21-1799

#Se nombran las variables las cuales utilizaremos segun el mandato
Residencial ="R"

Comercial ="C"

Instalacion ="I"

# Se asignan las variables para poder introducir por teclado
kwhconsumido = float(input("Cantidad de kwh consumido: "))

tipoinstalacion = input("Introduzca el tipo de instalacion: ")


#Despues se asignan las condiciones correspondientes
if tipoinstalacion == 'R':
    if kwhconsumido <= 500:
        precio = 550
    else:
        precio = 850

elif tipoinstalacion == 'C':
    if kwhconsumido < 1000:
        precio = 1300
    else:
        precio = 2500

elif tipoinstalacion == 'I':
    if kwhconsumido < 5000:
        precio = 3800
    
    else:
        precio = 4200

if precio:
    print("Precio = ", precio)