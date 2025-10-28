libreria = [ "Romantico", "Terror", "Fantasia", "Ciencia Ficcion", "Misterio"]
print("Bienvenido a la librería virtual. Aquí tienes una lista de géneros disponibles:")

for genero in libreria:
    print(f"- {genero}")

eleccion = input("Por favor, elige un género de la lista anterior: ").strip()

while eleccion not in libreria:
    print("Lo siento, ese género no está disponible. Por favor, elige un género válido de la lista.")
    eleccion = input("Por favor, elige un género de la lista anterior: ").strip()

if eleccion =="Romantico":
    libro_romatico  =["'Orgullo y Prejuicio' de Jane Austen", "'Bajo la misma estrella' de John Green", "'El cuaderno de Noah' de Nicholas Sparks"]
    print("Aquí tienes algunos libros del género Romántico:")
    

    for libro in libro_romatico:
        print(f" {libro}")

elif eleccion =="Terror":
    libro_terror = ["'It' de Stephen King", "'El exorcista' de William Peter Blatty", "'Drácula' de Bram Stoker"]
    print("Aquí tienes algunos libros del género Terror:")
    precios = []
    for libro in libro_terror:
        print(f" {libro}")
    
elif eleccion =="Fantasia":
    libro_fantasia = ["'El señor de los anillos' de J.R.R. Tolkien", "'Harry Potter y la piedra filosofal' de J.K. Rowling", "'El nombre del viento' de Patrick Rothfuss"]
    print("Aquí tienes algunos libros del género Fantasía:")

    for libro in libro_fantasia:
        print(f" {libro}")

elif eleccion =="Ciencia Ficcion":
    print("Aquí tienes algunos libros del género Ciencia Ficción:")
    libro_cienciaficcion = ["'Dune' de Frank Herbert", "'Neuromante' de William Gibson", "'Fundación' de Isaac Asimov"]
    
    for libro in libro_cienciaficcion:
        print(f" {libro}")

elif eleccion =="Misterio":

    libro_misterio = ["'El código Da Vinci' de Dan Brown", "'Asesinato en el Orient Express' de Agatha Christie", "'La chica del tren' de Paula Hawkins"]
    print("Aquí tienes algunos libros del género Misterio:")

    for libro in libro_misterio:
        print(f" {libro}")
    
#ponerle precio a los libros y poder comprarlos
