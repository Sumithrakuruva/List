# a=[1,2,3,4,5,6]
# i=0
# while i<len(a):
#     x=len(a)-1
#     i=i+1
# print(x)

# a=[1,2,3,4,5,6]
# c=0
# for i in a:
#     c=c+1
# print(c)


# i=-1
# while i>=-10:
#     print(-i)
#     i=i-1

# a=556
# while a<655:
#     if (a-555)%7==0:
#         print(a-555)
#     a=a+1    


# i=156
# i=156-145
# while i<=101:
#     print(i)
#     i=i+1    


# i=0
# while i<=5:
#     print(i)
#     if i==3:

# n=int(input("enter the number"))
# frist=0
# second=1
# for i in range(n):
#     print(frist)
#     temp=frist
#     frist=second
#     second=temp+second  
    


# n=int(input("enter the number"))
# n1=0
# n2=1
# count=0
# while count<n:
#     print(n1)
#     next=n1+n2
#     n1=n2
#     n2=next
#     count=count+1

# i=10
# while i>=1:
#     print(i)
#     i=i-1
    

# c=[1,2,3,4,5]
# i=c[-1]
# while i>=c[0]:
#     print(i,end="")
#     i=i-1


# a=int(input("enter the number"))
# i=1
# count=0
# while i<=a:
#     if a%i==0 and a%a==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print(a,"prime number")
# else:
#     print(a,"not prime number")
# i=i+1


# a=int(input("enter the number"))
# len=len(str(a))
# i=a
# sum=0 
# while i>a:
#     d=a%10**len
#     sum=sum+d
#     a=a//10
# if sum==a:
#     print("arm strong number")
# else:
#     print("arn ")

# i=1
# a=0
# while i<=3:
#     j=1
#     while j<=3:
#         print(0+j,end=" ")
#         j=j+1
#     a=a+1
#     i=i+1
#     print()


# 123
# 234
# 345
# n=int(input("enter the  number"))
# i=1
# r=1
# while i<=3:
#     j=1
#     while j<=3:
#         if i==1:
#             print(r,end=" ")
#         elif i==2 and j==1 or i==2 and j==2 or i==2 and j==3:
#             print(r-2,end=" ")
#         elif i==3 and j==1 or i==3 and j==2 or i==3 and j==3:
#             print(r-4,end=" ")
#         j=j+1
#         r=r+1
#     i=i+1
#     print()
       
# i=1
# a=0
# while i<=3:
#     j=1
#     while j<=3:
#         print(a+j,end=" ")
#         j=j+1
#     a=a+1
#     i=i+1
#     print()
    
# user=4
# num=5
# i=0
# while i<1:
#     j=0
#     while j<num:
#         print(user,end=" ")
#         user=str(user)+str(i)
#         j=j+1
#     i=i+1


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     k=1
    
#     while k<=n-i:
#         print(" ",end=" ")
#         k=k+1
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
        
#     i=i+1
#     print()


# count=150
# i=150-149
# while i<=50:
#     print(i)
#     i=i+1

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if j<i:
#             print("*",end=" ")
#         else:
#             print(i)
#         j=j+1
#     i=i+1
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print((i+j)%2,end=" ")
#         j=j+1
#     i=i+1
#     print()
    
    
# n=int(input("enter the number"))
# a=n
# while a>=10:
#     sum=0
#     while a>0:
#         b=a%10
#         sum=sum+(b**2)
#         a=a//10
#     a=sum
# if a==1:
#         print(n,"is happy number")
# else:
#         print(n,"is not a happy number")


# n=int(input("enter the number"))
# a=n
# sum=0
# while a>0:
#     fact=1
#     r=a%10
#     while r:
#         fact=fact*r
#         r=r-1
#         sum=sum+fact
#         a=a//10
# if sum==n:
#     print(n,"strong number")
# else:
#     print(n,"is not strong number")


# n=int(input("enter the number"))
# l=[]
# i=1
# while i<=n:
#     ele=int(input("enter the number"))
#     l.append(ele)
#     i=i+1
# print(l)
# b=l[::-1]
# if l==b:
#     print("pal")
# else:
#     print("not pal")


# l=[6,1,3,5,6,3,1]
# i=0
# b=[]
# while i<len(l):
#     if l[i] not in b:
#         b.append(l[i])
#     i=i+1
# print(b)
# i=0
# p=1
# while i<len(b):
#     p*l[i]
#     i=i+1
# print(p)

# l=[6,1,3,5,6,3,1]
# i=0
# b=[]
# while i<len(l):
#     if l[i] not in b:
#         b.append(l[i])
#     i=i+1
# print(b)


a="123"
b=list(a)
i=-1
c=[]
while i>=-len(b):
    c.append(int(a[i]))
    i=i-1
print(c)
    