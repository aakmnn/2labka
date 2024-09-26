thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Дубликаты значений будут проигнорированы:


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


thisset = {"apple", "banana", "cherry"}
print(len(thisset))


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#ключевое слово in.


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#добавлять 


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#из другого в другой


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#kosy


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#kosy


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#Присоединиться к set1 и set2, но сохранить только дубликаты:


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)



