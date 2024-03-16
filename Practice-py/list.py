#List in python
'''
In Python, a list is a collection of items, where each item can be of any data type. Lists are mutable, meaning they can be modified after creation. They are denoted by square brackets [ ], and items within the list are separated by commas. 
Lists can contain elements of different data types, including other lists'''

myFriends = ['Agnik', 'Shivam', 'Jeet', 'Vivak', 'Swrup', 'Souvik', 'Debdhoot', 'Corona']
print(myFriends)
print(type(myFriends))
'''Access the elements in the list by using the indexed number'''
print(myFriends[2])
print(myFriends[0:4])
print(myFriends[0:4:3])

''' Define a list of numbers '''
numbers = [1, 2, 3, 4, 5]
print(numbers)

''' Define a list of strings '''
fruits = ["apple", "banana", "orange"]
print(fruits)

''' Define a list with mixed data types '''
mixed_list = [10, "hello", True, 3.14]
print(mixed_list)

''' Define a list of lists (nested list) or 2d list '''
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)



