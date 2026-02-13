#list = [i**2 for i in range(1,20)]
#print(list)

#list = [int(i) for i in range(1,20) if i%3==0 and i%5 != 0]
#print(list)

list = []
n = int(input("enter a range: "))
for i in range(n):
    names = input("enter names u want to insert: ")
    list.append(names)
print(list)
upper_case = [j.upper() for j in list]
print(upper_case)



