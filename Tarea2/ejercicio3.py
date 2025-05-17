
n=int(input("Ingrese un numero: "))
cont_div=0
p=1

if n>1:
    while p<=n:
        if n%p==0:
            cont_div+=1
        p+=1

if cont_div==2:
    print(f"{n} es un numero primo")
else:
    print(f"{n} no es un numero primo")
    