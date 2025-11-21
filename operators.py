#Operator is a special symbol which is use  to perform some operations on operand
# 10 & 20 are the operand
'''Types of Operator
1.Arithmetic Operator(+,-,*,**(Exponent Operator),/,//(Floor division),%,)
2.Relational Operators/ Comparison Operator (<,>,<=,>=,==,!=)
3.Logical Operator (and ,or,not) 
4.Assignment Operator (+=,-=,*=,/=,//=,**=,%=)



''' 
a=10
b=3
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)             # Decimal Point
print("Modulus",a%b)              # Remainder
print("Exponent Operator",a**b)   # a to the power b 10*10*10
print("Floor Division",a//b)      #a/b Integer not in decimal

print("==================================================================")



price=3000 # product Price
#discount apply 20% then give the final price to customer
discount=price*0.20
finalprice = price-discount
print("Final Price",finalprice)
print("Discount You Got",discount,"Final Price",finalprice)
print("==============================================================")

# Relational Operators : relational operators used to check the relationship between 2 operands
c=20
d=100
print("c is less than d :",c<d)             # True
print("C is greater thad d :",c>d)          #False
print("C is less than equal to d",c<=d)     #True
print("C is greater than equal to d",c>=d)  #False
print("C is equal equal to d:",c==d)        #False
print("C is not equal to d:",c!=d)          # True

print("==============================================================")

# Logical Operator: used for decision making 
# to check multiple conditions more than one use logical operator
x=10
y=20
print(x==y and x<y)  # False
print(x<y and x==y)  # False
print(x<y or x==y)   # True
print(x>y and x==y)  # False
print(x!=y and x<y)  # True
x=True
y = False
print(x) # True
print(not x) #False
print(y) # False
print(not y) # True
print(not x<10) # False
print(not y>10) # True
print(x>10) #False
print("========================================================")

# Assignment Operators
a=50
#a=a+10
a+=10
print(a) 

a-=10
#a=a-10
print(a)

a*=10
a=a-10
print(a)

a/=10
# a=a/10
print(a)

a//=10
#a=a//10
print(a)

a**=10
print(a)

a%=10
print(a)

print("======================================================")

balance=1000
deposite=500
balance+=deposite
withdraw=200
balance -=withdraw
print(balance)