
edad=int(input("Ingrese su edad: "))

if edad<12:
    print("Usted es un niño")
elif edad>=12 and edad<18:
    print("Usted es un adolescente")
elif edad>=18 and edad<60:
    print("Usted es un adulto")
elif edad>=60:
    print("Usted es un adulto mayor")
    