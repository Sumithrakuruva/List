# # Original list:
# from sys import argv


a=[1, 1, 3, 4, 4, 5, 6, 7,0]
b=[0, 1, 2, 3, 4, 4, 5, 7, 8]

# Average of two lists:
# 3.823529411764706

i=0
suma=0
sumb=0
n=[]
while i<len(a):
    suma+=a[i]
    sumb+=b[i]
    i=i+1
avg1=suma/(len(a)-1)
avg2=sumb/len(b)
avg=avg1+avg2
print(avg/2)
# avg1=sum(a)/len(a)
# avg2=sum(b)/len(b)
# avg=avg1+avg2
# print(avg/2)
 
 
    





    
 


       