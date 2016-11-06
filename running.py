import sqlite3

conn = sqlite3.connect('running_stats.db')
c = conn.cursor()


if __name__ == "__main__":

    def create_table():
        c.execute('CREATE TABLE IF NOT EXISTS running_data(date TEXT, distance REAL, duration REAL, avg_pace REAL)')
    
    date = input('Running date: ')
    distance = float(input('Enter TOTAL DISTANCE RAN: '))
    duration = float(input('Enter TOTAL DURATION: '))
    avg_pace = float(input('Enter AVERAGE PACE: '))
    
    def data_entry():
        c.execute("INSERT INTO running_data VALUES (%s, %.2f, %.2f, %.2f)" % (date, distance, duration, avg_pace))
        conn.commit()
        c.close()
        conn.close()


    create_table()
    data_entry()
