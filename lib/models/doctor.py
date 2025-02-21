from models.__init__ import CONN, CURSOR

class Doctor:
    
    def __init__(self, name, specialty, hospital, id=None):
        if not isinstance(name, str) or not 0 < len(name):
            raise AttributeError("Name must be a non-empty string.")
        self.name = name

        if not isinstance(specialty, str) or not 0 < len(specialty):
            raise AttributeError("Specialty must be a non-empty string.")
        self.specialty = specialty

        if not isinstance(hospital, str) or not 0 < len(hospital):
            raise AttributeError("Hospital name must be a non-empty string.")
        self.hospital = hospital

        self.id = id

    @classmethod
    def create_table(cls):
        """Create the doctors table."""
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                specialty TEXT NOT NULL,
                hospital TEXT NOT NULL
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the doctors table if it exists."""
        sql = "DROP TABLE IF EXISTS doctors;"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, specialty, hospital):
        """Create and save a new doctor instance."""
        doctor = cls(name, specialty, hospital)
        doctor.save()
        return doctor

    @classmethod
    def find_by_id(cls, id):
        """Find a doctor by ID."""
        sql = "SELECT * FROM doctors WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls(*row) if row else None

    @classmethod
    def get_all(cls):
        """Return a list of all doctors."""
        sql = "SELECT * FROM doctors"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Return a Doctor object from a database row."""
        return cls(row[1], row[2], row[3], id=row[0])

    def get_patients(self):
        from models.patient import Patient
        """Retrieve all patients associated with this doctor through appointments."""
        sql = """
            SELECT patients.* FROM patients
            JOIN appointments ON patients.id = appointments.patient_id
            WHERE appointments.doctor_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Patient(*row) for row in rows]

    def save(self):
        """Insert or update a doctor record in the database."""
        if self.id is None:
            sql = """
                INSERT INTO doctors (name, specialty, hospital)
                VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.specialty, self.hospital))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()

    def update(self):
        """Update an existing doctor in the database."""
        sql = """
            UPDATE doctors
            SET name = ?, specialty = ?, hospital = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.specialty, self.hospital, self.id))
        CONN.commit()

    def delete(self):
        """Delete a doctor from the database."""
        sql = "DELETE FROM doctors WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
