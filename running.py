import sqlite3
import time

conn = sqlite3.connect('running_stats.db')
c = conn.cursor()

def menu():
    print ('\n------------------------')
    print ('    RUNNING DATABASE')
    print ('------------------------\n')
    print ('1) Enter Data')
    print ('2) Show all data within Database')
    print ('3) Update a certain row')
    print ('4) Delete a certain row')
    print ('0) EXIT')

if __name__ == "__main__":

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS running_data(date TEXT, distance REAL, duration REAL, avg_pace REAL)')
    create_table()
    
    choice = ""
    while (choice != '0'):
        menu()
        choice = input('\nEnter number from menu above to continue: ')
        print ('-------------------------------------------')
        
        # Inserting into Database
        if choice == '1':
            try:
                date = input('\n\n\nA) Enter the DATE for the run completed (i.e. 2016-01-10): ')
                print ('\n      ++ Date Entered into Database ++')
                distance = float(input('\nB) Enter TOTAL DISTANCE RAN (i.e 2.11): '))
                print ('\n      ++ Distance Entered into Database ++')
                duration = float(input('\nC) Enter TOTAL DURATION (i.e. 20.34): '))
                print ('\n      ++ Duration Entered into Database ++')
                avg_pace = float(input('\nD)Enter AVERAGE PACE (i.e. 10.44): '))
                print ('\n      ++ Average Pace Entered into Database ++')
                
                def data_entry():
                    c.execute("INSERT INTO running_data VALUES (?, ?, ?, ?)", (date, distance, duration, avg_pace))
                    conn.commit()
                    c.close()
                    conn.close()

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
        
        # Print all the rows within the database
        if choice == '2':
            def read_from_db():
                c.execute('SELECT * FROM running_data')
                data = c.fetchall()
                print (data)
            read_from_db()
        
        # Updating the Database
        if choice == '3':
            def update_db():
                c.execute('SELECT * FROM running_data')
                # EDIT THE (?)
                c.execute('UPDATE running_data SET value = (?) WHERE -- <enter column name> =  (?)')
                conn.commit()
            update_db()
        
        # Deleting rows in the Database
        if choice == '4':
            def delete_db():
                c.execute('SELECT * FROM running_data')
                # EDIT THE (?)
                c.execute('DELETE FROM running_data WHERE -- <enter column name> = (?)')
                conn.commit()
            delete_db()
        
        # Exit out of program
        if choice == '0':
            print ('\n%% EXITED %%')