# a=['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Check if a substring presents in the said list of string values:
# True
# Substring to search:
# abc
# Check if a substring presents in the said list of string values:
# False


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     a=int(input("enter the number"))
    
#     lar=0
#     small=1000
# if a>lar:
#     lar=a
# if a<small:
#     small=a
# i=i+1
# print("lar",a)
# print("small",a)


# i=0
# l=0
# s=1000
# while i<10:
#     user=int(input("enter the number"))
#     if user>l:
#         l=user
#     elif user<s:
#         s=user
#     i=i+1
# print("largest number is",l)
# print("smallest number is",s)


n=int(input("enter the number"))
i=1
while i<=n:
    user=int(input("enter the number"))
    lar=0
    small=1000
    if user>lar:
        lar=user
    if  user<small:
        small=user
    i=i+1
print("lar",lar)
print("small",small)