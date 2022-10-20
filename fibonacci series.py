num=50
a,b=0,1
print("fibonacci series: ",a,b,end=" ")
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print()
