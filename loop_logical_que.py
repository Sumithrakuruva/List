# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass
# print("Letters", l)
# print("Digits", d)


# countiune= skip the current itreation :

# i=0
# while i<10:
#     i=i+1
#     if i==6:
#         continue
#     else:
#         print(i)
        
# a=891
# while a<930:
#     c=a-890
#     print(c)
#     a=a+1
    
    


a=[1,2,3,4]
# o/p=[1,3,6,10]
i=0
sum=0
b=[]
while i<len(a):
    sum=sum+a[i]
    i=i+1
    b.append(sum)
    print(sum) 
print(b)      
    