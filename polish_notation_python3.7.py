from functools import reduce   #sadly we have an import, although it can me made without it
add = lambda *args: reduce(lambda x,y: x+y,[x for x in args])
sub = lambda *args: reduce(lambda x,y: x-y,[x for x in args])
mul = lambda *args: reduce(lambda x,y: x*y,[x for x in args])
div = lambda *args: reduce(lambda x,y: x/y,[x for x in args])

print(add(2,3,6,3,sub(8,5,mul(2,3,2)),div(3,7)))
