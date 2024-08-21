from math import sqrt
a = float(input('qual o valor de a'))
b = float(input('qual o valor de b'))
c = float(input('qual o valor de c'))

delta = sqrt((b**2)-4*a*c)
print(f'X1 = {(-b + delta)/2}')
print(f'X2 = {(-b - delta)/2}')

# delta deve ser positivo e inteiro (0;4;0)