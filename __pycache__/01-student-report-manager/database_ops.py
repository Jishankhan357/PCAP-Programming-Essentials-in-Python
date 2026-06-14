import pickle
import os
from ui_reports import set_data, display_data, display_data_tabular

def class_result():
    """Reads all records and prints them in a tabular format."""
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found..')
        print('Go to admin menu to create a record first.')
        return

    print('\n' + '='*78)
    print('{0:<8}{1:<20}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}'.format(
        'Rollno', 'Name', 'English', 'Maths', 'Physics', 'Chemistry', 'CS'
    ))
    print('='*78)
    
    while True:
        try:
            student = pickle.load(infile)
            display_data_tabular(student)
        except EOFError:
            break
    infile.close()

def write_record():
    """Appends new student records to the binary file."""
    outfile = open('student.dat', 'ab')
    while True:
        pickle.dump(set_data(), outfile)
        ans = input('Want to enter another record (y/n)?: ')
        if ans.lower() == 'n':
            break
    outfile.close()
    print("Records saved successfully!")

def read_records():
    """Reads and displays all records one by one."""
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No records found..')
        return

    while True:
        try:
            student = pickle.load(infile)
            display_data(student)
        except EOFError:
            break
    infile.close()

def search_record():
    """Searches for a specific student using their roll number."""
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No records exist yet.')
        return

    print('\n--- SEARCH RECORD ---')
    rollno = int(input('Enter the rollno you want to search: '))
    found = False
    
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                display_data(student)
                found = True
                break
        except EOFError:
            break
            
    if not found:
        print('Record not found!!')
    infile.close()

def delete_record():
    """Deletes a student record by copying all OTHER records to a temp file, then renaming it."""
    print('\n--- DELETE RECORD ---')
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to delete..')
        return

    outfile = open("temp.dat", "wb")
    found = False
    rollno = int(input('Enter roll number to delete: '))
    
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                display_data(student)
                found = True
            else:
                pickle.dump(student, outfile)
        except EOFError:
            break

    infile.close()
    outfile.close()
    os.remove("student.dat")
    os.rename("temp.dat", "student.dat")
    
    if not found:
        print('Record not Found\n')
    else:
        print("Record successfully deleted.\n")

def modify_record():
    """Modifies an existing student's data."""
    print('\n--- MODIFY RECORD ---')    
    try:
        infile = open('student.dat', 'rb')
    except FileNotFoundError:
        print('No record found to modify..')
        return

    outfile = open("temp.dat", "wb")
    found = False
    rollno = int(input('Enter roll number to modify: '))
    
    while True:
        try:
            student = pickle.load(infile)
            if student['rollno'] == rollno:
                print(f"Current Name: {student['name']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['name'] = input("Enter new name: ")

                print(f"Current English marks: {student['english']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['english'] = int(input("Enter new marks: "))

                print(f"Current Maths marks: {student['maths']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['maths'] = int(input("Enter new marks: "))

                print(f"Current Physics marks: {student['physics']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['physics'] = int(input("Enter new marks: "))

                print(f"Current Chemistry marks: {student['chemistry']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['chemistry'] = int(input("Enter new marks: "))

                print(f"Current CS marks: {student['cs']}")
                if input('Want to edit (y/n)? ').lower() == 'y':
                    student['cs'] = int(input("Enter new marks: "))
                
                pickle.dump(student, outfile)
                found = True
                print('\nRecord updated successfully!')
                display_data(student)
            else:
                pickle.dump(student, outfile)
                
        except EOFError:
            break
            
    infile.close()
    outfile.close()
    os.remove("student.dat")
    os.rename("temp.dat", "student.dat")
    
    if not found:
        print('Record not Found')