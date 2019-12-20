import numpy
a=numpy.array(input("enter an array :\n"))
b=c=d=numpy.array(input("enter another array:\n"))
l=len(a)
for i in range(0,l):
	b=numpy.append(b,a[i])
print b;
for i in range(0,l):
	if(a[i]%2==0):
		c=numpy.append(a[i],c)
print c;
for i in range(0,l):
	if(a[i]>5):
		d=numpy.append(a[i],d)
print d;







