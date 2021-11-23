a=int(input("enter the year "))
if(a%100==0):
    if(a%400==0):
        print(a,"is leap year")
    else:
        print(a,"is not leap year")
elif(a%4==0):
    print(a,"is leap year")
else:
    print(a,"is not leap year")
    

    
