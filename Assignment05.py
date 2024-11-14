# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   James Copsey,11/13/2024,Built upon existing script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, 'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print(f"{FILE_NAME} was not found. Creating {FILE_NAME}")
    file = open(FILE_NAME, 'w') # If the file doesn't exist, create it
except Exception as e:
    print("There was an error opening the file.")
    print(e, e.__doc__)
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalnum():
                raise ValueError("Student First Name must be alphanumeric")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalnum():
                raise ValueError("Student Last Name must be alphanumeric")
            course_name = input("Please enter the name of the course: ")
            if not course_name.isalnum():
                raise ValueError("Course Name must be alphanumeric")
            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name
            }
            students.append(student_data)
            print((
                f"You have registered {student_data['FirstName']} "
                f"{student_data['LastName']} for "
                f"{student_data['CourseName']}."
            ))
            continue
        except ValueError as e:
            print("Invalid information. Please try again.")
            continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print((
                f"{student['FirstName']} "
                f"{student['LastName']} is registered for "
                f"{student['CourseName']}."
            ))
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print((
                    f"Student {student['FirstName']} "
                    f"{student['LastName']} "
                    f"is enrolled in {student['CourseName']}."
                ))
        except Exception as e:
            print(f"There was an error writing to {FILE_NAME}.")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
