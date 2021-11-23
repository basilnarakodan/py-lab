a=int(input("enter a number"))
sum=0
temp=a
while(a!=0):
    digit=a%10
    sum=sum+digit**3
    a=a//10
if sum==temp:
	print(temp,"is armstrong")
else:
	print(temp,"is not armstrong")
