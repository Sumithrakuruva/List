a=[1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
i=0
b=[]
d=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        j=0
        c=[]
    while j<1:
        x=a.count(a[i])
        if x>=2:
            c.append(x)
            c.append(a[i])
        else:
            d.append(c)
        j=j+1
    d.append(c)
    i=i+1
print(d)