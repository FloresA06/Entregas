
x=float(input("Ingrese el valor de x: "))
n=float(input("Ingrese el valor de n: "))
a=float(input("Ingrese el valor de a: "))

def pol(x,n,a):
    p_x=((a*n)*x**n)+((a*n-1)*x**(n-1))+a*x+a*0
    print(p_x)

pol(x,n,a)
