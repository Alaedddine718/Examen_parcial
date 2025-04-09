import matplotlib.pyplot as plt

# tablero.py

class Tablero:
    def __init__(self):
        """Inicializa un tablero de ajedrez vacío."""
        self.tablero = [["." for _ in range(8)] for _ in range(8)]

    def imprimir(self):
        """Imprime el tablero de ajedrez."""
        for fila in self.tablero:
            print(" ".join(fila))
        print()

    def colocar(self, x, y, simbolo):
        """Coloca un símbolo en una posición específica del tablero."""
        self.tablero[x][y] = simbolo

    def limpiar(self):
        """Limpia el tablero, dejándolo vacío."""
        self.tablero = [["." for _ in range(8)] for _ in range(8)]


class Caballo:
    def __init__(self, x, y):
        """Inicializa la posición del caballo."""
        self.x = x
        self.y = y

    def movimientos_posibles(self):
        """Calcula los movimientos posibles del caballo desde su posición actual."""
        movimientos = [
            (self.x + 2, self.y + 1), (self.x + 2, self.y - 1),
            (self.x - 2, self.y + 1), (self.x - 2, self.y - 1),
            (self.x + 1, self.y + 2), (self.x + 1, self.y - 2),
            (self.x - 1, self.y + 2), (self.x - 1, self.y - 2)
        ]
        # Filtrar movimientos que estén dentro del tablero
        return [(mx, my) for mx, my in movimientos if 0 <= mx < 8 and 0 <= my < 8]

    def mostrar_movimientos(self, tablero):
        """Muestra el tablero con los movimientos posibles del caballo."""
        tablero.limpiar()
        tablero.colocar(self.x, self.y, "C")  # Posición actual del caballo
        for mx, my in self.movimientos_posibles():
            tablero.colocar(mx, my, "*")  # Posiciones posibles
        tablero.imprimir()

    def mostrar_movimientos_grafico(self):
        """Muestra un gráfico con los movimientos posibles del caballo."""
        fig, ax = plt.subplots(figsize=(8, 8))

        # Dibujar el tablero
        for x in range(8):
            for y in range(8):
                color = "white" if (x + y) % 2 == 0 else "gray"
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color=color))

        # Posición actual del caballo
        ax.text(self.y + 0.5, self.x + 0.5, "C", color="red", ha="center", va="center", fontsize=16)

        # Movimientos posibles
        for mx, my in self.movimientos_posibles():
            ax.text(my + 0.5, mx + 0.5, "*", color="blue", ha="center", va="center", fontsize=16)

        # Configuración del gráfico
        ax.set_xlim(0, 8)
        ax.set_ylim(0, 8)
        ax.set_xticks(range(9))
        ax.set_yticks(range(9))
        ax.grid(True)
        ax.set_aspect("equal")
        plt.title("Movimientos posibles del caballo")
        plt.show()


if __name__ == "__main__":
    # Crear un tablero
    tablero = Tablero()

    # Crear un caballo en una posición inicial (por ejemplo, en el centro del tablero)
    caballo = Caballo(4, 4)

    # Mostrar el tablero con los movimientos posibles del caballo
    caballo.mostrar_movimientos(tablero)

    # Mostrar el gráfico con los movimientos posibles del caballo
    caballo.mostrar_movimientos_grafico()