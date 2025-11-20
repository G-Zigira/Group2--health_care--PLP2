import sqlite3


def get_connection():
    return sqlite3.connect('clinico.db')




def init_db():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      street_number INTEGER,
                      chronic_illness TEXT
    )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (
                      id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      name TEXT NOT NULL,
                      address TEXT NOT NULL,
                      phone TEXT NOT NULL,
                      street_number INTEGER
    )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      hospital_id INTEGER,
                      rating INTEGER,
                      FOREIGN KEY (hospital_id) REFERENCES hospitals(id)
    )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS visits (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_name TEXT,
                      hospital_name TEXT,
                      medical_issue TEXT
    )''')


    cursor.execute('SELECT COUNT(*) FROM hospitals')
    if cursor.fetchone()[0] == 0:
        hospitals = [
            ("Kigali General Hospital", "12 Kimironko Rd", "0788001122",12),
            ("Rwanda Medical Center", "45 Remera St", "0788123456",45),
            ("Nyamirambo Health Clinic", "75 Nyamirambo Ave", "0788765432",75),
            ("CHUK Teaching Hospital", "KK 102 St", "0788987654",102)
        ]
        cursor.executemany('INSERT INTO hospitals (name, address, phone, street_number) VALUES (?, ?, ?, ?)', hospitals)



    conn.commit()
    conn.close()



