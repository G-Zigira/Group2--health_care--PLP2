
import sqlite3

import time

from db import init_db, get_connection
from hospitals import refer_to_hospital
from records import review_medical_record
from emergency import send_emergency_alert





def main():
    init_db()
    print("Welcome to Clinico — Your Personal Health Assistant!\n")


    name = input("Enter your full name: ")
    try:
        street_number = int(input("Enter your street number (e.g., 23):"))
    except ValueError:
        print("Invalid input. Setting street number to 0.")
        street_number = 0
    chronic = input("Do you have any chronic illnesses (e.g., asthma, myopia)? If none, type 'None': ")
    time.sleep(2)


    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, street_number, chronic_illness) VALUES (?, ?, ?)", (name, street_number, chronic))
    conn.commit()
    conn.close()


    
    while True:
        print("\n-------- MAIN MENU --------")
        print("\n___ Services in Clinico___")
        print("1. Refer to a hospital")
        print("2. Review Medical record")
        print("3. Send an Emergency alert")
        print("4. Exit")
        


        choice = input("Choose an option(1-4): ")
        time.sleep(2)



        if choice == '1':
            refer_to_hospital(name)
        elif choice == '2':
            review_medical_record(name)
        elif choice == '3':
            send_emergency_alert(name)
        elif choice == '4':
            print("Exiting Clinico. thank you ")
            break
        else:
            print("Invalid option please try again.")



if __name__ == "__main__":
    main()