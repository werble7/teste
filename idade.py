x= int(input('Qual a sua idade? '))

if x > 50:
	print('Que experiente!')
else:
	pass

if x >= 18:
	print('A habilitação te aguarda!')
else:
	print('Só mais um pouquinho para dirigir')

y = None

if x >= 16:
	y= input('Já votou esse ano? ')
else:
	print('Já já vai poder votar!')

if y != None:
	if y=="sim":
		z= input("Qual? B ou H? ")
		if z=="B":
			print("Bolsominion")

		if z=="H":
			print("O Lula tá preso babaca!")

	if y=="não" or y=="nao":
		print("Luciano Huck para presidente")


