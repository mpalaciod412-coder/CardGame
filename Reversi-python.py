import random

# Esta función inicia el tablero de juego
def tablero_inicial():
    tablero = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(" ")
        tablero.append(fila)
    
    tablero[3][3] = "X"
    tablero[4][4] = 'X'
    tablero[3][4] = "O" 
    tablero[4][3] = 'O'
    
    print("  12345678")
    print(" +--------+")
    for i in range(8):
        print(f"{i+1}|", end = "")
        for celda in tablero[i]:
            print(celda, end = "")
        print(f"|{i+1}")
    print(" +--------+")
    print("  12345678")

    return tablero

# Funcion de asignación de fichas
def asig_fichas(jugadores, primer_jug):
    while True:
        seleccion = input(f"{primer_jug} indica con que ficha vas a jugar [O]/[X]:").upper()
        if seleccion in ["O", "X"]:
            break
        else:
            print("Entrada inválida. Por favor, selecciona 'O' o 'X'.")
    jugadores_dict = {}
    if seleccion == "O":
        jugadores_dict[primer_jug] = "O"
        jugadores_dict[jugadores[0]] = "X"
    elif seleccion == "X":
        jugadores_dict[primer_jug] = "X"
        jugadores_dict[jugadores[0]] = "O"
    return jugadores_dict

# Función que añade fichas y revisa si la casilla está ocupada
def anadir_ficha(file, fila, columna, ficha, tablero, jugador):
    if tablero[fila-1][columna-1] != " ":
        print("La casilla", fila , columna, "ya está ocupada")
        return False
    else:
        tablero[fila-1][columna-1] = ficha
        voltereta_ficha(tablero, fila, columna, ficha)
        file.write(f"{jugador}[{ficha}] jugada en fila {fila}, columna {columna}\n")
        file.flush()
    print("  12345678")
    print(" +--------+")
    for i in range(8):
        print(f"{i+1}|", end = "")
        for celda in tablero[i]:
            print(celda, end = "")
        print(f"|{i+1}")
    print(" +--------+")
    print("  12345678")

    return True

# Función para contar las fichas
def contar_fichas(tablero, jugadorX, jugadorO):
    fichaX = 0
    fichaO = 0
    for fila in tablero:
        for celda in fila:
            if celda == "X":
                fichaX += 1
            elif celda == "O":
                fichaO += 1
    print(f"Puntaje ---> {jugadorX} : {fichaX} {jugadorO} : {fichaO}")
    if fichaX > fichaO:
        print(f"El ganador es {jugadorX}!")
    elif fichaO > fichaX:
        print(f"El ganador es {jugadorO}!")
    else:
        print("Es un empate!")
    return fichaX + fichaO

# Funcion para las volteretas
def voltereta_ficha(tablero, fila, columna, jugador):
    voltear_horizontal(tablero, fila, columna, jugador)
    voltear_vertical(tablero, fila, columna, jugador)
    voltear_diagonal(tablero, fila, columna, jugador)

# Función para voltear horizontalmente
def voltear_horizontal(tablero, fila, columna, jugador):
    # Voltear de forma horizontal hacia la izquierda
    i = columna - 2
    while i >= 0 and tablero[fila-1][i] != " ":
        if tablero[fila-1][i] == jugador:
            # Confirmar voltereta
            print(f"Voltereta horizontal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for j in range(i+1, columna-1):
                tablero[fila-1][j] = jugador
            break
        i -= 1
    # Voltear de forma horizontal hacia la derecha
    i = columna
    while i < 8 and tablero[fila-1][i] != " ":
        if tablero[fila-1][i] == jugador:
            # Confirmar voltereta
            print(f"Voltereta horizontal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for j in range(columna, i):
                tablero[fila-1][j] = jugador
            break
        i += 1

# Función para voltear verticalmente
def voltear_vertical(tablero, fila, columna, jugador):
    # Voltear de forma vertical hacia arriba
    i = fila - 2
    while i >= 0 and tablero[i][columna-1] != " ":
        if tablero[i][columna-1] == jugador:
            # Confirmar voltereta
            print(f"Voltereta vertical en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for j in range(i+1, fila-1):
                tablero[j][columna-1] = jugador
            break
        i -= 1
    # Voltear de forma vertical hacia abajo
    i = fila
    while i < 8 and tablero[i][columna-1] != " ":
        if tablero[i][columna-1] == jugador:
            # Confirmar voltereta
            print(f"Voltereta vertical en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for j in range(fila, i):
                tablero[j][columna-1] = jugador
            break
        i += 1

# Función para voltear diagonalmente
def voltear_diagonal(tablero, fila, columna, jugador):
    # Voltear diagonal hacia arriba-izquierda
    i, j = fila-2, columna-2
    while i >= 0 and j >= 0 and tablero[i][j] != " ":
        if tablero[i][j] == jugador:
            # Confirmar voltereta
            print(f"Voltereta diagonal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for k, l in zip(range(i+1, fila-1), range(j+1, columna-1)):
                tablero[k][l] = jugador
            break
        i -= 1
        j -= 1
    # Voltear diagonal hacia abajo-derecha
    i, j = fila, columna
    while i < 8 and j < 8 and tablero[i][j] != " ":
        if tablero[i][j] == jugador:
            # Confirmar voltereta
            print(f"Voltereta diagonal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for k, l in zip(range(fila, i), range(columna, j)):
                tablero[k][l] = jugador
            break
        i += 1
        j += 1
    # Voltear diagonal hacia arriba-derecha
    i, j = fila-2, columna
    while i >= 0 and j < 8 and tablero[i][j] != " ":
        if tablero[i][j] == jugador:
            # Confirmar voltereta
            print(f"Voltereta diagonal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for k, l in zip(range(i+1, fila-1), range(j-1, columna-1, -1)):
                tablero[k][l] = jugador
            break
        i -= 1
        j += 1
    # Voltear diagonal hacia abajo-izquierda
    i, j = fila, columna-2
    while i < 8 and j >= 0 and tablero[i][j] != " ":
        if tablero[i][j] == jugador:
            # Confirmar voltereta
            print(f"Voltereta diagonal en [{fila},{columna}], pulsa [ENTER] para confirmar")
            input()  # Pausa para que el usuario confirme la voltereta
            for k, l in zip(range(fila, i), range(columna-1, j, -1)):
                tablero[k][l] = jugador
            break
        i += 1
        j -= 1

# Función de asignacion de jugadas
def jugar(jugadorX, jugadorO, jugadores_dict, tablero):
    tablero = tablero_inicial()  # Inicializar el tablero una vez
    fichaX,fichaO = 0,0
    for fila in tablero:
        for celda in fila:
            if celda == "X":
                fichaX += 1
            elif celda == "O":
                fichaO += 1
    print(f"Puntaje ---> {jugadorX} : {fichaX} {jugadorO} : {fichaO}")
    jugadores_partida = [jugadorX, jugadorO]
    turno = 0
    with open("jugadas.txt", "a") as file:  # Abrir en modo de adición
        while True:
            jugador = jugadores_partida[turno]
            ficha = "X" if jugador == jugadorX else "O"
            jugada = input(f"{jugador}[{ficha}] indica <fila>,<columna>, [P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar:")
            if jugada == "T":
                print(f"{jugador} se ha retirado. Gana {jugadores_partida[1-turno]}")
                file.write(f"{jugador} se ha retirado. Gana {jugadores_partida[1-turno]}\n")
                file.flush()
                break
            if jugada == "P":
                print(f"{jugador} pasa el turno")
                file.write(f"{jugador} pasa el turno\n")
                file.flush()
                turno = 1 - turno
                continue 
            elif jugada == "A":
                while True:
                    fila = random.randint(1, 8)
                    columna = random.randint(1, 8)
                    if tablero[fila-1][columna-1] == " ":
                        anadir_ficha(file, fila, columna, ficha, tablero, jugador)
                        print(fila, columna)
                        break
            else:
                while True:
                    try:
                        
                        fila, columna = int(jugada.split(",")[0]), int(jugada.split(",")[1])
                        if 1 <= fila <= 8 and 1 <= columna <= 8:
                            if tablero[fila-1][columna-1] == " ":
                                if anadir_ficha(file, fila, columna, ficha, tablero, jugador):
                                    file.write(f"{jugador}[{ficha}] jugada en fila {fila}, columna {columna}\n")
                                    file.flush()
                                    break
                            else:
                                print("La casilla ya está ocupada. Intenta de nuevo.")
                                jugada = input(f"{jugador}[{ficha}] indica <fila>,<columna>, [P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar:")
                        else:
                            print("Las coordenadas deben estar entre 1 y 8. Intenta de nuevo.")
                            jugada = input(f"{jugador}[{ficha}] indica <fila>,<columna>, [P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar:")
                    except (ValueError, IndexError):
                        print("Entrada inválida. Debes ingresar dos números separados por una coma. Intenta de nuevo.")
                        jugada = input(f"{jugador}[{ficha}] indica <fila>,<columna>, [P] para pasar el turno, [T] para terminar el juego o [A] para jugada al azar:")
            
            # Verificar si el tablero está lleno
            if all(celda != " " for fila in tablero for celda in fila):
                print("El tablero está lleno.")
                contar_fichas(tablero, jugadorX, jugadorO)
                break
            
            turno = 1 - turno

# Variables generalizadas
tablero = []
fichas = 0

# ---------------------Inicio del juego---------------------
titulo = input("Domina la voltereta")
    
# Pedir datos de los jugadores y escoger ficha
jugadores = []
jug_1 = input("Por favor indique nombre de participante #1:")
jug_2 = input("Por favor indique nombre de participante #2:")
jugadores.append(jug_1)
jugadores.append(jug_2)

# Escoger cual jugador va primero
lanza_moneda = input(f"Lanzando una moneda al aire para decidir si empieza {jug_1} o {jug_2}...")
primer_jug = random.choice(jugadores)  # Usar random.choice en lugar de random.choices
empieza = input(f"Empieza {primer_jug}")
jugadores.remove(primer_jug)

# Escoger fichas
Jugadores_dict = asig_fichas(jugadores, primer_jug)

# Asignar fichas a los jugadores
p_j = input(f"{primer_jug} jugara con ficha [{Jugadores_dict[primer_jug]}]")
s_j = input(f"{jugadores[0]} jugara con ficha [{Jugadores_dict[jugadores[0]]}]")

cargar = input("Cargando el tablero de juego...")

with open("jugadas.txt", "a") as file:  # Abrir en modo de adición
    file.write(f"Inicia la partida de {primer_jug} que juega con [{Jugadores_dict[primer_jug]}] contra el jugador {jugadores[0]} que lleva [{Jugadores_dict[jugadores[0]]}] \n")
    file.flush()

jugar(primer_jug, jugadores[0], Jugadores_dict, tablero)
