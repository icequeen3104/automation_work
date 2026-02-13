#list = [[1], [2,[2,3]], [3,4,5], [6,7,8,9], [10]]
##r_list = [i for sublist in list for i in sublist]
# result_list = [int(i) for sublist in list for i in sublist if i%2==0] #list comprehension
#print("new list:", r_list)
# print("new list with only even numbers: ", result_list)
#[1,[2,3,[4,5,[6,7]]]]



def flatten(lis):
    r = []
    for item in lis:
        if isinstance(item, list):
            r.extend(flatten(item))
        else:
            r.append(item)
    return r
lis = [1,[2,3,[4,5,[6,7]]]]
print(flatten(lis))