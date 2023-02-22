# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
a=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
i=0
b=[]
while i<len(a):
    j=0
    c=a[i]
    while j<len(c) :
        if type(c)==list:
            b.append(a[i])
        else:
            b.append(a[i])
        j=j+1
    i=i+1
print(b)

# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==list:
#         a.extend(b)
#     else:
#         a.extend(a[i])
#     i=i+1
# print(b)


