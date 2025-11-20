#this file handles database initialisation
import sqlite3

# This creates and returns a  connection to the database
def get_connection():
    return sqlite3.connect('clinico.db')


# This  initializes and sets up all database tables

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

# Creates a table for storing user information

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      street_number INTEGER,
                      chronic_illness TEXT
    )''')

# Creates a table for storing hospital information

    cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (
                      id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      name TEXT NOT NULL,
                      address TEXT NOT NULL,
                      phone TEXT NOT NULL,
                      street_number INTEGER
    )''')

# Creates a table for hospital reviews

    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      hospital_id INTEGER,
                      rating INTEGER,
                      FOREIGN KEY (hospital_id) REFERENCES hospitals(id)
    )''')

# Creates a table for recording visits made by users

    cursor.execute('''CREATE TABLE IF NOT EXISTS visits (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_name TEXT,
                      hospital_name TEXT,
                      medical_issue TEXT
    )''')

# This Checks if hospitals table is empty and add default data

    cursor.execute('SELECT COUNT(*) FROM hospitals')
    if cursor.fetchone()[0] == 0:
        hospitals = [
            ("Kigali General Hospital", "12 Kimironko Rd", "0788001122",12),
            ("Rwanda Medical Center", "45 Remera St", "0788123456",45),
            ("Nyamirambo Health Clinic", "75 Nyamirambo Ave", "0788765432",75),
            ("CHUK Teaching Hospital", "KK 102 St", "0788987654",102)
        ]

        # Inserts all default hospitals into the table

        cursor.executemany('INSERT INTO hospitals (name, address, phone, street_number) VALUES (?, ?, ?, ?)', hospitals)


# This Saves the changes and closes the  connection
    
    conn.commit()
    conn.close()




