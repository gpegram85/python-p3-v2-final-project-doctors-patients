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
    name = input("Please enter patient's name to search: ")
    result = Patient.find_by_name(name)

    if result:
        print(f"ID: {result.id}, Name: {result.name}, Illness: {result.illness}, Insurance: {result.insurance}")
    else:
        print("No patient found with that name.")

def display_patients():
    results = Patient.get_all()

    if results:
        for result in results:
            print(result)
    else:
        print("No patients found.")
    

def verify_insurance():
    pass

def search_doctor():
    name = input("Please enter doctor's name to search: ")
    result = Doctor.find_by_name(name)

    if result:
        print(f"ID: {result.id}, Name: {result.name}, Specialty: {result.specialty}, Hospital: {result.hospital}")
    else:
        print("No patient found with that name.")

def search_specialty():
    pass

def display_doctors():
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
