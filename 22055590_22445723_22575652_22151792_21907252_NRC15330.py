#Integrantes:
# Carla Campos - 22.055.590-9
# Vicente Duarte - 22.151.792-K
# Antonia Hernández - 22.475.723-5
# Lukas Ortiz - 21.907.252-K
# Antonia Roca - 22.575.652-K

matriz = []
valor_m3 = 0
deptos = 0
meses = 0

while True:
    print("\nSISTEMA DE PLANIFICACIÓN DE CONSUMO DE AGUA")
    print("1. Generar plan de consumo")
    print("2. Ingresar cantidad de m³ consumidos")
    print("3. Visualizar pago total por departamento")
    print("4. Visualizar pago total por mes")
    print("5. Salir del programa")
    
    opcion = input("Seleccione su opción: ")

    if opcion == "1":
        deptos = int(input("Ingrese número de departamentos: "))
        meses = int(input("Ingrese número de meses de consumo: "))
        
        matriz = []
        for i in range(deptos):
            fila = []
            for j in range(meses):
                fila.append(0)
            matriz.append(fila)
        
        print("\nPlan de consumo")
        print("**"*18)
        
        # Imprimir encabezado de meses
        encabezado = "                " 
        for m in range(meses):
            encabezado = encabezado + "    " + str(m + 1)
        print(encabezado)
        
        # Imprimir filas con el nombre del departamento
        for i in range(deptos):
            linea = "Departamento " + str(i + 1) + "    "
            for j in range(meses):
                linea = linea + str(matriz[i][j]) + "     "
            print(linea)
        print("**"*18)
     elif=="2":
         #Se deve cumplir primero la opcion anterior para tener de los datos de deptos, meses y matriz.
         if len(matriz)==0:
             print("Se necesita rellenar la opción 1.")
             continue
#Ahora le entregamos un valor a la variable de valor_m3
    valor_m3=float(input("Ingrese cantidad de m³ consumidos este mes:"))
#ciclos de for para recorrer los departamentos y los meses
    for i in range (deptos):
        print("Departamento"+ (1+))
