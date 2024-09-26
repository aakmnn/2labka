#Списки используются для хранения нескольких элементов в одной переменной.

thislist = ["apple", "banana", "cherry"]
print(thislist)


#списки могут иметь элементы с одинаковым значением:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#Чтобы определить, сколько элементов в списке, используйте функцию len():

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


mylist = ["apple", "banana", "cherry"]

print(type(mylist))


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  #рисутствует ли указанный элемент в списке, используйте ключевое слово in:


  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#change


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Чтобы добавить элемент в конец списка, используйте метод append():
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Чтобы привить элементы из другого списка в текущий список, используйте метод extend()


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#удаляет 


thislist = ["apple", "banana", "cherry"]
del thislist


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#Распечатайте все элементы в списке, один за другим:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Вы можете просматривать элементы списка, используя цикл while

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  
#Короткий цикл for, который печатает все элементы в списке.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)