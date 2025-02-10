# lib/cli.py

from helpers import (
    hello_world,
    exit_program
)

def main() :
    while True:
        menu()
        choice = input(">> ")
        if choice == "1":
            hello_world()
        elif choice == "2":
            exit_program()
        elif choice == "3":
            exit_program()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice! Select again.")

def menu():
    print()
    print("************************")
    print("Please select an option.")
    print("************************")
    print()
    print("1.) Say hello world.")
    print("2.) Press 2 if you are a patient.")
    print("3.) Press 3 if you are a doctor.")
    print("0.) Press 0 to exit the program.")


if __name__ == "__main__":
    main()