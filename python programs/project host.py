
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path(__file__).with_name("hospital_data.json")


def load_data():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            for key in ("patients", "doctors", "appointments", "bills"):
                data.setdefault(key, [])
            return data
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved data. Starting with empty records.")
    return {"patients": [], "doctors": [], "appointments": [], "bills": []}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def next_id(records, prefix):
    return f"{prefix}{max((int(r['id'][1:]) for r in records), default=0) + 1:04d}"


def prompt(label, required=True):
    while True:
        value = input(label).strip()
        if value or not required:
            return value
        print("This field is required.")


def find_record(records, record_id):
    return next((r for r in records if r["id"].lower() == record_id.lower()), None)


def add_patient(data):
    print("\nAdd patient")
    patient = {
        "id": next_id(data["patients"], "P"),
        "name": prompt("Full name: "),
        "age": prompt("Age: "),
        "gender": prompt("Gender: "),
        "phone": prompt("Phone: "),
        "address": prompt("Address: ", required=False),
    }
    data["patients"].append(patient)
    save_data(data)
    print(f"Patient added. ID: {patient['id']}")


def list_records(title, records, fields):
    print(f"\n{title}")
    if not records:
        print("No records found.")
        return
    for record in records:
        print(" | ".join(f"{field}: {record.get(field, '-') }" for field in fields))


def add_doctor(data):
    print("\nAdd doctor")
    doctor = {
        "id": next_id(data["doctors"], "D"),
        "name": prompt("Full name: "),
        "specialty": prompt("Specialty: "),
        "phone": prompt("Phone: "),
    }
    data["doctors"].append(doctor)
    save_data(data)
    print(f"Doctor added. ID: {doctor['id']}")


def add_appointment(data):
    print("\nSchedule appointment")
    if not data["patients"] or not data["doctors"]:
        print("Add at least one patient and one doctor first.")
        return
    list_records("Patients", data["patients"], ["id", "name"])
    patient = find_record(data["patients"], prompt("Patient ID: "))
    if not patient:
        print("Patient not found.")
        return
    list_records("Doctors", data["doctors"], ["id", "name", "specialty"])
    doctor = find_record(data["doctors"], prompt("Doctor ID: "))
    if not doctor:
        print("Doctor not found.")
        return
    while True:
        date_time = prompt("Appointment date and time (YYYY-MM-DD HH:MM): ")
        try:
            datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Use the format YYYY-MM-DD HH:MM.")
    appointment = {
        "id": next_id(data["appointments"], "A"),
        "patient_id": patient["id"],
        "patient": patient["name"],
        "doctor_id": doctor["id"],
        "doctor": doctor["name"],
        "date_time": date_time,
        "reason": prompt("Reason for visit: ", required=False),
    }
    data["appointments"].append(appointment)
    save_data(data)
    print(f"Appointment scheduled. ID: {appointment['id']}")


def create_bill(data):
    print("\nCreate bill")
    if not data["patients"]:
        print("Add a patient first.")
        return
    list_records("Patients", data["patients"], ["id", "name"])
    patient = find_record(data["patients"], prompt("Patient ID: "))
    if not patient:
        print("Patient not found.")
        return
    while True:
        try:
            amount = float(prompt("Amount: "))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid non-negative amount.")
    bill = {
        "id": next_id(data["bills"], "B"),
        "patient_id": patient["id"],
        "patient": patient["name"],
        "amount": round(amount, 2),
        "description": prompt("Description: ", required=False),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "paid": False,
    }
    data["bills"].append(bill)
    save_data(data)
    print(f"Bill created. ID: {bill['id']}")


def mark_bill_paid(data):
    list_records("Bills", data["bills"], ["id", "patient", "amount", "date", "paid"])
    bill = find_record(data["bills"], prompt("Bill ID to mark paid: "))
    if not bill:
        print("Bill not found.")
        return
    bill["paid"] = True
    save_data(data)
    print("Bill marked as paid.")


def main():
    data = load_data()
    actions = {
        "1": lambda: add_patient(data),
        "2": lambda: list_records("Patients", data["patients"], ["id", "name", "age", "gender", "phone", "address"]),
        "3": lambda: add_doctor(data),
        "4": lambda: list_records("Doctors", data["doctors"], ["id", "name", "specialty", "phone"]),
        "5": lambda: add_appointment(data),
        "6": lambda: list_records("Appointments", data["appointments"], ["id", "patient", "doctor", "date_time", "reason"]),
        "7": lambda: create_bill(data),
        "8": lambda: list_records("Bills", data["bills"], ["id", "patient", "amount", "description", "date", "paid"]),
        "9": lambda: mark_bill_paid(data),
    }
    while True:
        print("\n=== Hospital Management System ===")
        print("1. Add patient\n2. View patients\n3. Add doctor\n4. View doctors")
        print("5. Schedule appointment\n6. View appointments\n7. Create bill\n8. View bills\n9. Mark bill paid\n0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Please choose a listed option.")


if __name__ == "__main__":
    main()
