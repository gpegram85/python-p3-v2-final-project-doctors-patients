#!/usr/bin/env python3

from models.doctor import Doctor
from models.patient import Patient
from models.appointment import Appointment

def seed_database():
    
    Doctor.drop_table()
    Patient.drop_table()
    Appointment.drop_table()

    Doctor.create_table()
    Patient.create_table()
    Appointment.create_table()

    # Seed data creation
    patient_one = Patient.create("Grey", "Migraine", "Y")
    patient_two = Patient.create("Rachel", "Flu", "Y")
    patient_three = Patient.create("Rowan", "Anemia", "N")
    
    doctor_one = Doctor.create("James", "General Practitioner", "Roper St. Francis")
    doctor_two = Doctor.create("Earl", "Enterologist", "Roper St. Francis")
    doctor_three = Doctor.create("Jones", "Pathologist", "Trident Urgent Care")

    print("Database seeded.")

if __name__ == "__main__":
    seed_database()