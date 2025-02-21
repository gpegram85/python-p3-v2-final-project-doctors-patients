# lib/helpers.py
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment


def add_patient():
    name = input("Please input patients name: ")
    illness = input("Please input patients illness: ")
    insurance = input("Does patient have insurance? Y or N: ")
    new_patient = Patient(name, illness, insurance)
    print(f"Patient: {new_patient.name} created.")

def search_patient():
    name = input("Please enter patients name to search: ")
    results = Patient.find_by_name(name)
    for result in results:
        print({result})

def display_patients():
    pass

def verify_insurance():
    pass

def search_doctor():
    pass

def search_specialty():
    pass

def schedule_appointment():
    pass

def exit_program():
    print("Exiting! Goodbye.")
    exit()

def display_patient_menu():
    pass

def display_doctor_menu():
    pass
