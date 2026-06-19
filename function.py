# def say_hello():
#     print("hello vatsal")
# say_hello()
# say_hello()

# def table():
#     n=int(input("enter n:"))
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
# table()
# table()

# def greet(name):
#     print("hello",name)
# greet("vatsal")
# greet("jayesh")

# def sum(a,b):
#     print("sum of a & b is:",a+b)
# sum(10,10)
# sum(10,12)

# def details(name,age,roll):
#     print(name,age,roll)
# details("vatsal",34,1000)
# details("etr",34,54354)


# def details(name,age,college):
#     print(name,age,college)
# details(age="adani",name=24,college="rt4")

# def square(n):
#     print(n*n)
# square(2)

# def table(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
# table(5)

# def vowel(word):
#     count=0

#     for i in word:
#         if i in "aeiou":
#             count+=1
#     print(count)
# vowel("vatsali")

# def sum(a,b):
#     print(a+b)
# sum(10,10)

# count=0
# def vowel(word):
   
#     for ch in word:
#         if ch in "aeiou":
#             count+=1
#     return count
# ans=vowel("vatsal")
# print(ans)

# def large(a,b):
#     if(a>=b):
#         return a
#     else:
#         return b
# large=large(100,20)
# print(large)


# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# result=factorial(5)
# print(result)

# x=10
# def test():
#     x=10
#     return x
# ans=test()
# print(ans)
# print(x)

# n1=int(input("enter n1:"))
# n2=int(input("enter n2:"))
# n3=int(input("enter n3:"))

# def avg(n1,n2,n3):
#     return ((n1+n2+n3)/3)
# ans=avg(n1,n2,n3)
# print(ans)

# def sum(a=0,b=1):
#     return a+b
# ans=sum(10)
# print(ans)

# square=lambda x:x*x
# add=square(4)
# print(add)

# n=int(input("enter n:"))

# def fact(n):
#     factt=1
#     for i in range(1,n+1):
#         factt=factt*i
#     return factt
# ans=fact(n)
# print(ans)


# n=int(input("etner n:"))
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# ans=factorial(n)
# print(ans)

# salary=int(input("enter your salary:"))
# if(salary<30000):
#     tax=salary*0.05

# elif(salary>=30000 and salary<70000):
#     tax=salary*0.15

# else:
#     tax=salary*0.30
# salary=salary-tax
# print("tax",tax)
# print("salary",salary)


# def digit(n):
#     for i in range(n):
#         print(i)
# digit(456)


# def counter(number):
#     count=0
#     for i in number:
#         count+=1
#     return count
# ans=counter("123443")
# print(ans)

# n=int(input("enter n:"))
# def sum(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#     return total
# ans=sum(n)
# print(ans)


while True:
    n=input("enter n:")
    if(n=="quit"):
        break
    else:
        print(n)
