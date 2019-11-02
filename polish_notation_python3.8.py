pl = lambda *m:[(r:=(r+m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1] #plus
mi = lambda *m:[(r:=(r-m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1] #minus
di = lambda *m:[(r:=(r/m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1] #division
mu = lambda *m:[(r:=(r*m[i])) if i!=0 else (r:=m[i]) for i in range(len(m))][-1] #multiplication

print(pl(4,di(5,2),mi(6,2,mu(10,2,1.6),19),2))
