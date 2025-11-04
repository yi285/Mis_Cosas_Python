
def saludar(nombre = "desconocido"):
    print(f"(Dentro de la función) El nombre es: {nombre}") 
    return nombre

nombre = input("Dime tu nombre: ")
nombre = saludar(nombre) 

saludo = (f"hola {nombre}")
print(saludo)

