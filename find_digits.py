l=raw_input()
c=0
for i in str(l):
    if i!='0' and int(l)%int(i)==0:
        c=c+1
print c
