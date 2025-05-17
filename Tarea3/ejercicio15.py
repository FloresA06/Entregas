
import random

intt=int(input("Ingrese un numero entre 1 y 50: "))

def adivinar(intt):
    num_o=random.randint(1,50)
    while intt!=num_o:
        if intt>num_o:
            print("Su numero es mayor que el obejtivo")
            intt=int(input("Ingrese su numero nuevamente: "))
        elif intt<num_o:
            print("Su numero es menor que el obejtivo")
            intt=int(input("Ingrese su numero nuevamente: "))
        elif intt==num_o:
            break
    if intt==num_o:
        print("Ha adivinado correctamente")
        
adivinar(intt)
