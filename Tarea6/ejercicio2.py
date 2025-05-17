
def reg_calificaciones():
    calif_estudiantes=dict()
    n=int(input("Ingrese el numero de estudiantes a registrar: "))
    for i in range(n):
        nombre=input(f"\nIngrese el nombre del estudiante #{i + 1}: ").strip()
        cant_cal=int(input(f"Ingrese el numero de calificaciones para {nombre}: "))
        calificaciones=list()
        for j in range(cant_cal):
            cal=float(input(f"Ingrese la calificación #{j + 1} de {nombre}: "))
            calificaciones.append(cal)
        calif_estudiantes[nombre] = calificaciones
    return calif_estudiantes

def mostrar_notas(cal_estudiantes):
    print("\nNotas estudiantes:")
    for nombre, calificaciones in cal_estudiantes.items():
        promedio=sum(calificaciones)/len(calificaciones)
        print(f"{nombre}: {calificaciones}")
        print(f"Promedio: {promedio:.2f}")

cals=reg_calificaciones()
mostrar_notas(cals)
