import time

from db import get_connection


def review_medical_record(user_name):
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute('SELECT name, street_number, chronic_illness FROM users WHERE name = ?', (user_name,))
    user = cursor.fetchone()
    if not user:
        print("No record found.")
        conn.close()
        return


    print(f"\n--- Medical Record for {user_name} ---")
    print(f"Address: {user[1]} St")
    print(f"Chronic Illness: {user[2] if user[2] else 'None'}")


    cursor.execute('SELECT hospital_name, medical_issue FROM visits WHERE user_name = ?', (user_name,))
    visits = cursor.fetchall()


    if visits:
        print("\nVisited Hospitals:")
        for hname, issue in visits:
            print(f"- {hname} ({issue})")
    else:
        print("\nNo previous hospital visits recorded.")


    conn.close()

# this is for a short delay before returning to main menu
    print("\nReturning to the main menu in a few secondss...")
    time.sleep(7) 