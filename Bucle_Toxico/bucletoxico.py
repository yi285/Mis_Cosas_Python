pareja = input("Me quieres? ").upper()

while pareja not in ["SI","NO"]:
    print("Por favor, indica si me quieres")
    pareja = input("Me quieres? ").upper()

if pareja == "SI":
    amigos = input("Quedas con tus amigos? ").upper()
    while amigos not in ["SI","NO"]:
        print("Por favor, indica si quedas con tus amigos")
        amigos = input("Quedas con tus amigos? ").upper()
        if amigos == "SI":
            print("Lo sabia, quedas sin decirme nada.")
        else:
            print("Ese es mi chico")
else:
    print("Lo sabia, es que eres un desgraciado")
    tiempo = input("Hace cuanto tiempo que sientes que no me quieres? ")
    print("Ojala te hagan lo mismo")



