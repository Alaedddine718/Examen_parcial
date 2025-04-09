import random
import time

def carrera_de_caballos():
    caballos = ["Caballo 1", "Caballo 2", "Caballo 3", "Caballo 4"]
    posiciones = [0, 0, 0, 0]
    meta = 20

    print("¡Bienvenidos a la carrera de caballos!")
    print("Los caballos están listos en la línea de salida.\n")

    while max(posiciones) < meta:
        time.sleep(1)
        for i in range(len(caballos)):
            posiciones[i] += random.randint(1, 3)
            print(f"{caballos[i]} está en la posición {posiciones[i]}")
        print("-" * 30)

    ganador = caballos[posiciones.index(max(posiciones))]
    print(f"¡El ganador es {ganador}!")

if __name__ == "__main__":
    carrera_de_caballos()