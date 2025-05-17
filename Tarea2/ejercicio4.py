
n=int(input("Ingrese un numero entre 1 y 50: "))
a=0
b=1
c=0

if n>=1 and n<51:
    print(a,end=" ")
    print(b,end=" ")
    for num in range(0,n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
else:
    print("Su numero tiene que estar entre 1 y 50")
    