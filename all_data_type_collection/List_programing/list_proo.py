thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print('1',thislist)

thislist = ["apple", "banana", "cherry"]
print('2',thislist[1])
#change the items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print('3',thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print('4',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print('5',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print('6',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print('7',thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print('8',thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print('9',thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print('10',thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print('11',thislist[i])



thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
