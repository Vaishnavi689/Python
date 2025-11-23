# multiplication table of any number which is given by user

num=int(input("Enter a number"))
if num<0:
    print("Enter positive numbers only")
else:
    for i in range(1,11):
      print(f"{num}*{i}={num*i}")