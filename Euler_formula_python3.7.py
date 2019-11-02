import functools

Euler = lambda n: sum(1/(functools.reduce(lambda x,y: x * y, [x for x in range(1,i+1)]) ) for i in range(1,n)) + 1

Euler(100)
