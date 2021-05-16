import converters
from larg_nums import find_max

#
print("converting weight")
converted = converters.kg_to_lbs(70)
print(converted)

#
print("finding the largest number")
numbers = [100, 5000, 500, 20, 90, 45]
maximum = find_max(numbers)
print(maximum)
