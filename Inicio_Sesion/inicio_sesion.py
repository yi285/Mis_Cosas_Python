print("----Informacion----")
nombre = input("\nEscribe tu nombre: ").lower()
apellido = input("Escribe tu apellido: ").lower()
telefono = int(input("Escribe tu telefono: "))

opciones = ["login","singin"]

print("----Opciones----")
for opcion in opciones:
    print(opcion)
eleccion = input("Elije una opcion: ").lower()

while eleccion not in ["login","singin"]:
    print("\nIntroduce una de las dos opciones validas")
    eleccion = input("\nElije una opcion: ").lower()

if eleccion == "login":
    usuario = input("\nEscribe tu usuario: ")
    contra = input("\nEscribe tu contraseña: ")
    print("completed")
elif eleccion == "singin":
    usuario = input("\nEscribe tu usuario: ")
    contra = input("\nEscribe tu contraseña: ")
    print("completed")

gua_usuario = usuario
gua_contra = contra

