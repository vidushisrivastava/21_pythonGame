import random
num_list=[]
n=1
flag=0
while n<6:
    num=random.randint(1,3)
    num_list.append(num)
    for i in range(1,4):
        count=num_list.count(i)
        if count==3:
            flag=1
            n=7
            break
    n=n+1
if flag==0:
    print("no number thrice")
else:
    print("got %d thrice"%(i))
print(num_list)
