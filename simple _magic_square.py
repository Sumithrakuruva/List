l=[[4,3,4],[6,3,4],[8,1,3]]
i=0
while i<len(l):
    j=0
    dia=0
    while j<len(l[i]):
        dia=dia+l[j][i]
        j=j+1
        
    i=i+1
    print(dia)