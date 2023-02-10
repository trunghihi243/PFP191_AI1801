friend =['a','b','c']
for i in friend:
    print("hello",i)
print(len(friend[::-1]))
for i in range(len(friend)):
    print(friend[i])
#############
total=0
count=0
while True:
    inp=input("nhap so ")
    if inp=="done":
        break
    value= float(inp)
    total+=value
    count+=1
av=total/count
print("average=",av)