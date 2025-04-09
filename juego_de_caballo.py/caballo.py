class CaballoAjedrez:
    def __init__(self):
        self.movimientos = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        self.solucion = []

    def es_movimiento_valido(self, x, y, visitados):
        return 0 <= x < 8 and 0 <= y < 8 and (x, y) not in visitados

    def resolver_caballo(self, x, y, visitados):
        if len(visitados) == 6:  # Si ya recorrió 6 casillas
            self.solucion = visitados[:]
            return True

        for dx, dy in self.movimientos:
            nx, ny = x + dx, y + dy
            if self.es_movimiento_valido(nx, ny, visitados):
                visitados.append((nx, ny))
                if self.resolver_caballo(nx, ny, visitados):
                    return True
                visitados.pop()  # Backtracking

        return False

    def iniciar(self, x, y):
        visitados = [(x, y)]
        if self.resolver_caballo(x, y, visitados):
            return self.solucion
        else:
            return None