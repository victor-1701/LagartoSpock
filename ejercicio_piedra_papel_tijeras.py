#HECHO POR ÓSCAR, ANGEL, VICTOR Y MARÍA

import random
import data
import input_jugador


def maquina():
    
    aleatorio = random.randrange(len(data.frames)) 
    opciones = ["Piedra", "Papel", "Tijeras", "Lagarto", "Spock"]
    eleccion_maquina = opciones[aleatorio]
    
    return aleatorio, eleccion_maquina
        

def logica_juego(eleccion_jugador, eleccion_maquina):
    
    if eleccion_maquina == eleccion_jugador:
        print("Empate")
        return 0
    elif (eleccion_maquina == 0 and (eleccion_jugador == 1 or eleccion_jugador == 4)) or \
         (eleccion_maquina == 1 and (eleccion_jugador == 2 or eleccion_jugador == 3)) or \
         (eleccion_maquina == 2 and (eleccion_jugador == 0 or eleccion_jugador == 4)) or \
         (eleccion_maquina == 3 and (eleccion_jugador == 0 or eleccion_jugador == 2)) or \
         (eleccion_maquina == 4 and (eleccion_jugador == 1 or eleccion_jugador == 3)):
        print("Has ganado esta ronda")
        return 1
    else:
        print("Ha ganado la maquina esta ronda")
        return -1


def volver_a_jugar():
    while True:
        jugar = int(input("1 para volver a jugar | 0 para cerrar programa "))
        if jugar == 1:
            main()
        elif jugar == 0:
            exit()
        else:
            print("Opción no válida")


def main():
    print("BIENVENIDO/A AL JUEGO DE PIEDRA PAPEL O TIJERAS")
    print("El primero que gane 2 rondas, gana la partida")
    
    puntos_jugador = 0
    puntos_maquina = 0
    
    while puntos_jugador < 2 and puntos_maquina < 2:
        eleccion_jugador = input_jugador.jugador()
        eleccion_maquina, nombre_eleccion_maquina = maquina()

        opciones = data.frames
        print(f"Has elegido: {opciones[eleccion_jugador]}")
        print(f"La máquina ha elegido: {opciones[eleccion_maquina]}")

        resultado = logica_juego(eleccion_jugador, eleccion_maquina)
        if resultado == 1:
            puntos_jugador += 1
        elif resultado == -1:
            puntos_maquina += 1

        print(f"Puntuación -> Jugador: {puntos_jugador} | Máquina: {puntos_maquina}")
        print("-" * 30)

    if puntos_jugador == 2:
        print("HAS GANADO LA PARTIDA")
        volver_a_jugar()
    else:
        print("LA MÁQUINA HA GANADO LA PARTIDA")
        volver_a_jugar()


if __name__ == "__main__":
    main()
    