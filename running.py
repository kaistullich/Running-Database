import sqlite3

conn = sqlite3.connect('running_stats.db')
c = conn.cursor()


if __name__ == "__main__":

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS running_data(date TEXT, distance REAL, duration REAL, avg_pace REAL)')
    
    date = input('Running the date: ')
    distance = float(input('Enter TOTAL DISTANCE RAN (i.e 2.11): '))
    duration = float(input('Enter TOTAL DURATION (i.e. 20.34): '))
    avg_pace = float(input('Enter AVERAGE PACE (i.e. 10.44): '))
    
    def data_entry():
        c.execute("INSERT INTO running_data VALUES ({}, {}, {}, {})".format(date, distance, duration, avg_pace))
        conn.commit()
        c.close()
        conn.close()

    #Only run 'create_table()' for the FIRST time
    #create_table()
    data_entry()
