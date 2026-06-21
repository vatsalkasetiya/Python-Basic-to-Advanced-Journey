# student={
#     "name":"vatsal",
#     "age":21,
#     "city":"rajkot"
# }
# print(student["city"])

# student={
#     "name":"vatsal",
#     "age":21
# }
# student["age"]=25
# print(student)

# student={
#     "name":"vatsal",
#     "age":21
# }
# student["city"]="rajkot"
# print(student)

# student={
#     "name":"vatsal",
#     "age":21,
#     "city":"rajkot"
# }
# student["city"]="ahmedabad"
# print(student["city"])

# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }
# for i in student:
#     print(i)

# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }
# for i in student:
#     print(student[i])

# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }

# for i in student:
#     print(i,":",student[i])

# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }
# count=0
# for i in student:
#     count+=1
# print("keys :",count)

# freq_count={}
# word="vatsal"

# for i in word:
#     if i in freq_count:
#         freq_count[i]+=1
#     else:
#         freq_count[i]=1
# print(freq_count)


# word="vatsal"
# new_string=""
# for ch in word:
#     if(ch in new_string):
#         continue
#     else:
#         new_string+=ch
# print(new_string)


# nums=[10,20,10,30,20,10]
# freq={}

# for i in nums:
#     if(i in freq):
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# word="banana"
# done=""
# for i in word:
#     if(i in done):
#         continue
#     else:
#         print(i,word.count(i))
#         done+=i
# print(done)

# word="banana"
# freq={}

# for i in word:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)



# word="kaara"
# freq={}
# for i in word:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# nums=[10,20,10,30,20,40]
# freq={}
# for i in nums:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# for i in nums:
#     if(freq[i]>1):
#         print(i)


# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }

# if "age" in student:
#     print("found")
# else:
#     print("not found")

# student={
# "name":"vatsal",
# "age":21,
# "city":"rajkot"
# }

# if "rajkot" in student.values():
#     print("found")
# else:
#     print("not found")

# student={
# "name":"vatsal",
# "age":21
# }

# print(student.keys())
# print(student.values())
# student={
# "name":"vatsal",
# "age":21
# }

# print(student.items())
# print(student.get("name"))

    
# student={
#     "name":"vatsal",
#     "age":23,
#     "address":"indravihar"
# }
# print(student)

# student.update({
#     "city":"rajkot",
#     "address":"amreli"
# })

# print(student)


# nums=[10,20]
# nums.append(30)
# nums.remove(30)
# print(nums)

# nums={10,20,30}
# print(nums)
# print(type(nums))
# nums.add(40)
# print(nums)

# nums={10,20,30}
# nums.add(20)
# print(nums)

# nums={10,20,30,40}
# nums.remove(20)
# print(nums)

# nums={10,0,0,40,50}
# if 20 in nums:
#     print("found")
# else:
#     print("not found")
    

# nums={10,20,30,40,50,60}
# count=0
# for i in nums:
#     count+=1
# print(count)
        

# nums={10,21,30,45,60,71}
# for i in nums:
#     if(i%2==0):
#         print(i)

# nums=[10,20,10,30,20,40]

# unique=set(nums)

# print(unique)
    

# list1=[10,20,30,40,40]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         continue
# print(list2)

nums={10,20,30,40,50}
count=0
for i in nums:
    if(i%2==0):
        count+=1
print(count)
        