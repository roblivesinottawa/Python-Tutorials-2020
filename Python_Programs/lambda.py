from functools import reduce


# this function returns all the positive numbers
_list = [1,-2,3,-4,5,6]
pos = list(filter(lambda x: x>=0, _list))
print(pos)

# this function returns the product 
_list1 = [1,2,3,4,5]
prod = reduce(lambda x,y : x*y, _list1)
print(prod)

# this function returns the greatest number on the list
list_ = [1,39,40,100,3999]
greatest = reduce((lambda x,y: y if y>x else x), list_)
print(greatest)

