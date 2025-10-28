print("----Informacion----")
nombre = input("Escribe tu nombre: ").lower()
apellido = input("Escribe tu apellido: ").lower()
telefono = int(input("Escribe tu telefono: "))

opciones = ["login","singin"]

print("----Opciones----")
for opcion in opciones:
    print(opcion)
eleccion = input("Elije una opcion: ").lower()

while eleccion not in ["login","singin"]:
    print("Introduce una de las dos opciones validas")
    eleccion = input("\nElije una opcion: ").lower()

if eleccion == "login":
    usuario = input("Escribe tu usuario: ")
    contra = input("Escribe tu contraseña: ")
    print("completed")
elif eleccion == "singin":
    usuario = input("Escribe tu usuario: ")
    contra = input("Escribe tu contraseña: ")
    print("completed")

gua_usuario = usuario
gua_contra = contra

