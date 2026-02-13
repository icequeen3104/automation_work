"""     The Advanced Inversion (One-to-Many)
In the real world, dictionaries often have duplicate values. If you use the method above on {'a':
1, 'b': 1}, the second '1' will overwrite the first, and you'll lose data.
To invert correctly, you must map the value to a list of keys.
Problem: Write a function that inverts a dictionary where the values are lists, such as {"Python":
["Alice", "Bob"], "Java": ["Bob", "Charlie"]}.
Goal: The output should show which languages each person knows: {"Alice": ["Python"], "Bob":
["Python", "Java"], "Charlie": ["Java"]}     """

#given input
'''data = {
    "Python": ["Alice", "Bob"],
    "Java": ["Bob", "Charlie"]
}'''

#user input
m = int(input("Enter the range of dictionary: "))
data = {}
n = int(input("enter the range of list: "))
for i in range(m):
    lis = []
    for j in range(n):
        value = input("Enter values: ")
        lis.append(value)
    key = input("Enter key: ")
    data[key] = lis

print("original user input: ", data)

inverted = {}

for language, people in data.items():
    for person in people:
        if person not in inverted:
            inverted[person] = []
        inverted[person].append(language)

print("inverted user input: ", inverted)
