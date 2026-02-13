names = " alex; john; maria; anna; bob "
new_names = names.split(";")
#new_names = names.split("-")#this will separate the values wherever it will find "-"
new_names = [name.strip() for name in new_names] #this removes extra spaces
print(new_names)


