num=int(raw_input())
factorial=1
if num<=0:
    print "Please enter a non negative number"
else:
    for i in range(1, num+1):
        factorial=factorial*i
    print factorial
