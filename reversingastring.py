
lis=[1,2,3,4,5,6,7,8,9,10]
length=len(lis)
a=0
b=length-1
while(a<b):
    c=lis[a]
    lis[a]=lis[b]
    lis[b]=c
    a+=1
    b-=1
print(lis)
