a=int(input("enter number of levels: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j,end="\t")
    print("\n")
