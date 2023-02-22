
k=[[2,7,6],[9,5,1],[4,3,8]]
i=0
sum=0
# b=[]
while i<len(k):
    j=0
    while j<len(k[i]):
        if i==j:
            sum=sum+k[i][j]
        j=j+1
    i=i+1
print(sum)
        
    
    
    
    
    
    
    
    
    
 