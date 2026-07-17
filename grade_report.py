# List containing 5 student dictionaries
students = [
    {"name": "Leo", "math_mark": 79, "english_mark": 78, "science_mark": 73},
    {"name": "Mia", "math_mark": 85, "english_mark": 92, "science_mark": 88},
    {"name": "Noah", "math_mark": 60, "english_mark": 65, "science_mark": 70},
    {"name": "Olivia", "math_mark": 95, "english_mark": 89, "science_mark": 94},
    {"name": "Ethan", "math_mark": 72, "english_mark": 74, "science_mark": 68}
]

# list containing only the marks for each student
all_marks = []

for student in students:
    marks = {
        "math_mark": student["math_mark"],
        "english_mark": student["english_mark"],
        "science_mark": student["science_mark"]
    }
    all_marks.append(marks)

student_