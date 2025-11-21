#!/usr/bin/python3
# this is the main program that calls all the other functions
import sqlite3
import time
import sys

from db import init_db, get_connection
from doctor import doctor_menu
from hospitals import refer_to_hospital
from records import review_medical_record
from emergency import send_emergency_alert


class ClinicoApp:
    def __init__(self):
        """initializing  the clinico app"""
        init_db()
        self.name = None
        self.street_number = None
        self.chronic = None

    def collect_user_info(self):
        """handles the input at the start and saving the information of the new user """
        print("\n_+_+_+_+_+_+ Welcome to Clinico +_+_+_+_+_+_\n")
        print("Your own Personalised Health direction giver\n")
        
        print("choose your selected role:")
        print("1. Patient")
        print("2. Doctor")

        role = input("Enter your choice (1 or 2): ")

        if role == "2":
            hospitals = [
                 "Kigali General Hospital",
                "Rwanda Medical Center",
                "Nyamirambo Health Clinic",
                "CHUK Teaching Hospital"
            ]

            print("\nSelect hospital:")
            for i, h in enumerate(hospitals, start=1):
                print(f"{i}. {h}")

            h_choice = int(input("Choose hospital (1-4): "))
            hospital_name = hospitals[h_choice - 1]

            pin = input("Enter 3-digit doctor PIN: ")

            if pin == "357":  
                doctor_menu(hospital_name)
                sys.exit()        
            else:
                print("the PINyou entered is incorrect, leaving clinico")
                sys.exit()

        self.name = input("Please enter your full names: ")

        try:
            self.street_number = int(input("Enter your street number (eg: 44, 23): "))
        except ValueError:
            print("Your input was invalid, so by default your street number will be 0.")
            self.street_number = 0

        self.chronic = input(
            "Do you have any chronic illnesses? (eg: asthma, myopia). "
            "If you don't have any type 'None': "
        )

        time.sleep(2)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, street_number, chronic_illness) VALUES (?, ?, ?)",
            (self.name, self.street_number, self.chronic),
        )
        conn.commit()
        conn.close()

    def main_menu(self):
        """Displays main menu and handles navigation."""
        while True:
            print("\n---------MAIN MENU---------")
            print("\n____Services in Clinico____")
            print("1. Refer to a hospital")
            print("2. Show personal nedical record")
            print("3. Send an emergency alert")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")
            time.sleep(2)

            if choice == '1':
                refer_to_hospital(self.name)
            elif choice == '2':
                review_medical_record(self.name)
            elif choice == '3':
                send_emergency_alert(self.name)
            elif choice == '4':
                print("Exiting the Clinico APP thank you")
                break
            else:
                print("The option you picked is invalid please try again ")

    def run(self):
        """Runs the complete application."""
        self.collect_user_info()
        self.main_menu()


if __name__ == "__main__":
    app = ClinicoApp()
    app.run()
