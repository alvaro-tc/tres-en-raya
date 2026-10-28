import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from tres_en_raya import TresEnRaya


class TestTresEnRayaInicio(unittest.TestCase):

    def test_tablero_empieza_con_nueve_posiciones_vacias(self):
        juego = TresEnRaya()
        self.assertEqual(juego.tablero, [" "] * 9)

    def test_el_primer_turno_es_de_X(self):
        juego = TresEnRaya()
        self.assertEqual(juego.turno, "X")

    def test_no_hay_ganador_al_empezar(self):
        juego = TresEnRaya()
        self.assertIsNone(juego.ganador)


class TestTresEnRayaTurnos(unittest.TestCase):

    def test_primer_jugada_devuelve_None_partida_en_curso(self):
        juego = TresEnRaya()
        self.assertIsNone(juego.jugar(0, 0))

    def test_primera_jugada_coloca_X_en_la_casilla(self):
        juego = TresEnRaya()
        juego.jugar(1, 1)
        self.assertEqual(juego.tablero[4], "X")

    def test_tras_jugar_X_el_turno_pasa_a_O(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)
        self.assertEqual(juego.turno, "O")

    def test_los_turnos_alternan_X_y_O(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 1)  # X
        self.assertEqual(juego.tablero[0], "X")
        self.assertEqual(juego.tablero[1], "O")
        self.assertEqual(juego.tablero[4], "X")
        self.assertEqual(juego.turno, "O")


class TestTresEnRayaMovimientosInvalidos(unittest.TestCase):

    def test_fila_negativa_lanza_ValueError(self):
        juego = TresEnRaya()
        with self.assertRaises(ValueError):
            juego.jugar(-1, 0)

    def test_columna_negativa_lanza_ValueError(self):
        juego = TresEnRaya()
        with self.assertRaises(ValueError):
            juego.jugar(0, -1)

    def test_fila_fuera_del_tablero_lanza_ValueError(self):
        juego = TresEnRaya()
        with self.assertRaises(ValueError):
            juego.jugar(3, 0)

    def test_columna_fuera_del_tablero_lanza_ValueError(self):
        juego = TresEnRaya()
        with self.assertRaises(ValueError):
            juego.jugar(0, 3)

    def test_casilla_ocupada_lanza_ValueError(self):
        juego = TresEnRaya()
        juego.jugar(2, 2)
        with self.assertRaises(ValueError):
            juego.jugar(2, 2)

    def test_movimiento_invalido_no_cambia_el_turno(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X, ahora turno O
        with self.assertRaises(ValueError):
            juego.jugar(0, 0)
        self.assertEqual(juego.turno, "O")


class TestTresEnRayaVictoria(unittest.TestCase):

    def test_gana_X_con_fila_horizontal(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(1, 0)  # O
        juego.jugar(0, 1)  # X
        juego.jugar(1, 1)  # O
        resultado = juego.jugar(0, 2)  # X
        self.assertEqual(resultado, "X")
        self.assertEqual(juego.ganador, "X")

    def test_gana_O_con_columna_vertical(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 0)  # X
        juego.jugar(1, 1)  # O
        juego.jugar(2, 2)  # X
        resultado = juego.jugar(2, 1)  # O
        self.assertEqual(resultado, "O")
        self.assertEqual(juego.ganador, "O")

    def test_gana_X_con_diagonal_principal(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 1)  # O
        juego.jugar(1, 1)  # X
        juego.jugar(0, 2)  # O
        resultado = juego.jugar(2, 2)  # X
        self.assertEqual(resultado, "X")
        self.assertEqual(juego.ganador, "X")

    def test_gana_O_con_diagonal_secundaria(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(0, 2)  # O
        juego.jugar(0, 1)  # X
        juego.jugar(1, 1)  # O
        juego.jugar(1, 0)  # X
        resultado = juego.jugar(2, 0)  # O
        self.assertEqual(resultado, "O")
        self.assertEqual(juego.ganador, "O")

    def test_la_victoria_devuelve_ganador_en_la_ultima_jugada(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(1, 0)  # O
        juego.jugar(0, 1)  # X
        juego.jugar(1, 1)  # O
        self.assertIsNone(juego.ganador)
        self.assertEqual(juego.jugar(0, 2), "X")


class TestTresEnRayaEmpate(unittest.TestCase):

    def test_tablero_lleno_sin_ganador_es_empate(self):
        # Tablero final: X O X / X O O / O X X  (sin tres en línea)
        juego = TresEnRaya()
        jugadas = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0),
                   (2, 0), (1, 2), (2, 2), (2, 1)]
        resultados = [juego.jugar(f, c) for f, c in jugadas]
        self.assertIsNone(resultados[-2])
        self.assertEqual(resultados[-1], "Empate")
        self.assertIsNone(juego.ganador)

    def test_empate_no_se_declara_antes_de_llenar_el_tablero(self):
        juego = TresEnRaya()
        jugadas = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0),
                   (2, 0), (1, 2), (2, 2)]
        for f, c in jugadas:
            self.assertIsNone(juego.jugar(f, c))


class TestTresEnRayaPartidaTerminada(unittest.TestCase):

    def test_no_se_puede_jugar_tras_victoria(self):
        juego = TresEnRaya()
        juego.jugar(0, 0)  # X
        juego.jugar(1, 0)  # O
        juego.jugar(0, 1)  # X
        juego.jugar(1, 1)  # O
        juego.jugar(0, 2)  # X gana
        with self.assertRaises(ValueError):
            juego.jugar(2, 2)

    def test_no_se_puede_jugar_tras_empate(self):
        juego = TresEnRaya()
        jugadas = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0),
                   (2, 0), (1, 2), (2, 2), (2, 1)]
        for f, c in jugadas:
            juego.jugar(f, c)
        with self.assertRaises(ValueError):
            juego.jugar(0, 0)


if __name__ == "__main__":
    unittest.main()
