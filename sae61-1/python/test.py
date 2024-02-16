import pytest
import fonctions as f

def test_regex_password() :
	assert f.validate_password("a") == [False,False,True,False,False]
	assert f.validate_password("aA#123azs") == [True,True,True,True,True]
