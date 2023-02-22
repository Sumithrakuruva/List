# a=[1,2,3,4,5,6,7,8,9,0]
# b=len(a)
# if b==10:
#     print("+"+"("+a[0:3]+")"+"-"+a[3:7]+"_"+a[7:])
# else:
# #     print("no")

# r=3
# c=3
# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         if  i==1 and j==1 or j==2 and i==2 or i==3 and j==3:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j=j+1
    
#     i=i+1
    # print()
    
a=[[1,2,3],4,6]
i=0
b=[]
while i<len(a):
    j=0
    c=a[i]
    sum=0
    while j<len(b):
        sum=sum+a[i][j]
        j=j+1
        b.append(sum)
    i=i+1
print(b)
        

    
    
