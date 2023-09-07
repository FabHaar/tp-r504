import fonctions as f

print(" Hello, World ! ")

while True :
	nombre = int(input ("Saisir un nombre pour afficher son carré : "))
	print (nombre*nombre)
	
	v1 = int(input("indiquer un nombre : "))
	v2 = int(input("et sa puissance : "))
	res = f.puissance (v1,v2)
	print (res)

