from utils import resolve_try_type


def test_resolve_try_type():
    a,b,c,= 234,56,45
    result=resolve_try_type(a,b,c)
    assert result == "разносторонний"


def test_resolve_try_type_same():
    a,b,c,= 3,56,3
    result = resolve_try_type(a,b,c)
    assert result == "Треугольник равнобедренный"

def test_resolve_try_type_unsoless():
    a,b,c,= 3,3,3
    result = resolve_try_type(a,b,c)
    assert result == "Треугольник равноcторонний"