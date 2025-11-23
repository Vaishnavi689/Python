# Calculate percentage & grade based on total marks

def get_marks():
    print("Enter marks of all subjects out of 100:")
    s1 = float(input("Enter marks of Java: "))
    s2 = float(input("Enter marks of Python: "))
    s3 = float(input("Enter marks of C++: "))
    s4 = float(input("Enter marks of DBMS: "))
    s5 = float(input("Enter marks of DSA: "))
    return s1, s2, s3, s4, s5


def calculate_total():
    s1, s2, s3, s4, s5 = get_marks()
    total = s1 + s2 + s3 + s4 + s5
    return total


def calculate_percentage():
    total = calculate_total()
    percentage = (total / 500) * 100
    return percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


# MAIN PROGRAM
percentage = calculate_percentage()
grade = calculate_grade(percentage)

print("Your Percentage is:", percentage)
print("Your Grade is:", grade)
