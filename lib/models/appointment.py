from patient import Patient
from doctor import Doctor

class Appointment:
    
    def __init__(self, patient, doctor, date, id=None):
        if not isinstance(patient, Patient):
            raise AttributeError("Patient must be an instance of Patient.")
        self._patient = patient

        if not isinstance(doctor, Doctor):
            raise AttributeError("Doctor must be an instance of Doctor.")
        self.doctor = doctor

        if not isinstance(date, str) or not len(date) >= 8:
            raise AttributeError("Date must be a string in the format of MMDDYYYY")
        self.date = date

    @property
    def patient(self):
        return self._patient
        
    @patient.setter
    def patient(self, new_patient):
        if not isinstance(new_patient, Patient):
            raise AttributeError("Patient must be an instance of Patient")
        self._patient = new_patient

    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor (self, new_doctor):
        if not isinstance(new_doctor, Doctor):
            raise AttributeError("Doctor must be an instance of Doctor")
        self._doctor = new_doctor

    @property
    def date(self):
        return self._date
    
    @date.setter
    def sate(self, new_date):
        if not isinstance(new_date, str) or not len(new_date) >= 8:
            self._date = new_date