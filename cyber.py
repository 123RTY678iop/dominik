def binarNum(num,bits):
    place=2**(bits-1)
    binar=[]
    for i in range(0,bits):
        if num >= place :
            binar.append(1)
            num= num-place
        elif num<place:
            binar.append(0)
        elif num==0:
            binar.append(0)
        place= place/2
    return binar

num=int(input('please enter num biger than 9 :__'))
bits=int(input('please enter num of bits  :__'))
binar = binarNum(num,bits)
print(binar)
for i in range(0,bits) : 
    if binar[i]==0:
        binar[i]=1
    elif binar[i]==1:
        binar[i]=0
print(binar)
count=-1
for j in range(1,bits):
    if binar[count]==1:
        binar[count]=0
    elif binar[count]==0:
        binar[count]=1
        break
    count=count-1
print(binar)
