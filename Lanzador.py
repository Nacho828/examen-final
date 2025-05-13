from RepositorioDeEstados import RepositorioDeEstados
from OperadorCuantico import OperadorCuantico
import numpy as np


class Lanzador:
    def __init__(self):
        self.repo = RepositorioDeEstados()

    def registrar_estado(self):
        print("\nRegistro de nuevo estado cuántico")
        id = input("Identificador único: ")
        vector_str = input("Vector de amplitudes (separadas por coma, ej: 1+0j,0+0j): ")
        base = input("Base asociada: ")
        try:
            vector = [complex(x.strip()) for x in vector_str.split(",")]
            self.repo.agregar_estado(id, vector, base)
            print("Estado registrado correctamente.")
        except Exception as e:
            print(f"Error al registrar estado: {e}")

    def listar_estados(self):
        print("\nEstados registrados:")
        for linea in self.repo.listar_estados():
            print(linea)

    def ejecutar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar nuevo estado cuántico")
            print("2. Listar estados cuánticos")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.registrar_estado()
            elif opcion == "2":
                self.listar_estados()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")