class Caballo:
    def __init__(self):
        self.tamaño = 8
        self.movimientos_posibles = [
            [2, 1], [1, 2], [-1, 2], [-2, 1],
            [-2, -1], [-1, -2], [1, -2], [2, -1]
        ]
        self.tablero = [[-1 for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        self.movimientos = []

    def es_valido(self, pos):
        x, y = pos
        return 0 <= x < self.tamaño and 0 <= y < self.tamaño and self.tablero[x][y] == -1

    def recorrer(self, pos, paso):
        x, y = pos
        self.tablero[x][y] = paso
        self.movimientos.append([x, y])

        if paso == self.tamaño * self.tamaño - 1:
            return True

        for mov in self.movimientos_posibles:
            nuevo = [x + mov[0], y + mov[1]]
            if self.es_valido(nuevo):
                if self.recorrer(nuevo, paso + 1):
                    return True

        self.tablero[x][y] = -1
        self.movimientos.pop()
        return False

    def resolver(self, inicio):
        self.movimientos = []
        if self.recorrer(inicio, 0):
            return self.movimientos
        else:
            return None