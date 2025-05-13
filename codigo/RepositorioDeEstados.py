import json
from EstadoCuantico import EstadoCuantico
from OperadorCuantico import OperadorCuantico
from typing import List, Dict

class RepositorioDeEstados:
    def __init__(self):
        self.estados = {}

    def listar_estados(self) -> List[str]:
        if not self.estados:
            return ["No hay estados registrados."]
        return [str(estado) for estado in self.estados.values()]

    def agregar_estado(self, id: str, vector: List[complex], base: str):
        if id in self.estados:
            raise ValueError(f"Error: ya existe un estado con identificador '{id}'.")
        estado = EstadoCuantico(id, vector, base)
        self.estados[id] = estado

    def obtener_estado(self, id: str) -> EstadoCuantico:
        if id not in self.estados:
            raise KeyError(f"No existe el estado con id '{id}'.")
        return self.estados[id]

    def aplicar_operador(self, id_estado: str, operador: OperadorCuantico, nuevo_id: str = None):
        estado_original = self.obtener_estado(id_estado)
        nuevo_estado = operador.aplicar(estado_original)
        if nuevo_id:
            nuevo_estado.id = nuevo_id
        if nuevo_estado.id in self.estados:
            raise ValueError(f"Error: el estado resultante '{nuevo_estado.id}' ya existe.")
        self.estados[nuevo_estado.id] = nuevo_estado

    def medir_estado(self, id: str) -> Dict[str, float]:
        estado = self.obtener_estado(id)
        return estado.medir()

    def guardar(self, archivo: str):
        data = {
            id: {
                "vector": [str(x) for x in estado.vector],
                "base": estado.base
            }
            for id, estado in self.estados.items()
        }
        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar(self, archivo: str):
        with open(archivo, "r") as f:
            data = json.load(f)
            for id, props in data.items():
                vector = [complex(x) for x in props["vector"]]
                base = props["base"]
                self.estados[id] = EstadoCuantico(id, vector, base)
