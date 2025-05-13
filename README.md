# examen-final
1. EstadoCuantico
Representa un estado cuántico individual.

Guarda un identificador, un vector de amplitudes complejas (que debe estar normalizado) y la base.
Permite medir el estado (devuelve probabilidades) y mostrarlo como texto.

2. OperadorCuantico
Representa un operador cuántico (como una puerta lógica cuántica).

Guarda un nombre y una matriz de operación.
Puede aplicar la operación a un EstadoCuantico y devolver un nuevo estado resultante.

3. RepositorioDeEstados
Gestiona un conjunto de estados cuánticos.

Permite agregar, listar, obtener y medir estados.
Puede aplicar operadores a estados, guardar los estados en un archivo y cargarlos desde un archivo.

4. Lanzador
Es la clase principal que orquesta el flujo del programa.

Crea estados y operadores, aplica operaciones, mide estados, muestra resultados y gestiona la persistencia (guardar/cargar).
Su método ejecutar ejecuta una demostración de todas estas funcionalidades.


Link Repositorio: https://github.com/Nacho828/examen-final.git