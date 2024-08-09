from arbitro import Arbitro

def test_calcular_puntaje_jugada_ambos_M():
    assert Arbitro.calcular_puntaje_jugada("M", "M") == (0, 0)

def test_calcular_puntaje_jugada_M_y_S():
    assert Arbitro.calcular_puntaje_jugada("M", "S") == (2, -1)

def test_calcular_puntaje_jugada_ambos_S():
    assert Arbitro.calcular_puntaje_jugada("S", "S") == (1, 1)

def test_calcular_puntaje_jugada_S_y_M():
    assert Arbitro.calcular_puntaje_jugada("S", "M") == (-1, 2)

