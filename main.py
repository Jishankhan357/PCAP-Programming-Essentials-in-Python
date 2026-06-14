import pickle
import time
import os

def set_data():
    """Takes input from the user and returns a dictionary of student details."""
    print("\n--- ENTER STUDENT'S DETAILS ---")
    rollno = int(input('Enter roll number: '))
    name = input('Enter name: ')
    english = int(input('Enter Marks in English: '))
    maths = int(input('Enter Marks in Maths: '))
    physics = int(input('Enter Marks in Physics: '))
    chemistry = int(input('Enter Marks in Chemistry: '))
    cs = int(input('Enter Marks in CS: '))
    print()
    
    # Packing data into a dictionary for easy serialization
    student = {
        'rollno': rollno,
        'name': name,
        'english': english,
        'maths': maths,
        'physics': physics,
        'chemistry': chemistry,
        'cs': cs
    }
    return student

def display_data(student):
    """Displays a single student's record in a readable format."""
    print('\nSTUDENT DETAILS..')
    print('Roll Number:', student['rollno'])
    print('Name:', student['name'])
    print('English:', student['english'])
    print('Maths:', student['maths'])
    print('Physics:', student['physics'])
    print('Chemistry:', student['chemistry'])
    print('CS:', student['cs'])
    print('-' * 20)

def display_data_tabular(student):
    """Formats and prints student data in a single row for the table view."""
    print('{0:<8}{1:<20}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}'.format(
        student['rollno'], student['name'], student['english'], 
        student['maths'], student['physics'], student['chemistry'], student['cs']
    ))

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
    
    # Keep reading until EOFError is thrown by pickle
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
        # Get data and serialize it directly into the file
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
                break  # We found the unique student, no need to read further
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
            # If it's the target record, show it but DO NOT write it to temp file
            if student['rollno'] == rollno:
                display_data(student)
                found = True
                # Notice: Removed the 'break' here so the rest of the file still gets copied
            else:
                pickle.dump(student, outfile)
        except EOFError:
            break

    infile.close()
    outfile.close()
    
    # Replace the old file with the updated temp file
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
                
                # Dump the updated student record
                pickle.dump(student, outfile)
                found = True
                print('\nRecord updated successfully!')
                display_data(student)
                # Notice: Removed the 'break' to ensure remaining records are copied over
            else:
                # Dump unchanged student records
                pickle.dump(student, outfile)
                
        except EOFError:
            break
            
    infile.close()
    outfile.close()
    
    os.remove("student.dat")
    os.rename("temp.dat", "student.dat")
    
    if not found:
        print('Record not Found')

def intro():
    """Displays the welcome screen."""
    print("="*80)
    print("{: ^80s}".format("NIIT Foundation"))
    print("{: ^80s}".format("STUDENT REPORT CARD"))
    print("{: ^80s}".format("PROJECT"))
    print("="*80)
    print()

def main_menu():
    time.sleep(0.5)
    print("\n--- MAIN MENU ---")
    print("1. REPORT MENU")
    print("2. ADMIN MENU")
    print("3. EXIT")

def report_menu():
    time.sleep(0.5)
    print("\n--- REPORT MENU ---")
    print("1. CLASS RESULT")
    print("2. SEARCH STUDENT REPORT CARD")
    print("3. BACK TO MAIN MENU")
    
def admin_menu():
    time.sleep(0.5)
    print("\n--- ADMIN MENU ---")
    print("1. CREATE STUDENT RECORD")
    print("2. DISPLAY ALL STUDENTS RECORDS")
    print("3. SEARCH STUDENT RECORD ")
    print("4. MODIFY STUDENT RECORD ")
    print("5. DELETE STUDENT RECORD ")
    print("6. BACK TO MAIN MENU")
    
def main():
    """Main program loop handling user navigation."""
    intro()
    while True:
        main_menu()
        choice = input('Enter choice (1-3): ')
        
        if choice == '1':
            while True:
                report_menu()
                rchoice = input('Enter choice (1-3): ')
                if rchoice == '1':
                    class_result()
                elif rchoice == '2':
                    search_record()
                elif rchoice == '3':
                    break
                else:
                    print('Invalid input !!!')
        
        elif choice == '2':
            while True:
                admin_menu()
                echoice = input('Enter choice (1-6): ')
                if echoice == '1':
                    write_record()
                elif echoice == '2':
                    read_records()
                elif echoice == '3':
                    search_record()
                elif echoice == '4':
                    modify_record()
                elif echoice == '5':
                    delete_record()
                elif echoice == '6':
                    break
                else:
                    print('Invalid input !!!')
            
        elif choice == '3':
            print('\nThanks for using NIIT Foundation Student Management System. Goodbye!')
            break
        else:
            print('Invalid input!!! Please select from 1 to 3.')

# Program execution starts here
if __name__ == "__main__":
    main()