
def sum_a(*args):
    suma=0
    for item in args:
        suma+=item
    print(f"La suma es: {suma}")

sum_a(1,2,3,4,5)
sum_a(6,7,8,9,10)
sum_a(100,200,300,400,500)
