import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from tres_en_raya import TresEnRaya


def jugar_todas(juego, jugadas):
    r = None
    for f, c in jugadas:
        r = juego.jugar(f, c)
    return r


class TableroTest(unittest.TestCase):
    def test_tablero_inicia_vacio(self):
        self.assertEqual(TresEnRaya().tablero, [" "] * 9)

    def test_fuera_del_tablero(self):
        for f, c in [(3, 0), (0, 3), (-1, 0), (0, -1)]:
            with self.assertRaises(ValueError):
                TresEnRaya().jugar(f, c)

    def test_casilla_ocupada(self):
        j = TresEnRaya()
        j.jugar(1, 1)
        with self.assertRaises(ValueError):
            j.jugar(1, 1)

    def test_jugada_invalida_no_cambia_turno(self):
        j = TresEnRaya()
        j.jugar(0, 0)
        with self.assertRaises(ValueError):
            j.jugar(0, 0)
        self.assertEqual(j.turno, "O")


class TurnosTest(unittest.TestCase):
    def test_empieza_X(self):
        j = TresEnRaya()
        j.jugar(0, 0)
        self.assertEqual(j.tablero[0], "X")

    def test_alternan_turnos(self):
        j = TresEnRaya()
        j.jugar(0, 0)
        j.jugar(0, 1)
        j.jugar(0, 2)
        self.assertEqual(j.tablero[:3], ["X", "O", "X"])


class GanadorTest(unittest.TestCase):
    def test_sin_ganador_en_curso(self):
        self.assertIsNone(TresEnRaya().jugar(0, 0))

    def test_gana_X_en_cada_linea(self):
        lineas = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                  [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                  [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
        for linea in lineas:
            with self.subTest(linea=linea):
                j = TresEnRaya()
                relleno = [p for p in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
                           if p not in linea][:2]
                jugadas = [linea[0], relleno[0], linea[1], relleno[1], linea[2]]
                self.assertEqual(jugar_todas(j, jugadas), "X")
                self.assertEqual(j.ganador, "X")

    def test_gana_O(self):
        j = TresEnRaya()
        self.assertEqual(jugar_todas(j, [(0, 0), (1, 0), (0, 1), (1, 1), (2, 2), (1, 2)]), "O")

    def test_no_se_juega_tras_ganar(self):
        j = TresEnRaya()
        jugar_todas(j, [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)])
        with self.assertRaises(ValueError):
            j.jugar(2, 2)


class EmpateTest(unittest.TestCase):
    # X O X / X O O / O X X
    JUGADAS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]

    def test_empate(self):
        self.assertEqual(jugar_todas(TresEnRaya(), self.JUGADAS), "Empate")

    def test_no_se_juega_tras_empate(self):
        j = TresEnRaya()
        jugar_todas(j, self.JUGADAS)
        with self.assertRaises(ValueError):
            j.jugar(0, 0)

    def test_ultima_jugada_que_gana_no_es_empate(self):
        # X llena el tablero y completa diagonal con la 9a jugada
        j = TresEnRaya()
        r = jugar_todas(j, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 1), (1, 2), (2, 0), (2, 2)])
        self.assertEqual(r, "X")


if __name__ == "__main__":
    unittest.main()
