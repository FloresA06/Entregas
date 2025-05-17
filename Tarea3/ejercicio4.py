
n = int(input("Numero del que se desea obtener el factorial: "))

def factorial(n):
    if n>=0:
        cont=1
        fact=1
        while cont<=n:
            fact*=cont
            cont+=1
        print(f"El factorial de {n} es {fact}")

factorial(n)
