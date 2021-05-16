
# introduction to zip
# zip connects everything together
name = ['Rob', "Vick", "Sam"]
age = [30,31,32]
grade = ['A', 'A', 'C']

for n in zip(name, age, grade):
	print(n)


# 
my_list = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]
print(my_list)

for num in zip(*my_list):
	print(num)












# midterms = [80,91,78]
# finals = [98,89,53]
# students = ['dan', 'ang', 'kate']


# # returns dict with {student:highest score} USING LIST COMP
# # {'dan': 98, 'ang': 91, 'kate': 78}
# final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# # returns dict with {student:highest score} USING MAP+LAMBDA
# # {'dan': 98, 'ang': 91, 'kate': 78}
# final_grades = dict(
# 	zip(
# 		students,
# 		map(
# 			lambda pair: max(pair),
# 			zip(midterms, finals)
# 		)
# 	)
# )

# # returns dict with student:average score
# # {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
# avg_grades = dict(
# 	zip(
# 		students,
# 		map(
# 			lambda pair: ((pair[0]+pair[1])/2),
# 			zip(midterms, finals)
# 		)
# 	)
# )































# # r = dict(zip(students, midterms))
# print(r)

# r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
# print(r)

# r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
# print(r)


# z = zip(
# 	students,
# 	map(
# 		lambda pair: max(pair),
# 		zip(midterms, finals)
# 	)
# )

