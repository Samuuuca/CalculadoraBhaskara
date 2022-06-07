a = int(input('Valor de a? \n'))
b = int(input('Valor de b? \n'))
c = int(input('Valor de c? \n' ))

delta = b**2 - 4 * a * c
raizDelta = delta**0.5


x1 = (-b + raizDelta) / (2 * a) 
x2 = (-b - raizDelta) / (2 * a)

bask = x1, x2

print(sorted(bask))
