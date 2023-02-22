a=['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
i=0
b=[]
while i<len(a):
    j=0
    c=a[i]
    while j<len(c):
        d=c[::-1]
        # print(d)
        j=j+1
    b.append(d)
    i=i+1
print(b)
        
    
    
    




        