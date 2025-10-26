import Constantes

print("----Fruteria----")
print("La cantidad de manzana es de: " , Constantes.manzanas,  " a un precio de", Constantes.precma)
print("La cantidad de peras es de: " , Constantes.peras,  " a un precio de", Constantes.precpe)
print("La cantidad de limones es de: " , Constantes.limones,  " a un precio de", Constantes.precli)
print("La cantidad de naranjas es de: ", Constantes.naranjas,  " a un precio de", Constantes.precna)

elije = input("Elije la fruta: ").lower()
while elije not in ["manzanas","peras","limones","naranjas"]:
    print("Ingresa una fruta valida")
    elije = input("Elije la fruta: ").lower()


if elije == "manzanas":
    cantidad = int(input("¿Cuantas manzanas quieres? "))
    precio = cantidad*Constantes.precma
    Constantes.manzanas = Constantes.manzanas -cantidad
    print("Compras", cantidad, "manzanas", "a", Constantes.precma, "la unidad =", precio )
elif elije == "peras":
    cantidad = int(input("¿Cuantas peras quieres? "))
    precio = cantidad*Constantes.precpe
    Constantes.peras = Constantes.peras -cantidad
    print("Compras", cantidad, "peras", "a", Constantes.precpe, "la unidad =", precio )
elif elije == "limones":
    cantidad = int(input("¿Cuantos limones quieres? "))
    precio = cantidad*Constantes.precli
    Constantes.limones = Constantes.limones -cantidad
    print("Compras", cantidad, "limones", "a", Constantes.precli, "la unidad =", precio )
elif elije == "naranjas":
    cantidad = int(input("¿Cuantas naranjas quieres? "))
    precio = cantidad*Constantes.precna
    Constantes.naranjas = Constantes.naranjas -cantidad
    print("Compras", cantidad, "naranjas", "a", Constantes.precna, "la unidad =", precio )