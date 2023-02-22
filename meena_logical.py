a=["R",["A","N","I"]]
i=0
b=[]
while i<len(a):
    if type (a[i]) is list:
        j=0
        while j<len(a[i]):
            d=a[i][j]
            b.append(d.lower())
            j=j+1
    else:
        b.append(a[i])
    i=i+1
p="".join(b)
print(p)