from models.patient import Patient
from models.doctor import Doctor
from models.__init__ import CONN, CURSOR

class Appointment:
    
    def __init__(self, id, patient, doctor, date):
        if not isinstance(patient, Patient):
            raise AttributeError("Patient must be an instance of Patient.")
        self.patient = patient

        if not isinstance(doctor, Doctor):
            raise AttributeError("Doctor must be an instance of Doctor.")
        self.doctor = doctor

        if not isinstance(date, str) or len(date) != 10:
            raise AttributeError("Date must be a string in the format YYYY-MM-DD.")
        self.date = date

        self.id = id

    @classmethod
    def create_table(cls):
        """Create the appointments table with foreign keys."""
        sql = """
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                date TEXT NOT NULL CHECK(length(date) = 10), 
                FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
                FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the appointments table if it exists."""
        sql = "DROP TABLE IF EXISTS appointments;"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, patient, doctor, date):
        """Create and save a new Appointment instance."""
        appointment = cls(patient, doctor, date)
        appointment.save()
        return appointment

    @classmethod
    def find_by_id(cls, id):
        """Find an appointment by ID."""
        sql = "SELECT * FROM appointments WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def get_all(cls):
        """Return a list of all appointments."""
        sql = "SELECT * FROM appointments"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return an Appointment object from a database row."""
        patient = Patient.find_by_id(row[1])
        doctor = Doctor.find_by_id(row[2])
        return cls(patient, doctor, row[3], id=row[0])

    def save(self):
        """Insert or update an appointment record in the database."""
        if self.id is None:
            sql = "INSERT INTO appointments (patient_id, doctor_id, date) VALUES (?, ?, ?)"
            CURSOR.execute(sql, (self.patient.id, self.doctor.id, self.date))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()

    def update(self):
        """Update an existing appointment in the database."""
        sql = """
            UPDATE appointments
            SET patient_id = ?, doctor_id = ?, date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.patient.id, self.doctor.id, self.date, self.id))
        CONN.commit()

    def delete(self):
        """Delete an appointment from the database."""
        sql = "DELETE FROM appointments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
