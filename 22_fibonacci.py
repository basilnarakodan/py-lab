def fib(n):
    a=0
    b=1
    print(a,b)
    for i in range(n):
        c=a+b
        print(c)
        a=b
        b=c


a=int(input("enter limit: "))
fib(a)
        
