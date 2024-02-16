import pytest
import fonctions as f

def test_regex_password() :
	assert f.validate_password("a") == [True,False,True,False,False]
	assert f.validate_password("aA#123azs") == [True,True,True,True,True]

def test_regex_username() :
	assert f.validate_username("fabien") == [True,True,True]
