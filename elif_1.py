age=int(input("Enter your age:"))
if age>18 and age<=25:
    print("You are eligible for admission")

marks = int(input("Enter your marks :"))
if marks>=90:
    print("Addmission Sucess")

elif marks <90 and marks >70:
    print("You need to pay 2 Lakh for admission")

elif marks <70 and marks>50:
    print("You need to pay 4 Lakh for admission")

elif marks <50 and marks > 35:
    print("You need to pay 10 Lakh for admission")

else:
    print("You are not eligible for admission due to age or marks")