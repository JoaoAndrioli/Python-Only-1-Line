add = lambda *m:[(r:=(r+m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1]
sub = lambda *m:[(r:=(r-m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1]
mul = lambda *m:[(r:=(r/m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1]
div = lambda *m:[(r:=(r*m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1]

print(add(2,3,6,3,sub(8,5,mul(2,3,2)),div(3,7)))
