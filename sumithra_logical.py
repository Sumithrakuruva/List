# lst = [1,2,3,4]
# n = len(lst)

# for i in range(n):
#     for j in range(i+1, n+1):
#          print(lst[i:j])


nums = []
for i in range(3):
    nums.append([])
    for j in range(3, 6):
        nums[i].append(j)

print(nums)