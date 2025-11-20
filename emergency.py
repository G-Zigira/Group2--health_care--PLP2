import time

from db import get_connection


def send_emergency_alert(user_name):
    conn = get_connection()
    cursor = conn.cursor()



    cursor.execute('SELECT street_number FROM users WHERE name = ?', (user_name,))
    result = cursor.fetchone()
    if not result:
        print("No user information found.")
        conn.close()
        return


    user_street = result[0] if result[0] is not None else 0


    
    cursor.execute('''SELECT name, address, phone, street_number FROM hospitals''')
    hospitals = cursor.fetchall()


    if not hospitals:
        print("No hospitals were found in the database ")
        conn.close()
        return


   
    nearest = min(hospitals, key=lambda h: abs(h[3] - user_street))

    
    print("\n---- Emergency Hospital RESPONSE Contact ----")
    time.sleep(3)
    print(f"THE Nearest Hospital: {nearest[0]}\nAddress: {nearest[1]}\nCall: {nearest[2]}")


    conn.close()
    print("\nReturning to the main menu ina few seconds...")
    time.sleep(7) 