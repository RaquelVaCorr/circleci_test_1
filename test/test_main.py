import code.main as main
import pytest

@pytest.mark.parametrize(
        (
    "a",
    "b",
    "valor_esperado"
        ),
        [
    ( #caso 1
    2,
    3,
    5
    ),
    (
    4,
    5,
    9    
    )
        ],
        ids = ["test_1", "test_2"]
)
def test_suma(a,b, valor_esperado):
    assert main.suma(a,b) == valor_esperado