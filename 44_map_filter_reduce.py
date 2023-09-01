# MAP
def cube(x):
    return x*x*x
    print(cube(x))

l = [2,12,8,3,7,5]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl) or

newl = list(map(cube,l))
print(newl)

# FILTER
# def filter_function(a):
#     return a>4
# newnewl = list(filter(filter_function,l))
# print(newnewl)

# REDUCE
from functools import reduce
def mySum(x,y):
    return x + y
sum = reduce(mySum,l)
print(sum)
