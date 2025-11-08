import random

#Creas las variables
veces = 1000
cero_diez = 0
diez_veinte = 0
veinte_treinta = 0
treinta_cuarenta = 0
cuarenta_cincuenta = 0
cincuenta_sesenta = 0
sesenta_setenta = 0
setenta_ochenta = 0
ochenta_noventa = 0
noventa_cien = 0

#carrera de caballos
while veces != 0:
    numran = random.randint(0,100)
    veces -= 1
    if 0 <= numran < 10:
        cero_diez += 1
    elif 10 <= numran < 20:
        diez_veinte += 1
    elif 20 <= numran < 30:
        veinte_treinta += 1
    elif 30 <= numran < 40:
        treinta_cuarenta += 1
    elif 40 <= numran < 50:
        cuarenta_cincuenta += 1
    elif 50 <= numran < 60:
        cincuenta_sesenta += 1
    elif 60 <= numran < 70:
        sesenta_setenta += 1
    elif 70 <= numran < 80:
        setenta_ochenta += 1
    elif 80 <= numran < 90:
        ochenta_noventa += 1
    elif 90 <= numran <= 100:
        noventa_cien += 1


#imprimes la  carrera de caballos
como = input("Como quieres el resultado en lineas o plano? (L/P/D)").upper()

while como not in ["L", "P", "D"]:
    print("introduce una opcion valida")
    como = input("Como quieres el resultado en lineas o plano? (L/P/D)").upper()

if como == "P":
    print("---Resultado en plano---")
    print("CABALLO 1  :", cero_diez)
    print("CABALLO 2  :", diez_veinte)
    print("CABALLO 3  :", veinte_treinta)
    print("CABALLO 4  :", treinta_cuarenta)
    print("CABALLO 5  :", cuarenta_cincuenta)
    print("CABALLO 6  :", cincuenta_sesenta)
    print("CABALLO 7  :", sesenta_setenta)
    print("CABALLO 8  :", setenta_ochenta)
    print("CABALLO 9  :", ochenta_noventa)
    print("CABALLO 10 :", noventa_cien)
elif como == "L":
    print("---Resultado en lineas---")
    print("CABALLO 1  :", "-" * cero_diez, cero_diez)
    print("CABALLO 2  :", "-" * diez_veinte, diez_veinte)
    print("CABALLO 3  :", "-" * veinte_treinta, veinte_treinta)
    print("CABALLO 4  :", "-" * treinta_cuarenta, treinta_cuarenta)
    print("CABALLO 5  :", "-" * cuarenta_cincuenta, cuarenta_cincuenta)
    print("CABALLO 6  :", "-" * cincuenta_sesenta, cincuenta_sesenta)
    print("CABALLO 7  :", "-" * sesenta_setenta, sesenta_setenta)
    print("CABALLO 8  :", "-" * setenta_ochenta, setenta_ochenta)
    print("CABALLO 9  :", "-" * ochenta_noventa, ochenta_noventa)
    print("CABALLO 10 :", "-" * noventa_cien, noventa_cien)    
elif como == "D":
    print("---Resultado Directo---")
    # Creamos una lista con todos los contadores
    caballos = [
        cero_diez, diez_veinte, veinte_treinta, treinta_cuarenta,
        cuarenta_cincuenta, cincuenta_sesenta, sesenta_setenta,
        setenta_ochenta, ochenta_noventa, noventa_cien
    ]

    # Buscamos el mayor
    max_valor = max(caballos)
    indice_ganador = caballos.index(max_valor)  # devuelve el índice del primer máximo

    print(f"El caballo ganador es CABALLO{indice_ganador   + 1} con {max_valor} pasos")
