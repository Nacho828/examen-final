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

    def aplicar_operador(self):
        print("\nAplicar operador cuántico")
        id_estado = input("ID del estado a transformar: ")
        print("Operadores disponibles: X, H, Z")
        op = input("Selecciona operador (X/H/Z): ").upper()
        nuevo_id = input("Nuevo identificador para el estado resultante: ")
        try:
            if op == "X":
                matriz = [[0, 1], [1, 0]]
            elif op == "H":
                matriz = [[1/np.sqrt(2), 1/np.sqrt(2)],
                          [1/np.sqrt(2), -1/np.sqrt(2)]]
            elif op == "Z":
                matriz = [[1, 0], [0, -1]]
            else:
                print("Operador no reconocido.")
                return
            operador = OperadorCuantico(op, matriz)
            self.repo.aplicar_operador(id_estado, operador, nuevo_id)
            print(f"Operador {op} aplicado correctamente. Nuevo estado: {nuevo_id}")
        except Exception as e:
            print(f"Error al aplicar operador: {e}")

    def medir_estado(self):
        print("\nMedición de estado cuántico")
        id_estado = input("ID del estado a medir: ")
        try:
            probabilidades = self.repo.medir_estado(id_estado)
            print("Probabilidades de medición:")
            for base, prob in probabilidades.items():
                print(f"Base {base}: {prob}")
        except Exception as e:
            print(f"Error al medir estado: {e}")

    def guardar_estados(self):
        archivo = input("Nombre del archivo para guardar (ej: estados.json): ")
        ruta = os.path.join(self.directorio_datos, archivo)
        try:
            self.repo.guardar(ruta)
            print("Estados guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_estados(self):
        archivo = input("Nombre del archivo para cargar (ej: estados.json): ")
        ruta = os.path.join(self.directorio_datos, archivo)
        try:
            self.repo.cargar(ruta)
            print("Estados cargados correctamente.")
        except Exception as e:
            print(f"Error al cargar: {e}")

    def ejecutar(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar nuevo estado cuántico")
            print("2. Listar estados cuánticos")
            print("3. Aplicar operador cuántico")
            print("4. Medir estado cuántico")
            print("5. Guardar estados en archivo")
            print("6. Cargar estados desde archivo")
            print("7. Salir")
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.registrar_estado()
            elif opcion == "2":
                self.listar_estados()
            elif opcion == "3":
                self.aplicar_operador()
            elif opcion == "4":
                self.medir_estado()
            elif opcion == "5":
                self.guardar_estados()
            elif opcion == "6":
                self.cargar_estados()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")