
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

def mcd(n1,n2):
    if n2==0:
        return n1
    else:
        return mcd(n2,n1%n2)
    
res=f"El maximo comun divisor de {num1} y {num2} es:"
print(res,mcd(num1,num2))
