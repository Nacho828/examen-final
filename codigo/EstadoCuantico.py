import math
from typing import List, Dict

class EstadoCuantico:
    def __init__(self, id: str, vector: List[complex], base: str):
        if not vector:
            raise ValueError("El vector de estado no puede estar vacío.")
        self.id = id
        self.vector = vector
        self.base = base

        # Validar que esté normalizado (∑|amplitud|^2 ≈ 1)
        norma = sum(abs(x)**2 for x in vector)
        if not math.isclose(norma, 1.0, abs_tol=1e-6):
            raise ValueError(f"El vector de estado no está normalizado. Norma actual: {norma}")

    def medir(self) -> Dict[str, float]:
        return {str(i): round(abs(amp)**2, 6) for i, amp in enumerate(self.vector)}

    def __str__(self):
        return f"{self.id}: vector={self.vector} en base {self.base}"
