from main import jadd

def test_jadd_two_positives():
    result = jadd(4,2)
    assert result == 6

def test_jadd_two_negatives():
    result = jadd(-4,-2)
    assert result == -6

def test_jadd_mixed():
    result = jadd(-4,2)
    assert result == -2

