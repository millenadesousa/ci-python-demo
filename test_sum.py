from sum import sum 

def test_sum_positivos():
    assert sum(1, 2) == 3

def test_sum_negativos_e_zero():
    assert sum(-1, 1) == 0

def test_sum_zeros():
    assert sum(0, 0) == 0
    
