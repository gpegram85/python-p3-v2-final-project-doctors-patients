from models.__init__ import CONN, CURSOR

class Patient:

     def __init__(self, name, illness, insurance, id=None):
          if not isinstance(name, str) or not len(name) > 0:
               raise AttributeError("Name must be a string longer than 0 characters.")
          self.name = name

          if not isinstance(illness, str) or not (0 < len(illness) <= 20):
               raise AttributeError("Illness must be a string between 0 and 20 characters.")
          self.illness = illness

          if not isinstance(insurance, str) or insurance not in ("Y", "N"):
               raise AttributeError("Insurance must be either 'Y' or 'N'")
          self.insurance = insurance

          self.id = id

     @classmethod
     def create_table(cls):
        """Create the patients table."""
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                illness TEXT NOT NULL,
                insurance CHAR NOT NULL CHECK(insurance IN ('Y', 'N'))
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

     @classmethod
     def drop_table(cls):
        """Drop the patients table if it exists."""
        sql = "DROP TABLE IF EXISTS patients;"
        CURSOR.execute(sql)
        CONN.commit()

     @classmethod
     def create(cls, name, illness, insurance):
          """Create and save a new patient instance."""
          patient = cls(name, illness, insurance)
          patient.save()
          return patient

     @classmethod
     def find_by_id(cls, id):
          """Find a patient by ID."""
          sql = "SELECT * FROM patients WHERE id = ?"
          row = CURSOR.execute(sql, (id,)).fetchone()
          return cls(*row) if row else None
     
     @classmethod
     def find_by_name(cls, name):
         """Find a petient by name."""
         sql = "SELECT * FROM patients WHERE name = ?"
         row = CURSOR.execute(sql, (name,)).fetchall()
         return cls(*row) if row else None

     @classmethod
     def get_all(cls):
          """Return a list of all patients."""
          sql = "SELECT * FROM patients"
          rows = CURSOR.execute(sql).fetchall()
          return [cls.instance_from_db(row) for row in rows]

     @classmethod
     def instance_from_db(cls, row):
        """Return a Patient object from a database row."""
        return cls(row[1], row[2], row[3], id=row[0])

     def get_doctors(self):
          from models.doctor import Doctor
          """Retrieve all doctors associated with this patient through appointments."""
          sql = """
          SELECT doctors.* FROM doctors
          JOIN appointments ON doctors.id = appointments.doctor_id
          WHERE appointments.patient_id = ?
          """
          rows = CURSOR.execute(sql, (self.id,)).fetchall()
          return [Doctor(*row) for row in rows]

     def save(self):
        """Insert or update a patient record in the database."""
        if self.id is None:
            sql = "INSERT INTO patients (name, illness, insurance) VALUES (?, ?, ?)"
            CURSOR.execute(sql, (self.name, self.illness, self.insurance))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            self.update()

     def update(self):
          """Update an existing patient in the database."""
          sql = """
               UPDATE patients
               SET name = ?, illness = ?, insurance = ?
               WHERE id = ?
          """
          CURSOR.execute(sql, (self.name, self.illness, self.insurance, self.id))
          CONN.commit()

     def delete(self):
          """Delete a patient from the database."""
          sql = "DELETE FROM patients WHERE id = ?"
          CURSOR.execute(sql, (self.id,))
          CONN.commit()
          self.id = None
