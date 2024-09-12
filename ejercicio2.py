# Elabore un programa para el Éxito que determine el salario de los 1897 empleados de su compañía, teniendo en cuenta las comisiones y la seguridad social que debe pagar, e imprima el listado de la información. 

# Definición de parámetros
empleados = []

for i in range(0, 3):  
    salario_base = int(input("Ingrese su salario basico: "))
    comision_porcentaje = float(input("Ingrese su salario de comision: "))
    seguridad_social_porcentaje = float(input("Ingrese porcentaje de segudidad social: "))
    print("-" * 40)

    comision = salario_base * comision_porcentaje
    salario_total = salario_base + comision
    deduccion_seguridad_social = salario_total * seguridad_social_porcentaje
    salario_neto = salario_total - deduccion_seguridad_social
    
    # Agregar la información del empleado a la lista
    empleados.append({
        "Empleado ID": i,
        "Salario Base": salario_base,
        "Comisión": comision,
        "Salario Total": salario_total,
        "Deducción Seguridad Social": deduccion_seguridad_social,
        "Salario Neto": salario_neto
    })

# Imprimo la info de los empleados
for empleado in empleados:
    print(f"Empleado ID: {empleado['Empleado ID']}")
    print(f"Salario Base: {empleado['Salario Base']} COP")
    print(f"Comisión: {empleado['Comisión']} COP")
    print(f"Salario Total: {empleado['Salario Total']} COP")
    print(f"Deducción Seguridad Social: {empleado['Deducción Seguridad Social']} COP")
    print(f"Salario Neto: {empleado['Salario Neto']} COP")
    print("-" * 40)