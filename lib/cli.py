# lib/cli.py

from helpers import (
    exit_program,
    add_patient,
    search_patient,
    display_patients,
    verify_insurance,
    search_doctor,
    search_specialty,
    schedule_appointment
)

def main() :
    while True:
        menu()
        choice = input(">> ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            search_patient()
        elif choice == "3":
            display_patients()
        elif choice == "4":
            verify_insurance()
        elif choice == "5":
            search_doctor()
        elif choice == "6":
            search_specialty()
        elif choice == "7":
            schedule_appointment()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice! Select again.")

def menu():
    print()
    print("------------------------")
    print("Please select an option.")
    print("------------------------")
    print()
    print("1.) Press 1 to add a new patient.")
    print("2.) Press 2 to lookup a patient.")
    print("3.) Press 3 to list all patients.")
    print("4.) Press 4 to check for patient insurance coverage.")
    print("5.) Press 5 to lookup a doctor.")
    print("6.) Press 6 to find a specialist.")
    print("7.) Press 7 to schedule an appointment.")
    print("0.) Press 0 to exit the program.")

if __name__ == "__main__":
    main()