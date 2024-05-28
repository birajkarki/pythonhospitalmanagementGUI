from admin import Admin
from doctor import Doctor
from patient import Patient
from gui import HospitalGUI
import tkinter as tk

def main():
    # Initializing admin, doctors, and patients
    admin = Admin('admin', '123', 'B1 1AB') 
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jane', 'Doe', 'Pediatrics'), Doctor('Carlos', 'Johnson', 'Cardiology')]
    patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234'), Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB'), Patient('David', 'Smith', 15, '07123456789', 'C1 ABC')]
    discharged_patients = []

    root = tk.Tk()
    app = HospitalGUI(root, admin, doctors, patients, discharged_patients)
    root.mainloop()

if __name__ == '__main__':
    main()
