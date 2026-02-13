#numbers = [int(i) for i in range(0,20)]
#print(numbers) #print the range in the list

#numbers = [int(i) for i in range(0,20) if i%2 != 0] #example of ternary operator(if-else block in the same line)
#print(numbers) #print the odd numbers only

#enter a set of names in a list
names = []
n = int(input("enter the range of name u want to enter: "))
for i in range(n):
    name = input("enter names: ")
    names.append(name)
print(names)
names.insert(1,"raju") #use "insert" to add a particular value at a particular index
print(names)
