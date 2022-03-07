a=int(input("enter no: "))
f=0
for i in range(1,a):
    if(a%i==0):
        f=f+1
if f>1:
    print("not prime")
else:
    print("prime")
    
