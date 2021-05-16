my_list = []
for x in range(1, 11):
    my_list.append(x**2)

print(my_list)

# using a list comprehension
my_list2 = [y**2 for y in range(1,11)]
print(my_list2)

# another example 
L = [3,8,9,7,-1,11]
odds = [num for num in L if num%2!=0]
print(odds)




result = []