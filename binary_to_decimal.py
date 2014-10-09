A=raw_input()
num=-1
b=A.split()
b = map(int, b)
sum=0
for i in reversed(b):
	num=num+1
	res=b[i]*pow(2,num)
	sum=sum+res
print sum
