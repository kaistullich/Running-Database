import sqlite3
import time

conn = sqlite3.connect('running_stats.db')
c = conn.cursor()

def menu():
    print ('\n------------------------')
    print ('    RUNNING DATABASE')
    print ('------------------------\n')
    print ('1) Enter Data')
    print ('0) EXIT')

if __name__ == "__main__":

    choice = ""
    while (choice != '0'):
        menu()
        choice = input('\nEnter number from menu above to continue: ')
        print ('-------------------------------------------')
        if choice == '1':
            try:
                def create_table():
                    c.execute('CREATE TABLE IF NOT EXISTS running_data(date TEXT, distance REAL, duration REAL, avg_pace REAL)')
                
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

                create_table()
                data_entry()
                print ('\n !!! Checking for errors !!!')
                time.sleep(1)
                print ('.')
                time.sleep(1)
                print ('..')
                time.sleep(1)
                print ('...')
                time.sleep(1)
                print ('....')
                time.sleep(1)
                print ('\n ~~ Successful Upload into Database! ~~')
                
            
            except Exception as e:
                print ('\n\n*************************')
                print ('ERROR FOUND! Re-Do Entry!:',e)
                print ('*************************')
        
        if choice == '0':
            print ('\n%% EXITED %%')