from RepositorioDeEstados import RepositorioDeEstados
from OperadorCuantico import OperadorCuantico
import numpy as np

class Lanzador:
    def __init__(self):
        self.repo = RepositorioDeEstados()

    def registrar_estado(self):
        print("Registro de nuevo estado cuántico")
        id = input("Identificador único: ")
        vector_str = input("Vector de amplitudes (separadas por coma, ej: 1+0j,0+0j): ")
        base = input("Base asociada: ")
        try:
            vector = [complex(x.strip()) for x in vector_str.split(",")]
            self.repo.agregar_estado(id, vector, base)
            print("Estado registrado correctamente.")
        except Exception as e:
            print(f"Error al registrar estado: {e}")

    # ...resto de la clase...
