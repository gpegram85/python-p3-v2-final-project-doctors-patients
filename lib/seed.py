#!/usr/bin/env python3

from models import CONN, CURSOR
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

    sql = """
        CREATE TABLE IF NOT EXISTS players_games (
        id INTERGER PRIMARY KEY,
        player_id INTEGER,
        game_id INTEGER,
        score TEXT,
        FOREIGN KEY (player_id) REFERENCES players(id),
        FOREIGN KEY (game_id) REFERENCES games(id)
        );
    """
    CURSOR.execute(sql)
    CONN.commit()

    # Seed data creation
    patient_one = Patient.create("Grey", "Migraine", "Y")
    patient_two = Patient.create("Rachel", "Flu", "Y")
    patient_three = Patient.create("Rowan", "Anemia", "N")
    
    doctor_one = Doctor.create("James", "General Practitioner", "Roper St. Francis")
    doctor_two = Doctor.create("Earl", "Enterologist", "Roper St. Francis")
    doctor_three = Doctor.create("Jones", "Pathologist", "Trident Urgent Care")

    print("Database seeded.")
