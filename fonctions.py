def puissance(a,b):
	if not type(a) is int :
		raise TypeError ("Only integers are allowed")
	if not type(b) is int :
		raise TypeError ("Only integers are allowed")
	retour = a**b
	
	if (retour < 0) :
		retour = retour *(-1)
	
	return retour
	
