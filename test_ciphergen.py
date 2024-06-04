import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
from io import StringIO
from project_class import Settings, color
from project import execute, exe_len, exe_enable, exe_disable, exe_number, exe_special, exe_reset


def test_exe_len():
    obj = Settings()
    
    value = 10
    exe_len(obj, value)
    assert obj.len == value
    
    value = '7'
    exe_len(obj, value)
    assert obj.len == int(value)
    
    # Arg is not an integer
    with pytest.raises(TypeError):
        assert exe_len(obj, 'hello')

    # Arg is not in the range 5 to 128
    with pytest.raises(ValueError):
        assert exe_len(obj, 3)

    # Arg is lower than the total of min numbers and specials
    obj.min_number = 9
    with pytest.raises(ValueError):
        assert exe_len(obj, 5)
        
def test_exe_enable():
    obj = Settings()
    
    exe_enable(obj, 'uppercase')
    assert obj.uppercase == True
    
    exe_enable(obj, 'lowercase')
    assert obj.lowercase == True

    exe_enable(obj, 'number')
    assert obj.number == True

    exe_enable(obj, 'special')
    assert obj.special == True
    
    # Arg is not valid
    with pytest.raises(Exception):
        assert exe_enable(obj, 'hello')

def test_exe_disable():
    obj = Settings()
    
    exe_disable(obj, 'uppercase')
    assert obj.uppercase == False
    
    exe_disable(obj, 'lowercase')
    assert obj.lowercase == False

    exe_disable(obj, 'number')
    assert obj.number == False

    # Cannot disable all character types
    with pytest.raises(ValueError):
        assert exe_disable(obj, 'special')
    
    # Arg is not valid
    with pytest.raises(Exception):
        assert exe_disable(obj, 'hello')

def test_exe_number():
    obj = Settings()
    
    value = 3
    exe_number(obj, value)
    assert obj.min_number == value

    value = 9
    exe_number(obj, value)
    assert obj.min_number == value
    assert obj.len == 13
    
    # Arg is not an integer
    with pytest.raises(TypeError):
        assert exe_number(obj, 'number')

    # Arg is not in the range 1 to 9
    with pytest.raises(ValueError):
        assert exe_number(obj, 0)
    
    # Cannot set mininum value if numbers are disabled 
    obj.number = False
    with pytest.raises(AttributeError):
        assert exe_number(obj, 4)
    
def test_exe_special():
    obj = Settings()
    
    value = 2
    exe_special(obj, value)
    assert obj.min_special == value

    value = 9
    exe_special(obj, value)
    assert obj.min_special == value
    assert obj.len == 13
    
    # Arg is not an integer
    with pytest.raises(TypeError):
        assert exe_special(obj, 'special')

    # Arg is not in the range 1 to 9
    with pytest.raises(ValueError):
        assert exe_special(obj, 10)

    # Cannot set mininum value if numbers are disabled 
    obj.special = False
    with pytest.raises(AttributeError):
        assert exe_special(obj, 2)

def test_exe_res(monkeypatch):
    obj = Settings()
    
    # User input yes
    monkeypatch.setattr('sys.stdin', StringIO('y\n'))
    exe_reset(obj)
    assert obj.uppercase == True
    assert obj.lowercase == True
    assert obj.number == True
    assert obj.special == True
    assert obj.min_number == 1
    assert obj.min_special == 1
    assert obj.len == 5
    
    # User input no
    monkeypatch.setattr('sys.stdin', StringIO('n\n'))
    with pytest.raises(Exception):
        assert exe_reset(obj)

    # User input else
    monkeypatch.setattr('sys.stdin', StringIO('hello\n'))
    with pytest.raises(ValueError):
        assert exe_reset(obj)

def test_exit():
    obj = Settings()
    
    with pytest.raises(SystemExit):
        assert execute(obj, '.exit')