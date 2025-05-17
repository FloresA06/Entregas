
def reg_puntajes():
    jugadores=dict()
    n=int(input("Indique la cantidad de jugadores: "))
    for i in range(n):
        nom=input(f"Ingrese el nombre del jugador {i+1}: ")
        puntaje=int(input(f"Ingrese el puntaje de {nom}: "))
        jugadores[nom]=puntaje
    return jugadores

def mostrar_puntajes(jugadores):
    print("\nPuntajes de los jugadores: ")
    for nombre,puntaje in jugadores.items():
        print(f"{nombre}:{puntaje}")

puntajes=reg_puntajes()
mostrar_puntajes(puntajes)
