def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
    

a=int(input("enter a no: "))
print(fact(a))

