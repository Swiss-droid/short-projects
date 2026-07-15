student_name = input("Enter the student's name: ")

mark_1 = float(input("Enter the first mark: "))
mark_2 = float(input("Enter the second mark: "))
mark_3 = float(input("Enter the third mark: "))

average = (mark_1 + mark_2 + mark_3) / 3

if mark_1 >= 80:
    print("A")
elif 70 <= mark_1 <= 79:
    print("B")
elif 60 <= mark_1 <= 69:
    print("C")
if 50 <= mark_1 <= 59:
    print("D")
else: # Below 50
    print("F")


if mark_1 < 40:
    print("Needs intervention")


if mark_2 >= 80:
    print("A")
elif 70 <= mark_2 <= 79:
    print("B")
elif 60 <= mark_2 <= 69:
    print("C")
if 50 <= mark_2 <= 59:
    print("D")
else: # Below 50
    print("F")


if mark_1 < 40:
    print("Needs intervention")


if mark_3 >= 80:
    print("A")
elif 70 <= mark_3 <= 79:
    print("B")
elif 60 <= mark_3 <= 69:
    print("C")
if 50 <= mark_3 <= 59:
    print("D")
else: # Below 50
    print("F")


if mark_1 < 40:
    print("Needs intervention")



if average >= 50:
    print("Pass")
else:
    print("Fail")