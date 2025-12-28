from datetime import datetime

LOG_FILE = "keystrokes.log"

def log_keys(text):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} : {text}\n")

def view_logs():
    try:
        with open(LOG_FILE, "r") as f:
            print("\n--- Logged Keystrokes ---")
            print(f.read())
    except FileNotFoundError:
        print("No logs found.")

print("ETHICAL KEYLOGGER (EDUCATIONAL PURPOSES ONLY)")
print("This program logs text typed INTO THIS APPLICATION ONLY.")
print("No system-wide monitoring is performed.")
print()

choice = input("Do you consent to continue? (yes/no): ").lower()

if choice != "yes":
    print("Consent not given. Exiting.")
    exit()

while True:
    print("\n1. Start logging")
    print("2. View logs")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        text = input("Type something to log: ")
        log_keys(text)
        print("Text logged successfully.")

    elif option == "2":
        view_logs()

    elif option == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid option.")
