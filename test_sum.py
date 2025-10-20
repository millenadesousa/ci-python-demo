from soma import soma 

def teste_soma_positivos():
    assert soma(1, 2) == 3

def teste_soma_negativos_e_zero():
    assert soma(-1, 1) == 0

def teste_soma_zeros():
    assert soma(0, 0) == 0
    
