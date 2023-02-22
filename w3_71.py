# a= [{},{},{}]
# Return value : True
b= [{1,2},{},{}]
# Return value : False

i=0
c=[]
while i<len(b):
    if b[i] in []:
        c.append(b[i])
        
    i=i+1
print(c)
print("ture")

