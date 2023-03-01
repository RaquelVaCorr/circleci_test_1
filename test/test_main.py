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
    5,
    5,
    10    
    )
        ],
        ids = ["test_1", "test_2"]
)
def test_suma(a,b, valor_esperado):
    assert main.suma(a,b) == valor_esperado