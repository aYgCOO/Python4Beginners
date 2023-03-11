#Sets functions......
# 
list = [12,35,78,90,28]
setting = set(list)
print("Code_1",setting)

print()

su = {85,96,22,55,84,36}
su.add(40)
print("Code_2",su)

print()

seets = {85,96,22,55,84,36}
seets.pop()
print("Code_3",seets)

print()

sees = {85,96,22,55,84,36}
sees.remove(84)
print("Code_4",sees)

print()

szuk = {85,96,22,55,84,36}
szuk.discard(55)
print("Code_5",szuk)

print()

soonoz = {85,96,22,55,84,36}
king_list = [32,88,67,45,10,55] #55 added only one time , because it's already exist
soonoz.update(king_list)
print("Code_6",soonoz)

print()

#Iterating through a set;
a_set = {85,96,22,55,84,36}
for i in a_set:
    print("Iterating through a set....",i)