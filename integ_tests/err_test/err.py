
def f ():
	print (x)
	x = 'asdf'
f () # Error

l = [a, '123'+'asdf', 2]
l *= 1.1 #Error


def func (x, y):
	return x + [3, 4] + y

print (func (1, 3)) # Throw TypeError
