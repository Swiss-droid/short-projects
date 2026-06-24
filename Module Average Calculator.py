student1 = int(input("Enter the average: "))
student2 = int(input("Enter the average: "))
student3 = int(input("Enter the average: "))
student4 = int(input("Enter the average: "))
student5 = int(input("Enter the average: "))
student6 = int(input("Enter the average: "))
student7 = int(input("Enter the average: "))
student8 = int(input("Enter the average: "))
student9 = int(input("Enter the average: "))
student10 = int(input("Enter the average: "))

student_average = (student1 + student2 + student3 + student4 + student5 + student6 + student7 + student8 + student9 + student10)

module_average = student_average / 10
print(module_average)



first_threshold = 75
second_threshold = 50

if student_average < 0:
    print("Error. Close the program.")

if module_average >= 75:
    print("Excellent results students.")
elif 50 <= module_average <= 74:
    print("Well done students.")
else:
    print("The class failed.")



if student1 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student1 == 75:
    print("Well done.")
elif student1 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student2 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student2 == 75:
    print("Well done.")
elif student2 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student3 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student3 == 75:
    print("Well done.")
elif student3 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student4 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student4 == 75:
    print("Well done.")
elif student4 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student5 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student5 == 75:
    print("Well done.")
elif student5 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student6 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student6 == 75:
    print("Well done.")
elif student6 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student7 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student7 == 75:
    print("Well done.")
elif student7 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student8 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student8 == 75:
    print("Well done.")
elif student8 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student9 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student9 == 75:
    print("Well done.")
elif student9 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

if student10 > 75:
    print("Distinction. Well Done Student!!!", first_threshold)
elif student10 == 75:
    print("Well done.")
elif student10 < 60:
    print("You passed", second_threshold) 
else:
    print("You failed")

