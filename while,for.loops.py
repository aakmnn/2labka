i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#остановить текущую итерацию и продолжить со следующей:


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


for x in "banana":
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Не печатать банан:



for x in range(6):
  print(x) 



for x in range(2, 6):
  print(x)