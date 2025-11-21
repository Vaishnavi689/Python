#age=80
age=int(input("Enter your age: "))

if age<=0:
    print("age should be grater than 0")
    print("Invalid age")

if age<18 and age>0:
    print("You are Child")

if age>=18 and age<=60:
    print("You are Adult")

if age>60:
    print("You are senoir citizen")
