import pytest
from fractal import Fractal

def test_get_name_capitalize(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: 'triangle')
   result = Fractal.get_input_name()
   assert result == 'Triangle'

def test_get_name_strip(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: '  snowflake  ')
   result = Fractal.get_input_name()
   assert result == 'Snowflake'
   
def test_get_name_lower(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: 'TREE')
   result = Fractal.get_input_name()
   assert result == 'Tree'
   
def test_get_name_value_error(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: 'nazarbaev')
   with pytest.raises(ValueError):
      Fractal.get_input_name()

def test_get_gens_correct(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: '15')
   assert 15 == Fractal.get_gens('Honeycomb')
   monkeypatch.setattr('builtins.input', lambda _: '5')
   assert 5 == Fractal.get_gens('Snowflake')

def test_get_gens_incorrect(monkeypatch):
   monkeypatch.setattr('builtins.input', lambda _: '100')
   with pytest.raises(ValueError):
      Fractal.get_gens('Triangle')
   
   monkeypatch.setattr('builtins.input', lambda _: 'abc')
   with pytest.raises(ValueError):
      Fractal.get_gens('Complex tree')

def test_get_final_gen():
   assert Fractal.get_final_gen('F++F++F', 2, 'Snowflake', 'F', 'F-F++F-F', '', '') == 'F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F'
   assert Fractal.get_final_gen('XY', 4, 'Tree', 'F', 'FF', 'X', 'F[+X]F[-X]+X') == 'FFFFFFFF[+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFFFFFF[-FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+XY'