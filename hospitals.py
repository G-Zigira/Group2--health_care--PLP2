import sqlite3
import time
from db import get_connection

# function that except paramter user_name as input


def refer_to_hospital(user_name):
    # connect to the database by using the get_connection function
    conn = get_connection()
    cursor = conn.cursor()

    # create a list that contain some of the issue and then prompt the user to choose one
    issues = [
        ("Consultation", "General doctor checkup and conversing with the doctor"),
        ("Pediatry", "Medical care for children and specialised consultation for them"),
        ("Blood Test", "Basic blood sample analysis for pathogens and others "),
        ("Dental", "Tooth and gum treatments together with braces"),
        ("Eye Care", "Vision testing and treatment together with glasses")
    ]

    print("\n Medical services available at the moment : ")
    for i, (issue, desc) in enumerate(issues, 1):
        print(f"{i}. {issue} - {desc}")

    try:
        choice = int(
            input("Select the type of medical attention you need right now: "))
        medical_issue = issues[choice - 1][0]
    except (ValueError, IndexError):
        print("Invalid choice ")
        conn.close()
        return

    print("\n---- Available Hospitals ----")
    cursor.execute('''SELECT h.id, h.name, h.address, h.phone, IFNULL(AVG(r.rating), 0)
                      FROM hospitals h LEFT JOIN reviews r ON h.id = r.hospital_id
                      GROUP BY h.id''')

    hospitals = cursor.fetchall()
    for i, (hid, name, address, phone, avg_rating) in enumerate(hospitals, 1):
        print(f"{i}. {name} - {address} (⭐ {avg_rating:.1f})")

    try:
        hosp_choice = int(input("Select a hospital: "))
        hospital = hospitals[hosp_choice - 1]
    except (ValueError, IndexError):
        print("Invalid hospital selection ")
        conn.close()
        return

    print(
        f"\nHospital Info:\nName: {hospital[1]}\nAddress: {hospital[2]}\nPhone: {hospital[3]}")

    cursor.execute('INSERT INTO visits (user_name, hospital_name, medical_issue) VALUES (?, ?, ?)',
                   (user_name, hospital[1], medical_issue))

    # ask the user for rate to the hospital then add to the database
    try:
        rating = int(input("\nRate this hospital (1-5): "))
        if 1 <= rating <= 5:
            cursor.execute(
                'INSERT INTO reviews (hospital_id, rating) VALUES (?, ?)', (hospital[0], rating))
        else:
            print(" Invalid rating, skipping3 this review ")
    except ValueError:
        print(" Invalid input, skipping review ")

    # commit the change to the database and then close the connection
    conn.commit()
    conn.close()


time.sleep(7)
