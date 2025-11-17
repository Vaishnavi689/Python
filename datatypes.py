a=10
b=20
sum=a+b  # addition
print("Sum of two number :",sum)
print("========================================================")

# How to take input from user/console
''' Python give a function called input() Function
''' 

a=input("Enter the 1st number : ")
b=input("Enter the 2nd number :")
print("Entered number :",a)
print("Enterd number  :",b)
print("Addition of a and b :",a+b) 
# Input function by default read the string value only that means 100 and 200 as a string read by input function
# we need to type casting for addition
print("=====================================================")

a= int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number :"))
# Two ways for addition 
print("Addition of a and b :",a+b)
print("Addition of a and b :",int(a)+ int(b))
print("Addition of a and b :",int(a+b)) # Not working
print("=======================================================================")

name=input("Enter your name            :")
age=int(input("Enter your age          :"))
address=input("Enter your address      :")
height=float(input("Enteer your height :"))
ismarried=bool(input("Are you married  :"))
print("=====================================================")

print("Name :",name)
print("Age  :",age)
print("Address :",address)
print("Height  :",height)
print("IsMarried:",ismarried) # in python string if we write true or false we get True value in output because if we write any we always got true 
# But if we take empty string then we got False
print("===================================================")

# We can read two or more  numbers in python at a time using split(',') function
a,b=input("Enter two numbers :").split(',')
print(int(a)+int(b))

name,age,address=input("Enter your name,age,address :").split(',')
print("Name:",name)
print("Age :",age)
print("Address:",address)

print("===========================================================")
# Create a  program to take input from user
# username , password,Email,mobile number,Gender,
# Print using F-string
# print that details USING PRINT FUNCTION


Username=input("Enter your name:")
password=input("Enter your password:")
Email=input("ENter Your Email :")
Mobile=input("Enter your mobile number:")
Gender=input("Enter your Gender:")

print("Username is:" , Username)
print("Password is:",password)
print("Email is:",Email)
print("Mobile NUmber is:",Mobile)
print("Gender is:",Gender)
print("===================================================")
print(f"Username:",{Username},"Password :",{password},"Email :",{Email},"Mobile Number :",{Mobile},"Gender:",{Gender})
print(f"username is : {Username} \n password is : {password} \n Email is: {Email} \n Mobile Number is: {9769346202}\n Gender is: {Gender}")