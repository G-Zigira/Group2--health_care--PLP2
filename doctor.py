import time
from db import get_connection


def doctor_menu(hospital_name):
    while True:
        print("\n------ DOCTOR MENU ------")
        print("1. Review patient records")
        print("2. View hospital rating")
        print("3. Exit to Clinico")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            review_patient_records(hospital_name)
        elif choice == "2":
            view_hospital_rating(hospital_name)
        elif choice == "3":
            print("Exiting Doctor Menu...")
            time.sleep(3)
            break
        else:
            print("Invalid choice. Try again.")
            

def review_patient_records(hospital_name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_name, medical_issue FROM visits WHERE hospital_name = ?", (hospital_name,))
    rows = cursor.fetchall()

    conn.close()

    print(f"\nPatients that came to {hospital_name}:")
    if not rows:
        print("No patient records found.")
    else:
        for patient, issue in rows:
            print(f"- {patient} | Reason: {issue}")


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
        print(f"\nRating for {hospital_name}: {avg_rating:.1f} ⭐")
    else:
        print(f"\nRating for {hospital_name}: No reviews yet")
