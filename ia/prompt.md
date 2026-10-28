# Prompt usado para generar las pruebas con IA

Actúa como un ingeniero QA experto en TDD con Python. Genera pruebas unitarias con `unittest` para la kata del **Tres en Raya**.

Reglas de la kata:
1. El tablero es de 3x3 y empieza vacío; las posiciones son (fila, columna) base 0.
2. El primer jugador siempre es `X`; los turnos se alternan `X`, `O`, `X`...
3. No se puede jugar fuera del tablero ni en una casilla ocupada (lanzar `ValueError`).
4. Gana quien complete tres fichas en línea: horizontal, vertical o diagonal.
5. Si el tablero se llena sin ganador, el resultado es `"Empate"`.
6. Tras terminar la partida no se puede seguir jugando (`ValueError`).

API a probar (módulo `src/tres_en_raya.py`, clase `TresEnRaya`):
- `jugar(fila, col)` -> devuelve `"X"`, `"O"`, `"Empate"` o `None` (partida en curso).
- Atributos: `tablero` (lista de 9 posiciones, `" "` si vacía), `turno`, `ganador`.

Requisitos: nombres de tests descriptivos en español, un caso por test, cubrir casos borde, sin dependencias externas. Entrega solo el código del archivo `test_tres_en_raya_ia.py`.
