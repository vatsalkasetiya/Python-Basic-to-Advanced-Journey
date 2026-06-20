# num=[10,20,30]
# for i in range(len(num)):
#     print(num[i])

# nums=[10,20,30]
# for i in range(len(nums)):
#     nums[i]/=2
# print(nums)

# nums=[10,20,30,40,50]
# for i in range(len(nums)):
#     nums[i]=nums[i]*2
# print(nums)

# nums=[10,21,12,34,43,43534,534]
# count=0
# for i in range(len(nums)):
#     if(nums[i]>=25):
#         count+=1
# print(count)

# nums=[10,20,30,15]

# for i in nums:

#     nums=i*2

# print(nums)

# nums=[10,20,30]
# for i in range(len(nums)):
#     nums[i]=nums[i]*2
# print(nums)

# nums=[5,10,15]

# for i in nums:
#     print(i)

# nums=[5,10,15]

# for i in range(len(nums)):
#     print(nums[i])

# nums=[11,20,31,40,55,60,22]
# for i in nums:
#     if(i%2==0):
#         print(i)

# nums=[10,21,31,40,55,60]
# count=0
# for i in nums:
#     if(i%2==1):
#         count+=1
# print(count)

# nums=[10,20,30,40]
# for i in range(len(nums)):
#     print(i,nums[i])

# nums=[100,200,300,400,500]

# for i in range(len(nums)):
#     if(i%2==0):
#         print(i,nums[i])

# nums=[10,20,30,40]
# for i in range(len(nums)):
#     nums[i]+=5
# print(nums)

# nums=[10,-5,20,-8,30]
# for i in range(len(nums)):
#     if nums[i]<0:
#         nums[i]=0
# print(nums)

# nums=[10,40,25,60,5,30]
# count=0
# for i in nums:
#     if(i>25):
#         count+=1
# print(count)

# nums=[20000,80,900,10,4543,100,50,400]
# max=nums[0]
# for i in range(len(nums)):
#     if(nums[i]>max):
#         max=nums[i]
# print(max)

# nums=[10199,104,43,232,2394,424]
# max=nums[0]
# for i in range(len(nums)):
#     if(nums[i]>max):
#         max=nums[i]
# print(max)

# nums=[10,20,50,40,90,50]
# for i in range(len(nums)):
#     if(nums[i]==50):
#         print("exist at",i)

# nums=[10,50,20,50,90,50]
# count=0
# for i in range(len(nums)):
#     if(nums[i]==50):
#         count+=1
# print(count)

# nums=[10,20,30,-5,40,-3]
# negative=False
# for i in range(len(nums)):
#     if(nums[i]<0):
#         negative=True
# print(negative)

# nums=[10,50,20,50,90,50]
# for i in range(len(nums)):
#     if(nums[i]==50):
#         print("first 50 at",i)
#         break
   
# nums=[10,20,30,4,50,40,33]
# odd=False
# for i in range(len(nums)):
#     if(nums[i]%2==1):
#         odd=True
# if(odd==True):
#     print("not all are even")
# else:
#     print("all are even")

# nums=[10,20,30,50,333,3]
# increse=True
# for i in range(len(nums)-1):
#     if(nums[i]>=nums[i+1]):
#         increse=False
# if increse==True:
#     print("increse")
# else:
#     print("not incerese")

# nums=[10,20,30,40,104,203]
# new_list=[]
# duplicate=False

# for i in range(len(nums)):
#     if(nums[i] not in new_list):
#         duplicate=False
#         new_list.append(nums[i])
#     else:
#         duplicate=True
# if(duplicate==True):
#     print("duplicate found")
# else:
#     print("duplicate not found")
# word = "banana"
# done = ""

# for ch in word:
#     if ch not in done:
#         print(ch,word.count(ch))
#         done+=ch
# print(done)

# nums=[10,20,10,30,20,10,10]
# new_list=[]
# for i in range(len(nums)):
#     if(nums[i] not in new_list):
#         print(nums[i],nums.count(nums[i]))
#         new_list.append(nums[i])
# print(new_list)

# word="banana"
# done=""
# count=0

# for ch in word:
#     if ch not in done:
#         done=done+ch
#         print(ch,word.count(ch))
#         count+=1


# nums = [10,20,30,20,40]
# for i in range(len(nums)):
#     if(nums[i]==20):
#         nums[i]=99
# print(nums)

# nums = [11, 20, 33, 40, 55]
# for i in range(len(nums)):
#     if(nums[i]%2==1):
#         nums[i]=0
# print(nums)

# nums = [100, 50, 20, 80, 90, 300]
# max=nums[0]
# for i in range(len(nums)):
#     if(nums[i]>max):
#         max=nums[i]
# print(max)

# nums = [10, 20, 30, 40]
# sum=0
# for i in range(len(nums)):
#     sum=nums[i]+sum
# print(sum)

# word="vatsal"
# reverse=""
# for ch in word:
#     reverse=ch+reverse
# print(reverse)

# nums = [10, 20, 30, 40,24]
# rev=[]
# for i in range(len(nums)-1,-1,-1):
#     rev.append(nums[i])
# print(rev)

# nums = [50, 20, 10, 5,80, 30]
# small=nums[0]
# for i in range(len(nums)):
#     if(small>nums[i]):
#         small=nums[i]
# print(small)

word="banana"
done=""

for ch in word:
    if ch not in done:
        print(ch,word.count(ch))
        done+=ch
        
print(done)
