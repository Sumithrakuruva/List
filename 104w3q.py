a=[1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
[0, 2, 1, 0, 1, 1, 1]
# Original list:
# [4, 5, 8, 9, 6, 10]
# Difference between consecutive numbers of the said list:
# [1, 3, 1, -3, 4]

i=0
c=[]
while i<len(a)-1:
    b=a[i+1]-a[i]
    c.append(b)
    i=i+1
print(c)