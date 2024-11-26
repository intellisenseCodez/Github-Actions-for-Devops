from src.app import addNum, subNum

def test_add():
    assert addNum(3, 7) == 10
    assert addNum(1, 2) == 3
    
    
def test_sub():
    assert subNum(3, 7) == -4
    assert subNum(2, 1) == 1