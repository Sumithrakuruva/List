# a=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i],a[i+1]
#     if a[i]==a[i+1]:
#         b.append(list(c))
#     else:
#         b.append([a[i]])
#     i=i+1
# print(b)
lst = [1,2,3,4]
n = len(lst)

for i in range(n):
    for j in range(i+1, n+1):
         print(lst[i:j])
        

    
        
    