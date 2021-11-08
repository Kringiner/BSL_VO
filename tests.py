from vector import Vector


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    result = v1.add(v2)
    assert result == Vector(2, 4)
    result = v1.subtract(v2)
    assert result == Vector(0, 0)
    result = v1.scalar_mult(v2)
    assert result == 5
