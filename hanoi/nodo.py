class NodoHanoi:

    def __init__(self, torres):
        self.torres = torres
        self.movimientos = []

    def agregar_movimiento(self, movimiento):
        self.movimientos.append(movimiento)

    def __repr__(self):
        return f"NodoHanoi({self.torres})"
