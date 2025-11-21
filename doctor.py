#!/usr/bin/python3
import time
from db import get_connection


def doctor_menu(hospital_name):
    while True:
        print("\n-------DOCTOR MENU-------")
        print("1. Review the patient records")
        print("2. View the hospital rating")
        print("3. Exit Clinico")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            review_patient_records(hospital_name)
        elif choice == "2":
            view_hospital_rating(hospital_name)
        elif choice == "3":
            print("Exiting the Clinico app thankyou")
            time.sleep(3)
            break
        else:
            print("the input you entered is invalid please try again.")
            

def review_patient_records(hospital_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_name, medical_issue FROM visits WHERE hospital_name = ?", (hospital_name,))
    rows = cursor.fetchall()

    conn.close()

    print(f"\nPatients that came to {hospital_name}:")
    if not rows:
        print("No patient records were found")
    else:
        for patient, issue in rows:
            print(f"- {patient} | Reason for visit: {issue}")


def view_hospital_rating(hospital_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(rating)
        FROM reviews
        JOIN hospitals ON reviews.hospital_id = hospitals.id
        WHERE hospitals.name = ?
    """, (hospital_name,))

    avg_rating = cursor.fetchone()[0]
    conn.close()

    if avg_rating:
        print(f"\nThe rating for {hospital_name}: {avg_rating:.1f} ⭐")
    else:
        print(f"\nThe rating for {hospital_name}: there are no reviews at the moment")
