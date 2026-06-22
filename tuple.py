# a=(1,2,3)
# print(a,type(a))

# nums=(10,20,30,40)
# print(nums[2])

# nums=(10,20,30,40)
# for i in nums:
#     print(i)

# nums=(10,20,10,30,10)
# # count=0
# # for i in nums:
# #     if(i==10):
# #         count+=1
# # print(count)
# print(nums.count(10))

# nums=(10,20,30,40,30)
# print(nums.index(30))
# for i in range(len(nums)):
#     if(nums[i]==30):
#         print(nums[i],"at postion",i)

nums=(10,40,50)
found=False
if(30 in nums):
        found=True
if found==True:
    print("found")
else:
    print("not found")
