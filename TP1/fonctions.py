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
	
	#-----------------------
	if b < 0 :
		bb = b* -1
	else :
		bb = b
	#-----------------------
	#Les conditions ci dessus me permettent d'avoir b intact pour le réutiliser plus tard en cas d'exposant négatif
	
	#-----------------------
	retour = float(a)
	#----------------------- 
	# calcul de a puissance 1
	

	# si b = 1, le résultat est deja calculer donc pas besoin de la boucle 
	if bb != 1 : 
		for i in range(bb-1) :
			retour = retour * a
	
	if b < 0 : # calcul du résultat final si l'exposant est négatif
		retour = 1/retour
	
	return retour
