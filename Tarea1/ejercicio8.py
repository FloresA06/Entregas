
año=int(input("Ingrese un año a analizar: "))

if año%4==0 and año%100!=0:
    print(f"{año} es bisiesto")
elif año%400==0 and año%100==0:
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")
