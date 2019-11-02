X = [201,225,305,380,560,600,685,735]
Y = [17,20,21,23,25,24,27,27]

linear_regression = lambda X,Y,predict : [((sum(Y)/(N:=len(X)))-(b1:=(((N*sum([X[i]*Y[i] for i in range(N)]))-((sX:=sum(X))*sum(Y)))/(N*sum([x**2 for x in X])-sX**2)))*(sX/N))+b1*pred for pred in predict]

print(linear_regression(X,Y,X))
