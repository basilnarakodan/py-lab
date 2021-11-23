def occurence(str):
    count=dict()
    words=str.split()
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i]=1
    return count
str=input("enter a sentance\n")
print(occurence(str))


#a=input("enter some words:")
#b=a.split(" ")
#for i in b:
#    print(i,"->",b.count(i),"times")

