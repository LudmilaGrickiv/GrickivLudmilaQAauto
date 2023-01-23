#def test_check_math():
    #assert 7 * 7 == 49


#def test_check_78():
    #assert 7 * 8 == 56


#class User:

    #def __init__(self) -> None:
        #self.name = 'Ludmila'
        #self.second_name = 'Grickiv'


#user = User()   


#def test_remove_name():
    #user.name = ''
    #assert user.name == ''


#def test_name():
    #assert user.name == 'Ludmila'


#def test_second_name():
    #assert user.second_name == 'Grickiv'


import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Ludmila'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Grickiv'    
