x=[1,2,3,4]

x1 = x

x1[1]=10
print(x)
# x2=x.copy()
x2=[]
x2[:]=x
x2[1]=100
print(x)
print(x2)