import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt


def hanoi(n, source, target, auxiliary):
    if n == 1:
        return [(source, target)]
    moves = hanoi(n - 1, source, auxiliary, target)
    moves.append((source, target))
    moves.extend(hanoi(n - 1, auxiliary, target, source))
    return moves


def guardar_movimientos_en_db(movimientos):
    try:
        conn = sqlite3.connect("hanoi.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS movimientos (id INTEGER PRIMARY KEY, origen TEXT, destino TEXT)")
        cursor.execute("DELETE FROM movimientos")  # Limpiar movimientos previos

        for src, dst in movimientos:
            cursor.execute("INSERT INTO movimientos (origen, destino) VALUES (?, ?)", (src, dst))

        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Error de Base de Datos", f"No se pudo guardar en la base de datos: {e}")
    finally:
        conn.close()


def mostrar_movimientos_en_db():
    try:
        conn = sqlite3.connect("hanoi.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM movimientos")
        movimientos = cursor.fetchall()
        return movimientos
    except sqlite3.Error as e:
        messagebox.showerror("Error de Base de Datos", f"No se pudo leer la base de datos: {e}")
        return []
    finally:
        conn.close()


def resolver_hanoi():
    try:
        n = int(entry_discos.get())
        if n <= 0:
            raise ValueError("El número de discos debe ser mayor a 0.")

        source = entry_origen.get().strip().upper()
        target = entry_destino.get().strip().upper()
        auxiliary = entry_auxiliar.get().strip().upper()

        if not source or not target or not auxiliary:
            raise ValueError("Las torres no pueden estar vacías.")
        if len({source, target, auxiliary}) < 3:
            raise ValueError("Las torres deben ser diferentes.")

        movimientos = hanoi(n, source, target, auxiliary)
        guardar_movimientos_en_db(movimientos)

        messagebox.showinfo("Éxito", f"Se resolvió con {len(movimientos)} movimientos. Revisa la base de datos.")
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error inesperado: {e}")


def mostrar_movimientos():
    movimientos = mostrar_movimientos_en_db()
    if not movimientos:
        messagebox.showinfo("Movimientos", "No hay movimientos guardados en la base de datos.")
        return

    ventana_movimientos = tk.Toplevel(root)
    ventana_movimientos.title("Movimientos Guardados")
    for i, (id_, origen, destino) in enumerate(movimientos, start=1):
        tk.Label(ventana_movimientos, text=f"{i}: Mover disco de {origen} a {destino}").pack()


def mostrar_grafica():
    movimientos = mostrar_movimientos_en_db()
    if not movimientos:
        messagebox.showinfo("Movimientos", "No hay movimientos guardados en la base de datos.")
        return

    origenes = [mov[1] for mov in movimientos]
    destinos = [mov[2] for mov in movimientos]
    pasos = list(range(1, len(movimientos) + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(pasos, origenes, label="Origen", marker="o")
    plt.plot(pasos, destinos, label="Destino", marker="o")
    plt.title("Movimientos de las Torres de Hanoi")
    plt.xlabel("Paso")
    plt.ylabel("Torre")
    plt.legend()
    plt.grid()
    plt.show()


# Configuración de la ventana principal
root = tk.Tk()
root.title("Torres de Hanoi")

tk.Label(root, text="Número de discos:").grid(row=0, column=0, padx=10, pady=5)
entry_discos = tk.Entry(root)
entry_discos.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Torre de origen:").grid(row=1, column=0, padx=10, pady=5)
entry_origen = tk.Entry(root)
entry_origen.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Torre de destino:").grid(row=2, column=0, padx=10, pady=5)
entry_destino = tk.Entry(root)
entry_destino.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Torre auxiliar:").grid(row=3, column=0, padx=10, pady=5)
entry_auxiliar = tk.Entry(root)
entry_auxiliar.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Resolver", command=resolver_hanoi).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Mostrar Movimientos", command=mostrar_movimientos).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Mostrar Gráfica", command=mostrar_grafica).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()

