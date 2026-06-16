# type conversion

# implicit type conversion
age="21"
print(type(age))
print(age +" age")  # this will give error because age is string and 10 is integer
age=int(age)
print(age+10)
print(type(age))    

marks=90
print(type(marks))
string=str(marks)
print(type(string))
print(string+" marks")

float_num=3.14
int_num=int(float_num)
print(int_num)
print(type(int_num))

marks=str(90)

print(marks+ " marks")
print(type(marks))