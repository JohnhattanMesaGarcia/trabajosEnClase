# Elabore un programa para la facultad de Ingeniería que pida 400 números e indique si ese número es par o impar; me muestre un listado y me indique cuantos son pares y cuantos son impares.

# Listas para almacenar los números pares e impares
pares = []
impares = []

# Pedir 400 números al usuario
for i in range(4):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    
    # Validar si es par o impar
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Mostrar el listado de números pares e impares
print("\nListado de números pares:")
for par in pares:
    print(par)

print("\nListado de números impares:")
for impar in impares:
    print(impar)

# Mostrar la cantidad de números pares e impares
print(f"\nTotal de números pares: {len(pares)}")
print(f"Total de números impares: {len(impares)}")