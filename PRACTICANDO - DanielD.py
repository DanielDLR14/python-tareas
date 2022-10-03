Residencial = "R"
Comercial = "C"
Industrial = "I"

KwhConsumidos = int(input("Introduzca la cantidad de kwh consumidos: "))
tipoinstalacion = input("Introduzca el tipo de instalacion: ")

if tipoinstalacion == "R":
    if KwhConsumidos >= 500:
        precio = 550
    else:
        precio = 850

if tipoinstalacion == "C":
    if KwhConsumidos >= 1000:
        precio = 1300
    else:
        precio = 2500

if tipoinstalacion == "I":
    if KwhConsumidos >= 5000:
        precio = 3800
    else:
        precio = 4200

if precio:
    print("Precio = ", precio)