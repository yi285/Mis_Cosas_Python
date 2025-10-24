producto = (input("Ingrese el nombre del producto: ")).lower()
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad a comprar: "))
tipoiva = [general, reducido, superreducido] = [21, 10, 4]
iva = float(input("Ingrese el porcentaje de IVA (general 21%, reducido 10%, superreducido 4%): "))
while iva not in [21, 10, 4]:
    print("Por favor, ingrese un valor de IVA válido: 21, 10 o 4.")
    iva = float(input("Ingrese el porcentaje de IVA (general 21%, reducido 10%, superreducido 4%): "))

descuento = float(input("Ingrese el porcentaje de descuento (sin el símbolo %): "))

print(f"Quieres que te calcule el valor de {producto} en la cantidad de {cantidad} al precio de {precio} con un descuento del {descuento}% y un IVA del {iva}%? ")
Opcion = input("Si / No: ").lower()

if Opcion == "si":
    precio_total = precio * cantidad
    valor_iva = precio_total * (iva / 100)
    precio_con_iva = precio_total + valor_iva
    valor_descuento = precio_total * (descuento / 100)
    precio_final = precio_total - valor_descuento

    print("Quieres toda la informacion del calculo? ")
    Opcion2 = input("Si / No: ").lower()
    
    if Opcion2 == "si":
        print(f"El precio total de comprar {cantidad} unidades de {producto} al {precio} sin descuento y sin IVA es: {precio} x {cantidad} = {precio_total:.2f}€")
        print(f"El precio total con IVA es: {precio_total:.2f} + {valor_iva:.2f} = {precio_con_iva:.2f}€")
        print(f"El precio total con descuento es: {precio_total:.2f} - {valor_descuento:.2f} = {precio_final:.2f}€")
        print(f"El precio final a pagar por {cantidad} unidades de {producto} es: {precio_final:.2f}€")
        print("Gracias por usar el calculador de precios!")
    elif Opcion2 == "no":
        print(f"El precio final a pagar por {cantidad} unidades de {producto} es: {precio_final:.2f}€")
        print("Gracias por usar el calculador de precios!")

elif Opcion == "no":
    print("Gracias por usar el calculador de precios!")
