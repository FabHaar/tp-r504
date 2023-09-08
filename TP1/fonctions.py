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
	if a == 0 & b<0 :
		raise TypeError ("0 avec une puissance négative impossible")
	
	return a**b
