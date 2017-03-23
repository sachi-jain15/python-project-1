'''STUDENT BECOMES THE TEACHER'''
# First student's dictionary
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
# Second student's dictionary
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
# Third student's dictionary
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
#List Students have the above three dictionaries as elements
students=[{"name": "Lloyd","homework": [90.0, 97.0, 75.0, 92.0],"quizzes": [88.0, 40.0, 94.0],"tests": [75.0, 90.0]}, {"name": "Alice","homework": [100.0, 92.0, 98.0, 100.0],"quizzes": [82.0, 83.0, 91.0],"tests": [89.0, 97.0]}, {"name": "Tyler","homework": [0.0, 87.0, 75.0, 22.0],"quizzes": [0.0, 75.0, 78.0],"tests": [100.0, 100.0]}]

# Function to calculate average of the element is described below:
def average(numbers):
    total = sum(numbers)
    total = float(total) # To convert integer type of the variable total to float type
    average_result = total / (len(numbers))
    return average_result

# Function to calculate overall average of a student is described below:
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return ((homework * 0.1) + (quizzes * 0.3) + (tests * 0.6)) #sum of weighted averages of the homework, quizzes and tests key


# Function to return the grade acheived by the students according to their score is given below:
def get_letter_grade(score):
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 60):
        return "D"
    else:
        return "F"

# Function to calculate average of all scores for all students in the array is given below:
def class_average(students):
    results = [] #Empty list
    for each_student in students:
        element_of_results = get_average(each_student)#calculate overall average of each student by making function call
        results.append(element_of_results)#insertion of calculated overall average of each student as an element in results
    return average(results)# returns average by making function call

print"Class average score is: ", class_average(students)
print "Class Grade: ", get_letter_grade(class_average)
