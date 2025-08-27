# criar uma eaquação de segundo grau : a**2 + bx + c

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))


if a == 0:
	print('0 valor de a não pode ser 0, pois se o valor de a for 0, não é uma equação de segundo grau, torna-se uma equação de primeiro grau entao digite um valor diferente de 0')
else:
	delta = (b**2) - 4*a*c
	x1 = (-b + (delta**0.5)) / (2*a)
	x2 = (-b - (delta**0.5)) / (2*a)
	print(f'{x1} e {x2}')


#fim do codigo