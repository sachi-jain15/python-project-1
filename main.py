# MAIN FILE
def output(): #Function to take user's choice
    print "\nWhich script you want to run??\n Press 1 for students_to_teacher\n Press 2 for battleship\n Press 3 for exam_stats"
    choice=int(raw_input('Your choice: ')) # To take users input of their choice
    if (choice==1):
        print "\n      STUDENTS_TO_TEACHER\n"
        import students_to_teacher # It will import the code written in students_to_teacher.py
    elif (choice==2):
        print "\n     BATTLESHIP\n"
        import battleship # It will import the code written in battleship.py
    elif (choice==3):
        print "\n    EXAM STATISTICS\n"
        import exam_stats # It will import the code written in exam_stats.py
    else:
        print # To print blank line
        print "Invalid choice" # To inform user that he/she has entered a wrong number

output() #Function call to start the program
print "\n If you want to continue to run any script once again type yes" # To ask user one more time whether he want to run the code again or not
user_input=raw_input().lower() # This statement will take the input in lower case
if(user_input=='yes' or user_input=='y'):
    output() #Function Call
print "\n            END"
