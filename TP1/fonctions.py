def puissance(a,b):
	if not type(a) is int :
		raise TypeError ("Only integers are allowed")
	if not type(b) is int :
		raise TypeError ("Only integers are allowed")
	if b == 0 :
		if a < 0 :
			return -1
		else :
			return 1
	if a == 0 & b<0 : #exception p0 puissance négative
		raise TypeError ("0 avec une puissance négative impossible")
	
	#return a**b
	
	if b < 0 :
		bb = b* -1
	else :
		bb = b
	
	retour = float(a)
	
	if bb != 1 :
		for i in range(bb-1) :
			retour = retour * a
	
	if b < 0 :
		retour = 1/retour
	
	return retour
