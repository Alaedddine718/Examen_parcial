from caballo import Caballo
from tablero import Tablero

class JuegoCaballo:
    def __init__(self):
        # Crear una instancia del tablero
        self.tablero = Tablero()

        # Crear una instancia del caballo
        self.caballo = Caballo()

        # Lista para almacenar los movimientos realizados
        self.movimientos_realizados = []

    def simular_movimientos(self, movimientos):
        # Simular movimientos del caballo
        for movimiento in movimientos:
            if self.tablero.mover_caballo(self.caballo, movimiento):
                self.movimientos_realizados.append(movimiento)

    def mostrar_movimientos(self):
        # Mostrar todos los movimientos realizados
        print("Movimientos realizados por el caballo:")
        for i, movimiento in enumerate(self.movimientos_realizados, start=1):
            print(f"{i}: {movimiento}")
