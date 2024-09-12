# Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable, registrando un puntaje que se clasifica de la siguiente forma si tiene 2 puntos está con un funcionamiento defectuoso, si tiene 3 puntos el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo


# Listas para almacenar las clasificaciones de las cabinas
defectuoso = []
moderado = []
optimo = []

# Registrar el puntaje para las 407 cabinas
for i in range(4):
    puntaje = int(input(f"Ingrese el puntaje de la cabina {i + 1} (2, 3, o 4): "))

    # Clasificar el funcionamiento de la cabina según el puntaje
    if puntaje == 2:
        defectuoso.append(puntaje)
    elif puntaje == 3:
        moderado.append(puntaje)
    elif puntaje == 4:
        optimo.append(puntaje)
    else:
        print("Puntaje no válido. Ingrese un puntaje de 2, 3, o 4.")

# Mostrar el listado de clasificaciones
print("\nCabinas con funcionamiento defectuoso:")
print(len(defectuoso))

print("\nCabinas con funcionamiento moderado:")
print(len(moderado))

print("\nCabinas con funcionamiento óptimo:")
print(len(optimo))