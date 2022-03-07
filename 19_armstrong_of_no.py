a=int(input("enter no: "))
l=len(str(a))
sum=0
temp=a
while(a!=0):
    digit=a%10
    sum=sum+digit**l
    a=a//10
if (temp==sum):
    print("armstrong")
else:
    print("not armstrong")
