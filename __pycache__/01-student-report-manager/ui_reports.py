import time

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
    
    student = {
        'rollno': rollno, 'name': name, 'english': english,
        'maths': maths, 'physics': physics, 'chemistry': chemistry, 'cs': cs
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