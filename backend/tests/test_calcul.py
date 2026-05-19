from modules.calcul import calcul


def test_calcul_returns_square_for_positive_integer() -> None:
    assert calcul(4) == 16


def test_calcul_returns_square_for_zero() -> None:
    assert calcul(0) == 0


def test_calcul_returns_square_for_negative_integer() -> None:
    assert calcul(-3) == 9
