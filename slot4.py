#q1
#cach1######################################################
# def check(p):
#     x= input(p)
#     flag = 0
#     while flag==0:
#         try:
#             x=int(x)
#         except:
#             print("error, hay nhap lai so")
#             x= input(p)
#         else:
#             flag = 1
#     return x
# def fac(x):
#     x=int(x)
#     f=1
#     for i in range (1,x+1):
#         f*=i
#     return f
# n= chech(("n="))
# print(fac(n))
#cach2#####################################3
# n = check(('Enter the n: '))
# def giaithua(n):
#     if n == 0:
#         return 1
#     return n*giaithua(n-1)
# print(giaithua(n))



















#q2###################################################
# import math
# def check(p):
#     x= input(p)
#     flag = 0
#     while flag==0:
#         try:
#             x=int(x)
#         except:
#             print("error, hay nhap lai so")
#             x= input(p)
#         else:
#             flag = 1
#     return x
# m= check(("m="))
# n= check(("n="))
# print(math.gcd(m,n))

#cach2##########################
# def check(p):
#     x= input(p)
#     flag = 0
#     while flag==0:
#         try:
#             x=int(x)
#         except:
#             print("error, hay nhap lai so")
#             x= input(p)
#         else:
#             flag = 1
#     return x
# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# 
# a= check(("a="))
# b= check(("b="))
# print(gcd(a,b))




















# #q3#############################################
# import math
# def check(p):
#     x= input(p)
#     flag = 0
#     while flag==0:
#         try:
#             x=float(x)
#         except:
#             print("error, hay nhap lai so")
#             x= input(p)
#         else:
#             flag = 1
#     return x
# try:
#     a= check(('a='))
#     b= check(('b='))
#     c= check(('c='))
#     s = (b**2)-4*a*c
#     if (a == 0):
#         if (b == 0):
#             print ('no roots exists')
#         else:
#             print ('root(s)=',(-c / b))
#     if(a!=0)  : 
#         if (s>0):
#             x1 = ((-b + math.sqrt(s)) / (2 * a))
#             x2 = ((-b - math.sqrt(s)) / (2 * a))
#             #print ("Phương trình có 2 nghiệm là: x1 = ",'{0:.{1}f}'.format(x1,3), " và x2 = ",'{0:.{1}f}'.format(sx2,3));
#             print ('root(s)=',x1)
#             print ('root(s)=',x2)
#         elif (s==0):
#             x=-b/2*a
#             print ( 'root(s)=', x)
#         else:
#             print('no roots exists')
# except:
#     print ('hay nhap cac so ')
#     


























# #####################################q4
# import math
# def check(p):
#     x= input(p)
#     flag = 0
#     while flag==0:
#         try:
#             x=int(x)
#         except:
#             print("error, hay nhap lai so")
#             x= input(p)
#         else:
#             flag = 1
#     return x
# def PrimeNum(n):
#     if n < 2:
#         return False
#     x = int(math.sqrt(n))
#     for i in range(2, x + 1):
#         if (n % i) == 0:
#             return False
#     return True
# 
# 
# n = check(('Nhap vao so nguyen duong n = '))
# if n >= 2:
#     print(2)
#     for i in range(3, n + 1):
#         if PrimeNum(i):
#             print(i)
