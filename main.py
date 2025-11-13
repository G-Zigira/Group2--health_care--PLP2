#this is the main program that calls all the other functions 
#adding the necesarry libraries for sql manipulation and time
import sqlite3
import time

#importing all the functions from the other files in teh directory
from db import init_db, get_connection
from hospitals import refer_to_hospital
from records import review_medical_record
from emergency import send_emergency_alert



#main function

def main():
    
    init_db()
    print("_+_+_+_+_+_+ Welcome to Clinico +_+_+_+_+_+_\n")
    print("Your own Personalised Health direction giver\n")


    name = input("Please enter your full names: ")
    try:
        street_number = int(input("enter your street number (eg: 44,23):"))
    except ValueError:
        print("Your input wasnt invalid so by default your street number will be 0 ")
        street_number = 0
    chronic = input("Do you have any chronic illnesses? (eg: asthma, myopia) If you dont have any type 'None': ")
    time.sleep(2)


    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, street_number, chronic_illness) VALUES (?, ?, ?)", (name, street_number, chronic))
    conn.commit()
    conn.close()


    #this is the loop to the main interface that will allpw the user to acces the other functions
    while True:
        
        print("\n---------MAIN MENU---------")
        print("\n____Services in Clinico____")
        print("1. Refer to a hospital")
        print("2. Review Medical record")
        print("3. Send an Emergency alert")
        print("4. Exit")
        


        choice = input("Choose an option(1-4): ")
        time.sleep(2)

        #conditional operator to call upon the other functions 
        

        if choice == '1':
            refer_to_hospital(name)
        elif choice == '2':
            review_medical_record(name)
        elif choice == '3':
            send_emergency_alert(name)
        elif choice == '4':
            print("Exiting the  Clinico APP. thank you ")
            break
        else:
            print(" Invalid option please try again ")



if __name__ == "__main__":
    main()