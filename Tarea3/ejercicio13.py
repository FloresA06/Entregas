
año=int(input("Ingrese un año a analizar: "))

def ver_bisiesto(año):
    if año%4==0 and año%100!=0:
        print(f"{año} es bisiesto")
    elif año%400==0 and año%100==0:
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")

ver_bisiesto(año)
