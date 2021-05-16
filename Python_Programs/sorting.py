from operator import itemgetter

record = [
    {'name':'Nick', 'score':9, 'age':18},
    {'name':'Rob', 'score':8, 'age':19},
    {'name':'Sam', 'score':7, 'age':18},
    {'name':'Harry', 'score':6, 'age':20},
    
]

sorting = sorted(record, key=itemgetter('score', 'age'))

print(sorting)