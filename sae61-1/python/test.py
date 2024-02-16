import pytest
import fonctions as f

def test_1() :
	assert f.validate_password("a") == [False,False,True,False,False
