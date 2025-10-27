animales = ["lobos","vacas","cerdos"]

for animal in animales:
    print(animal)

def loboshop():
    print("Los lobos valen 21€")
    cantidad_lobos = int(input("Cuantos quieres comprar? "))
    print("El precio total de la compra es de", cantidad_lobos*21, "€")

def vacasshop():
    print("Las vacas valen 24€")
    cantidad_vacas = int(input("Cuantos quieres comprar? "))
    print("El precio total de la compra es de", cantidad_vacas*24, "€")

def cerdosshop():
    print("Los cerdos valen 34€")
    cantidad_cerdos = int(input("Cuantos quieres comprar? "))
    print("El precio total de la compra es de", cantidad_cerdos*34, "€")
    
pedido = input("Dinos que animal quieres adoptar: ").lower()

while pedido not in ["lobos","vacas","cerdos"]:
    print("Introduce un animal valido")
    pedido = input("Dinos que animal quieres adoptar: ").lower()

if pedido == "lobos":
    loboshop()
elif pedido =="cerdos":
    vacasshop()
else:
    cerdosshop()
    