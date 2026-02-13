names = []
n = int(input("enter a range: "))
for i in range(n):
    name = input("enter names u want to insert: ")
    names.append(name)
new_names_complete = names[::-1] #it will print all the values
new_names = names[::-2] #it will print reverse+alternative values
print(new_names_complete)
print(new_names)


