"""The Basic Inversion (One-to-One)
If every value in your dictionary is unique, you can use a simple dictionary comprehension.
Original: {'a': 1, 'b': 2, 'c': 3}
Inverted: {1: 'a', 2: 'b', 3: 'c'} """

n = int(input("enter a range of dictionary: ")) #user input
dict = {}
#new_dict = {}
for i in range(n):
    key = input("enter key: ")
    value = input("enter value: ")
    dict[key] = value
print("original dictionary: ", dict)

#invert a dictionary using for loop
"""for j in dict:
    a = dict[j]
    new_dict[a] = j
print("inverted dictionary: ", new_dict)"""

#invert a dictionary using dictionary comprehension
new_dict = {value : key for key, value in dict.items()}
print("inverted dict: ", new_dict)


