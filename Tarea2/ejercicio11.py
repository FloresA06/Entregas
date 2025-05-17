
num=int(input("Ingrese un numero: "))
suma=0

while num>0:
    suma+=num%10
    num=num//10

print(f"La suma de sus digitos es: {suma}")
