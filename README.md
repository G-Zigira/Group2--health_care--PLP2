# Clinico

This is a simple command line intertface app that helps the users get hospital referrals, reviews medical records and send emergency alerts to see the hospitals nearbye.

---

## Overview

Clinico is a very simple beginner friendly medical helper program written in Python and uses Sql lite for the database. it uses features like oop and function importing.

---

## Features

1) The program saves user information like the users name, street number and chronic illnesses
2) Allows the user to view and choose from nearby hospitals
3) Permits the simple review of the patients medical records
4) The program sends a basic emergency alert
4) All the data is stored automatically into clinico.db

---

## How to run the app

1) Make sure you have Python  installed in your device.
2) Open the project folder in your terminal.
3) Run:

   ```bash
   python main.py
   ```
4) The app will automatically create the database and start the menu.

---

## Project files

```
main.py        =+ This is the main program that runs and hold everyhting together
db.py          =+ This file handles the database setup and has the hospital info
hospitals.py   =+ This file holds the  hospital referrals function
records.py     =+ This be the part responsible for medical record reviews
emergency.py   =+ This is the file with the emergency alert function
clinico.db     =+ This is the database file created by  db.py
```

---

## Database tables

* **users**: stores name, street number and chronic illness
* **hospitals**: the initialised list of hospitals
* **reviews**: the hospital ratings
* **visits**: user visiting record entries

---

## Quick notes

* You wont need to install anything extra because sqllite is built into Python
* If something breaks or there is an error try deleting clinico.db and running the app again

---

## License

Free to use for learning and personal projects or anythign else
