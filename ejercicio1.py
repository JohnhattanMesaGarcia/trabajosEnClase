# Elabore un programa para la Universidad de Florida que calcule los primeros 100 números de la siguiente serie 5, 8, 13, 21, ... sin mostrar el 13, y muestre la lista del resultado de los números.

a = 5
b = 8
series = []

for _ in range(100):
    if a != 13:  
        series.append(a)
  
    a, b = b, a + b

print(series)