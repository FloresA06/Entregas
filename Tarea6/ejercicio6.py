
def reg_temps():
    dias_semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    temperaturas=list()
    print("Ingrese las temperaturas diarias de la semana: ")
    for dia in dias_semana:
        temp=float(input(f"{dia}: "))
        temperaturas.append((dia, temp))
    return temperaturas

def calc_prom(temperaturas):
    total=sum(temp for _, temp in temperaturas)
    promedio=total/len(temperaturas)
    return promedio

def print_temps(temperaturas):
    print("\nTemperaturas registradas:")
    for dia, temp in temperaturas:
        print(f"{dia}: {temp}°C")

temps_semana=reg_temps()
print_temps(temps_semana)

promedio=calc_prom(temps_semana)
print(f"\nLa temperatura promedio de la semana es: {promedio:.2f}°C")
