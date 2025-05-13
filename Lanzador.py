from RepositorioDeEstados import RepositorioDeEstados
from OperadorCuantico import OperadorCuantico
import numpy as np

class Lanzador:
        def __init__(self):
            self.repo = RepositorioDeEstados()

        def ejecutar(self):
            self.repo.agregar_estado("q0", [1+0j, 0+0j], "computacional")

            # Estado base |1⟩
            self.repo.agregar_estado("q1", [0+0j, 1+0j], "computacional")

            # Puerta X (NOT)
            X = OperadorCuantico("X", [[0, 1], [1, 0]])

            # Aplicar X a q0 → debería dar |1⟩
            self.repo.aplicar_operador("q0", X, "q0_X")

            # Puerta Hadamard H
            H = OperadorCuantico("H", [[1/np.sqrt(2), 1/np.sqrt(2)],
                                       [1/np.sqrt(2), -1/np.sqrt(2)]])
            self.repo.aplicar_operador("q0", H, "q0_H")

            # Medición
            probabilidades = self.repo.medir_estado("q0_H")
            print("Probabilidades de q0_H:", probabilidades)

            # Listado de estados
            for linea in self.repo.listar_estados():
                print(linea)

            # Guardar a archivo
            self.repo.guardar("estados.json")

            # Cargar desde archivo nuevo repositorio
            nuevo_repo = RepositorioDeEstados()
            nuevo_repo.cargar("estados.json")
            print("Estados cargados:")
            for linea in nuevo_repo.listar_estados():
                print(linea)

              