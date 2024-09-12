# Elabore un programa para un Hospital que determine, y muestre el nivel de Leucemia de 803 pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia; si esta entre 11 y 40, nivel bajo de Leucemia; si esta entre 40 y 69, nivel moderado de Leucemia, si esta entre 70 y 100, nivel grave de Leucemia.

# Listas para almacenar las clasificaciones de los pacientes
sin_leucemia = []
nivel_bajo = []
nivel_moderado = []
nivel_grave = []

# Pedir el puntaje de leucemia para 803 pacientes
for i in range(3):
    puntaje = int(input(f"Ingrese el puntaje del paciente {i + 1}: "))
    

    # Clasificar el nivel de leucemia según el puntaje
    if puntaje < 10:
        sin_leucemia.append(puntaje)           
    elif 11 <= puntaje <= 40:
        nivel_bajo.append(puntaje)
    elif 41 <= puntaje <= 69:
        nivel_moderado.append(puntaje)
    elif 70 <= puntaje <= 100:
        nivel_grave.append(puntaje)

# Mostrar el listado de clasificaciones
print("\nPacientes sin Leucemia:")
# print(len(sin_leucemia), "\nPuntaje por paciente", str(sin_leucemia))
print(len(sin_leucemia), "\nPuntaje por paciente", str(sin_leucemia))

print("\nPacientes con nivel bajo de Leucemia:")
print(len(nivel_bajo))

print("\nPacientes con nivel moderado de Leucemia:")
print(len(nivel_moderado))

print("\nPacientes con nivel grave de Leucemia:")
print(len(nivel_grave))