#names = " alex, john, maria, anna, bob "
#new_names = names.split(",")
#new_names = names.split("-")#this will not separate into a set of values in list, it will only show one value in list
#print(new_names)

names = [" alex; john; maria; anna; bob "]
names= [name.strip() for name in names] #remove the extra spaces in the list in the last and the beginning
print(names)


