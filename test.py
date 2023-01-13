
import math
try:
    a= float( input('a='))
    b= float( input('b='))
    c= float( input('c='))
    s = (b**2)-4*a*c
    if (a == 0):
        if (b == 0):
            print ('no roots exists')
        else:
            print ('root(s)=',(-c / b))
    if(a!=0)  : 
        if (s>0):
            x1 = ((-b + math.sqrt(s)) / (2 * a))
            x2 = ((-b - math.sqrt(s)) / (2 * a))
            #print ("Phương trình có 2 nghiệm là: x1 = ",'{0:.{1}f}'.format(x1,3), " và x2 = ",'{0:.{1}f}'.format(sx2,3));
            print ('root(s)=',x1)
            print ('root(s)=',x2)
        elif (s==0):
            x=-b/2*a
            print ( 'root(s)=', x)
        else:
            print('no roots exists')
except:
    print ('hay nhap cac so ')
#
# #q1
# import math
# try:
#     a= float( input('a='))
#     b= float( input('b='))
#     c= float( input('c='))
#     s = (b**2)-4*a*c
#     if (a == 0):
#         if (b == 0):
#             print ('no roots exists');
#         else:
#             print ('root(s)=', '{0:.{1}f}'.format((-c / b),3));
#     if(a!=0)  : 
#         if (s>0):
#             x1 = ((-b + math.sqrt(s)) / (2 * a))
#             x2 = ((-b - math.sqrt(s)) / (2 * a))
#             #print ("Phương trình có 2 nghiệm là: x1 = ",'{0:.{1}f}'.format(x1,3), " và x2 = ",'{0:.{1}f}'.format(sx2,3));
#             print ('root(s)=','{0:.{1}f}'.format(x1,3))
#             print ('root(s)=','{0:.{1}f}'.format(x2,3))
#         elif (s==0):
#             x=-b/2*a
#             print ( 'root(s)=', x)
#         else:
#             print('no roots exists')
# except:
#     print ('hay nhap cac so nguyen')
# 
# # #q2
# # for i in range (1,6):
# #     s='*'*i
# #     print(s)
# # #q3
# # def prime(n):
# #     for i in range (2, int(n/2)+1):
# #         if n %i == 0:
# #             return False
# #     return True                  
# # while True:
# #     try:
# #         n = int(input('n='))
# #         if n > 0:
# #             break
# #     except:
# #         print('nhap lai n')
# # for i in range (2, n+1):
# #     if n % i ==0:
# #         if(prime(i)==True):
# #             print(i, end =' ')
