import sqlite3
import time

conn = sqlite3.connect('test_database.db')
c = conn.cursor()

def start_menu():
    print ('\n------------------------')
    print ('    RUNNING DATABASE')
    print ('------------------------\n')
    print ('1) Enter Data')
    print ('2) Show all data within Database')
    print ('3) Update a certain row')
    print ('4) Delete a certain row')
    print ('0) EXIT')

def update_menu():
    print ('\n1) If you want to insert into the DATE column')
    print ('2) For all other columns')

def read_from_db():
    c.execute('SELECT * FROM database_test')
    print ('\n        <CURRENT DATABASE DATA>\n')
    for row in c.fetchall():
        print (row,'\n')
    return read_from_db

if __name__ == "__main__":

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS database_test(id INTEGER NOT NULL PRIMARY KEY, date TEXT, distance REAL, duration REAL, avg_pace REAL)')
    create_table()
    
    choice = ""
    while (choice != '0'):
        start_menu()
        choice = input('\nEnter number from menu above to continue: ')
        print ('-------------------------------------------')
        
        # INSERTING into Database
        if choice == '1':
            try:
                id = int(input('\n\n\nA) Enter ID #: '))
                print ('\n      ++ ID Entered into Database ++')
                date = input('\nB) Enter the DATE for the run completed (i.e. 2016-01-10): ')
                print ('\n      ++ Date Entered into Database ++')
                distance = float(input('\nC) Enter TOTAL DISTANCE RAN (i.e 2.11): '))
                print ('\n      ++ Distance Entered into Database ++')
                duration = float(input('\nD) Enter TOTAL DURATION (i.e. 20.34): '))
                print ('\n      ++ Duration Entered into Database ++')
                avg_pace = float(input('\nE)Enter AVERAGE PACE (i.e. 10.44): '))
                print ('\n      ++ Average Pace Entered into Database ++')
                
                def data_entry():
                    c.execute("INSERT INTO database_test VALUES (?, ?, ?, ?, ?)", (id, date, distance, duration, avg_pace))
                    conn.commit()
                # Inputs data into DB
                data_entry()
                
                print ('\n !!! Checking for errors !!!')
                time.sleep(0.5)
                print ('.')
                time.sleep(0.5)
                print ('..')
                time.sleep(0.5)
                print ('...')
                time.sleep(0.5)
                print ('....')
                time.sleep(0.5)
                print ('\n ~~ Successful Upload into Database! ~~')
                
            except Exception as e:
                print ('\n\n*************************')
                print ('ERROR FOUND! Re-Do Entry!:',e)
                print ('*************************')
        
        # PRINT CURRENT Database
        if choice == '2':
            read_from_db()
        
        # UPDATING the Database
        if choice == '3':
            def update_db():
                c.execute('SELECT * FROM database_test')
                # 'i' prints current database information
                i = read_from_db()
                print (i)
                update_column = input('Enter the column name you want to update: ')
                # prints the menu for either updating DATE or all other columns
                update_menu()
                update_choice = input('\nEnter choice number from menu: ')
                if update_choice == '1':
                    date = input('Enter the NEW date (i.e. 2016-01-01): ')
                    return date
                if update_choice == '2':
                    all_other_rows = float(input('Enter the NEW value (i.e. 3.11): '))
                    return all_other_rows
                c.execute('UPDATE database_test SET (?) = (?) WHERE (?) = (?)', (update_column.lower()))
                conn.commit()
            update_db()
        
        # DELETING rows in the Database
        if choice == '4':
            def delete_db():
                c.execute('SELECT * FROM database_test')
                # EDIT THE (?)
                c.execute('DELETE FROM database_test WHERE (?) = (?)', ())
                conn.commit()
            delete_db()
        
        # EXIT out of program
        if choice == '0':
            c.close()
            conn.close()
            print ('\n\n')