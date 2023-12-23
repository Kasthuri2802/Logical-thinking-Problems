# Problem #3
# Use switch stmt (no if stmts) to calculate the grade of the student based on marks
# Grade A = mark >90
# Grade B  between 80 and 90
# Grade C between 60 and 80
# Fail , below 60

# Make sure to include code for all possible input values.

mark = int(input("Enter your mark: "))
match mark:
    case mark if 90 <= mark <= 100 :
        print("Grade A")
    case mark if 80 <= mark < 90:
        print("Grade B")
    case mark if 60<= mark < 80:
        print("Grade C")
    case mark if mark < 60:
        print("Fail")

