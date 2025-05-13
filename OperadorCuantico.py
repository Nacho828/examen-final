import numpy as np
from EstadoCuantico import EstadoCuantico
class OperadorCuantico:
    def __init__(self, nombre: str, matriz: List[List[complex]]):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        vector = np.array(estado.vector, dtype=complex)
        if self.matriz.shape[1] != len(vector):
            raise ValueError("Dimensión del operador incompatible con el estado.")
        
        resultado = np.dot(self.matriz, vector)
        nuevo_id = f"{estado.id}_{self.nombre}"
        return EstadoCuantico(nuevo_id, list(resultado), estado.base)

    def __str__(self):
        return f"Operador {self.nombre}: {self.matriz}"
