LINEAS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


class TresEnRaya:
    def __init__(self):
        self.tablero = [" "] * 9
        self.turno = "X"
        self.ganador = None

    def jugar(self, fila, col):
        """Coloca la ficha del turno en (fila, col), base 0. Devuelve 'X'/'O' si gana, 'Empate' o None."""
        if self.ganador or self.terminado():
            raise ValueError("El juego ya terminó")
        if not (0 <= fila < 3 and 0 <= col < 3):
            raise ValueError("Posición fuera del tablero")
        i = fila * 3 + col
        if self.tablero[i] != " ":
            raise ValueError("Casilla ocupada")
        self.tablero[i] = self.turno
        if any(all(self.tablero[j] == self.turno for j in l) for l in LINEAS):
            self.ganador = self.turno
        self.turno = "O" if self.turno == "X" else "X"
        return self.resultado()

    def terminado(self):
        return self.ganador is not None or " " not in self.tablero

    def resultado(self):
        if self.ganador:
            return self.ganador
        return "Empate" if self.terminado() else None
