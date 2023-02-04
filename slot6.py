def check(p):
    x= input(p)
    flag = 0
    while flag==0:
        try:
            x=int(x)
        except:
            print("error, hay nhap lai so")
            x= input(p)
        else:
            flag = 1
    return x
def tamgiacrong(n):
    for i in range(1, n+1 ):
        if i == 1:
            print("*")
        elif i<n:
            print("*" + " " * (i - 2) + "*")
        else :
            print("*" * n)
h= check(("h="))
tamgiacrong(h)


##################################



s=input("enter string s:")
nl=0
nn=0
no=0
index=0
while index<len(s):
    for char in s:
        if char.isalpha():
            nl += 1
        if char.isdigit():
            nn+=1
        if not char.isalnum():
            no+=1
        index+=1   
            
print("number of letter: =", nl)
print("number of number: =" ,nn)
print("number of orther: =" ,no)

##################################
s = "hello, world"
mang = {}
for char in s:
    if char in mang:
        mang[char] += 1
    else:
        mang[char] = 1

print("số lần xuất hiện của từng kí tự:", mang)
####################################
b=s.replace('o','c')
print(b)

