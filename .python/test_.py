import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import syracuse, temps_de_vol, temps_de_vol_en_altitude, altitude_maximale


def test_misc():
    l129 = syracuse(129)
    assert isinstance(l129, list) == True
    assert len(l129) == 122
    assert l129[15:19] == [188, 94, 47, 142]
    assert len(syracuse(27)) == 112
    assert len(syracuse(31)) == 107
    assert len(syracuse(41)) == 110


input_output = [(3, [3, 10, 5, 16, 8, 4, 2, 1]), (4, [4, 2, 1]), (5, [5, 16, 8, 4, 2, 1]), (6, [6, 3, 10, 5, 16, 8, 4, 2, 1])]

@pytest.mark.parametrize("input,expected", input_output)
def test_sl(input, expected):
    assert syracuse(input) == expected, input


input_output = [(3, 7), (4, 2), (5, 5), (6, 8)]

@pytest.mark.parametrize("input,expected", input_output)
def test_tv(input, expected):
    assert temps_de_vol(syracuse(input)) == expected, input

input_output = [(3, 5), (4, 0), (5, 2), (6, 0)]

@pytest.mark.parametrize("input,expected", input_output)
def test_tva(input, expected):
    assert temps_de_vol_en_altitude(syracuse(input)) == expected, input

input_output = [(3, 16), (4, 4), (5, 16), (6, 16)]

@pytest.mark.parametrize("input,expected", input_output)
def test_am(input, expected):
    assert altitude_maximale(syracuse(input)) == expected, input

