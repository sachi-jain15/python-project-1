'''EXAM STATISTICS'''

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] #List of grades

# Function to print grades is described below:
def print_grades(grades):
    for grade in grades:
        print grade

# Function to return sum of all the grades is described below:
def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

# Function to return average of all the grades scored is described below:
def grades_average(grades):
    sum_of_grades = grades_sum(grades) # grades_sum function call made here
    average = sum_of_grades / float(len(grades)) #len(grades) is to calcute the number of elements in the list and float() is to convert it into float value for calculation
    return average

# Function to return variance of grade scored is described below:
def grade_variance(scores):
    average = grades_average(scores)# grades_average function call made here
    variance = 0
    for score in scores:
        variance = variance + ((average - score) ** 2) # Formula of variance
    result = variance / len(scores) # Formula of variance
    return result

# Function to return return standard deviation of grades is described below:
def grade_std_deviation(variance):
    return variance ** 0.5 # Formula of standard deviation

variance = grade_variance(grades) # Variance variable to pass value in the grade_std_deviation function

print "\nGrades are  : \n", print_grades(grades)
print "Sum of grades : ", grades_sum(grades)
print "Average grade : ", grades_average(grades)
print "Variance : ", grade_variance(grades)
print "Standard deviation : ", grade_std_deviation(variance)
