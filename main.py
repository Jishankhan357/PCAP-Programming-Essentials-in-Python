import ui_reports
import database_ops

def main():
    """Main program loop handling user navigation."""
    ui_reports.intro()
    while True:
        ui_reports.main_menu()
        choice = input('Enter choice (1-3): ')
        
        if choice == '1':
            while True:
                ui_reports.report_menu()
                rchoice = input('Enter choice (1-3): ')
                if rchoice == '1':
                    database_ops.class_result()
                elif rchoice == '2':
                    database_ops.search_record()
                elif rchoice == '3':
                    break
                else:
                    print('Invalid input !!!')
        
        elif choice == '2':
            while True:
                ui_reports.admin_menu()
                echoice = input('Enter choice (1-6): ')
                if echoice == '1':
                    database_ops.write_record()
                elif echoice == '2':
                    database_ops.read_records()
                elif echoice == '3':
                    database_ops.search_record()
                elif echoice == '4':
                    database_ops.modify_record()
                elif echoice == '5':
                    database_ops.delete_record()
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