def jugador():
    while True:
        eleccion_jugador = int(input("Elige 0 (Piedra) | 1 (Papel) | 2 (Tijeras) | 3 (Lagarto) | 4 (Spock): "))
        if eleccion_jugador in [0, 1, 2, 3, 4]:
            return eleccion_jugador
        else:
            print("Por favor, elige un número entre 0 y 4.")
    