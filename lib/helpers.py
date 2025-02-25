# lib/helpers.py
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment


def add_patient():
    name = input("Please input patients name: ")
    illness = input("Please input patients illness: ")
    insurance = input("Does patient have insurance? Y or N: ")
    new_patient = Patient.create(name, illness, insurance)
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
            print(f"ID: {result.id}, Name: {result.name}, Illness: {result.illness}, Insurance: {result.insurance}")
    else:
        print("No patients found.")
    

def verify_insurance():
    name = input("Please enter a patient's name to search: ")
    name = name.strip()

    result = Patient.find_by_name(name)
    if result:
        print(f"Patient { 'DOES' if result.insurance == 'Y' else 'DOES NOT' } have insurance.")
    else:
        print("No patient found.")

def search_doctor():
    name = input("Please enter doctor's name to search: ")
    result = Doctor.find_by_name(name)

    if result:
        print(f"ID: {result.id}, Name: {result.name}, Specialty: {result.specialty}, Hospital: {result.hospital}")
    else:
        print("No patient found with that name.")

def search_specialty():
    specialty = input("Please enter a specialty to search for: ")
    specialty = specialty.strip()

    result = Doctor.find_by_specialty(specialty)

    if result:
        print(f"Doctor {result.name} is a(n) {result.specialty}.")
    else:
        print(f"No specialist found.")

def display_doctors():
    results = Doctor.get_all()

    if results:
        for result in results:
            print(f"ID: {result.id}, Name: {result.name}, Specialty: {result.specialty}, Hospital: {result.hospital}")
    else:
        print("No Doctors found.")

def schedule_appointment():
    patient_name = input("Input patient's name: ")
    doctor_name = input("Input doctor's name: ")
    appointment_date = input("Input the date of the appointment in the format YYYY-MM-DD: ")

    patient_name = patient_name.strip()
    doctor_name = doctor_name.strip()

    patient_result = Patient.find_by_name(patient_name)
    doctor_result = Doctor.find_by_name(doctor_name)

    if patient_result and doctor_result:
        Appointment.create(patient_result, doctor_result, appointment_date)
        print(f"Appointment created. {patient_result.name} meeting with {doctor_result.name} on {appointment_date}.")
    else:
        print("Error creating appointment.")

       

def exit_program():
    print("Exiting! Goodbye.")
    exit()

def display_patient_menu():
    pass

def display_doctor_menu():
    pass
