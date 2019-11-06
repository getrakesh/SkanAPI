import pytest

@pytest.mark.parametrize("num, output",[(1,1),(2,2),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output