def parse_input():
    movimiento = input("Ingrese su movimiento: ").strip().split()
    if len(movimiento) == 1 and movimiento[0].lower() == 'salir':
        return None, None, True 
    if len(movimiento) != 2 or movimiento[0] not in 'ABC' or movimiento[1] not in 'ABC':
        print("Torres mal etiquetadas o entrada inválida.")
        return None, None, False
    return movimiento[0], movimiento[1], False

def mover_discos(torres, origen, destino):
    if not torres[origen]:
        return False, None 
    if torres[destino] and torres[origen][0] > torres[destino][0]:
        return False, (torres[origen][0], torres[destino][0])
    
    disco = torres[origen].pop(0)
    torres[destino].insert(0, disco)
    return True, None

def mostrar_torres(torres):
    for torre in 'ABC':
        print(torre, ' '.join(map(str, torres[torre])))

def estado_logrado(torres):
    return torres['A'] == [] and torres['B'] == [] and torres['C'] == [1, 2, 3, 4]

def movidas_posibles(torres):
    posibles = []
    for origen in 'ABC':
        if torres[origen]:
            disco_origen = torres[origen][0]
            for destino in 'ABC':
                if origen != destino:
                    if not torres[destino] or disco_origen < torres[destino][0]:
                        posibles.append(f"{origen}>{destino}")
    return posibles

def main():
    torres = {'A': [1, 2, 3, 4], 'B': [], 'C': []}
    configuraciones_previas = []
    numero_movida = 0

    mostrar_torres(torres)
    
    while True:
        if numero_movida >= 16:
            print("No logrado")
            break
        
        origen, destino, salir = parse_input()
        if salir:
            print("Juego terminado.")
            break

        if origen is None or destino is None:
            continue

        movimiento_exitoso, error_info = mover_discos(torres, origen, destino)
        
        if movimiento_exitoso:
            numero_movida += 1
            mostrar_torres(torres)
            
            configuracion_actual = (tuple(torres['A']), tuple(torres['B']), tuple(torres['C']))
            
            if configuracion_actual in configuraciones_previas:
                print(f"Jugada repetida en la movida {numero_movida}")
                break
            
            configuraciones_previas.append(configuracion_actual)
            
            if estado_logrado(torres):
                print(f"Logrado en la movida {numero_movida}")
                break
        else:
            if error_info:
                print(f"No hubo movimiento ({error_info[0]} es más grande que {error_info[1]})")
            else:
                print("No hubo movimiento")
            mostrar_torres(torres)
        
        posibles = movidas_posibles(torres)
        print(f"Movidas posibles {' '.join(posibles)}")

if __name__ == "__main__":
    main()