import sqlite3

CONN = sqlite3.connect('doctors_patients.db')
CURSOR = CONN.cursor()