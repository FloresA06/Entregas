
from fractions import Fraction

def opfracc(frac1, frac2):
    frac1=Fraction(input("Primera fraccion: "))
    frac2=Fraction(input("Segunda fraccion: "))
    suma=frac1+frac2
    mult=frac1*frac2
    print(f"la suma es: {suma}, la multiplicacion es: {mult}")
    return

opfracc((1,2),(3,4))
