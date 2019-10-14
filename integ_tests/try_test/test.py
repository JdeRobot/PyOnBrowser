a = 1.3 + 123
l = [a, '123'+'asdf', 2]
print (l)
print (l[1])
t = (1, 2, 3)
print (t[-1])
a, b = 10, 12
s = 'asdf'
if (a == 10 and s == 'asdf' and a is a):
	print ('Works!')
for x in [1,2,3]:
	print (x)

for x in range (-10, 10, 5):
	print (x)

def func (x, y):
	return x + y

print (func (1, 2)) # 3
print (func ([1, 2], [3, 4])) # [1, 2, 3, 4]

def func (): pass

print (func ()) # None

def func (x, y):
	return x + [3, 4] + y

print (func ([1, 2], [5, 6]))
x = 12
def f ():
	global x
	print (x)
	x = 'asdf'
f()
print (x) #asdf


a = 1
while (a < 5):
	print (a)
	a += 10
print (a)
