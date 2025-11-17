print("My name is Vaishnavi")
print(10,20,30)
print("100","200","300")
print("17","11","2025",sep="-") # seperator used to seperate every value
print(17,11,2025,sep="/")
print(17,11,2025,sep=":",end="*\n")
print("Hi Everyone") # next line by default present in print function
print("Good Morning")

# if i want "HI Everyone Good Morning in single line"
print("Hi Everyone",end=" ")
print("Good Morning")

# if i want next line in single line
# Use \n for next line
print("I am Vaishnavi \n I am Python Developer\n I am Fresher")

# \t used for tab some space create between two words
print("I am \t Vaishnavi. \n I am Java Developer\n I am Fresher")


''' Variable is like a container which is used to store data on computer memory 
variable is a named memory location
eg : name= "Vaishnavi"  
At runtime python will decide what will be the datatype
Datatypes in python
1. int --- <class 'int'> # data type of int 
2. float
3.String
4.boolean
5.None 
6. Dictionary
7.Tuple
8.List
9.Complex 
10 Set '''




# way to print statement/Function
name="Vaishnavi"
age=23
address="Pune"
height=5.5
# 1St Way to print 
print(name,age,address,height)

# 2nd way to print using concatination
print("Name    :",name)
print("Age     :",age)
print("Address :",address)
print("Height  :",height)

# 3rd way to print using  F-string (F-formated)
print(f"My name is {name} \n My age is {age} \n My address is {address} \n My height is {height}")

# TYpe is a predefines function which is used to check the type of data type of variable
isMarried=True
b=None
print(type(name))      #<class 'str'>
print(type(age))       #<class 'int'>
print(type(address))   #<class 'str'>
print(type(height))    #<class 'float'>
print(type(isMarried)) #<class 'bool'>
print(type(None))      # <class 'NoneType'>

