#!/usr/bin/python3
# Used for pauses to make output more readable
import time
# Import functions to connect to the database
from db import get_connection

# Connect the database and create the cursor object to execute SQL queries
def send_emergency_alert(user_name):
    conn = get_connection()
    cursor = conn.cursor()


    # Get the user's street number from the database
    cursor.execute('SELECT street_number FROM users WHERE name = ?', (user_name,))
    result = cursor.fetchone()

    if not result: # If user is not found
        print("No user information found.")
        conn.close()
        return


    user_street = result[0] if result[0] is not None else 0 # Default to 0 if street_number is None


    # Fetch all hospital from the database
    cursor.execute('''SELECT name, address, phone, street_number FROM hospitals''')
    hospitals = cursor.fetchall()


    if not hospitals: # If no hosiptal are found
        print("No hospitals were found in the database ")
        conn.close()
        return


    # Find the nearest hospital based on street number  
    nearest = min(hospitals, key=lambda h: abs(h[3] - user_street))

    # Display emergency hospital information  
    print("\n---- Emergency Hospital RESPONSE Contact ----")
    time.sleep(3)
    print(f"THE Nearest Hospital: {nearest[0]}\nAddress: {nearest[1]}\nCall: {nearest[2]}")

    # Close connection and return to main menu
    conn.close()
    print("\nReturning to the main menu ina few seconds...")
    time.sleep(7) 
