#code the sttudents and ranks accordings to score give grades
maths=int(input("enter the maths marks of the student:"))
quadratic_physics=int(input("enter the phy marks of the student:"))
chemistry=int(input("enter the che marks of the student:"))
english=int(input("enter the eng marks of the student:"))
phyton=int(input("enter the phyton marks of the student:"))

total_marks=maths+quadratic_physics+chemistry+english+phyton
percentage=total_marks/5

if (percentage >= 90):
    print("O grade")
elif (percentage >= 80 and percentage < 90):
    print(" A grade")
elif (percentage >= 70 and percentage < 80):
    print("B grade")
elif (percentage < 70):
    print("fail")


