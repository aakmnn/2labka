print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15
print(bool(x))
print(bool(y))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))


x = 5
y = 3

print(x + y)



x = 5
y = 3

print(x - y)


x = 5
y = 3

print(x * y)


x = 12
y = 3

print(x / y)


x = 5
y = 2

print(x % y)


x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2


x = 15
y = 2

print(x // y)
#the floor division // rounds the result down to the nearest whole number

#для присвоения значений переменным:
x = 5
x//=3
print(x)


x = 5
x **= 3
print(x)

x = 5
x &= 3
print(x)


x = 5
x |= 3
print(x) #непон

x = 5
x ^= 3
print(x)


x = 5
x >>= 3
print(x)
