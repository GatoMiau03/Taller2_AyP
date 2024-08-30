def movidas_posibles(torres, ultimo_movimiento):
    posibles = []
    for origen in range(3):
        if torres[origen]:
            disco_origen = torres[origen][0]
            for destino in range(3):
                if origen != destino:
                    if not torres[destino] or disco_origen < torres[destino][0]:
                        # Evitar movimientos que revierten el último
                        if not ultimo_movimiento or [destino, origen] != ultimo_movimiento:
                            posibles.append([origen, destino])
    return posibles

def aplicar_movida(torres, movida):
    origen, destino = movida
    if not torres[origen]:
        return None
    if torres[destino] and torres[origen][0] > torres[destino][0]:
        return None
    
    nuevo_torres = [list(t) for t in torres]
    disco = nuevo_torres[origen].pop(0)
    nuevo_torres[destino].insert(0, disco)
    return nuevo_torres

def estado_logrado(torres, objetivo):
    return torres == objetivo

def mostrar_estado(estado):
    torres, movidas_posibles, nuevos_estados, estados_previos, ultimo_movimiento = estado
    print("Estado actual:")
    print(f"A: {' '.join(map(str, torres[0]))}")
    print(f"B: {' '.join(map(str, torres[1]))}")
    print(f"C: {' '.join(map(str, torres[2]))}")
    print(f"Movidas posibles: {', '.join([f'{chr(65 + m[0])}>{chr(65 + m[1])}' for m in movidas_posibles])}")
    print("Nuevos estados:")
    for nuevo_estado in nuevos_estados:
        print(nuevo_estado)
    print("Último estado previo:")
    if estados_previos:
        print(estados_previos[-1])

def main():
    estado_inicial = [[1, 2, 3, 4], [], []]
    estado_objetivo = [[], [], [1, 2, 3, 4]]
    
    estado = [estado_inicial, [], [], [estado_inicial], None]
    
    while True:
        torres = estado[0]
        ultimo_movimiento = estado[4]
        movidas = movidas_posibles(torres, ultimo_movimiento)
        
        if estado_logrado(torres, estado_objetivo):
            print("Estado logrado")
            for est in estado[3]:
                print(est)
            return
        
        estado[1] = movidas
        estado[2] = []
        
        for movida in movidas:
            nuevo_estado = aplicar_movida(torres, movida)
            if nuevo_estado and nuevo_estado not in estado[3]:
                estado[2].append(nuevo_estado)
        
        estado[3].append(torres)
        
        if not estado[2]:
            print("No logrado")
            return
        
        estado[0] = estado[2].pop(0)
        estado[4] = estado[1][0]  # Actualiza el último movimiento realizado
        mostrar_estado(estado)

if __name__ == "__main__":
    main()
