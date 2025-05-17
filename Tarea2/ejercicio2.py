
num=int(input("Ingrese un numero cualquiera entre 1 y 20: "))
f=num-1

if num>=1 and num<=20:
    while f!=1:
        num*=f
        f-=1
    print(f"El factorial del numero ingresado es {num}")
else:
    print("Su numero tiene que estar entre 1 y 20") 
