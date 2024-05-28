import tkinter as tk
from tkinter import messagebox

class HospitalGUI:
    def __init__(self, root, admin, doctors, patients, discharged_patients):
        self.root = root
        self.admin = admin
        self.doctors = doctors
        self.patients = patients
        self.discharged_patients = discharged_patients

        self.root.title("Hospital Management System")
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_frame()
        self.root.geometry("300x200")

        tk.Label(self.root, text="Admin Login").pack()
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.handle_login).pack()

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.admin.login(username, password):
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    def create_main_menu(self):
        self.clear_frame()
        self.root.geometry("400x300")

        tk.Button(self.root, text="Manage Doctors", command=self.manage_doctors).pack(fill=tk.X)
        tk.Button(self.root, text="View Patients", command=self.view_patients).pack(fill=tk.X)
        tk.Button(self.root, text="Discharge Patient", command=self.discharge_patient).pack(fill=tk.X)
        tk.Button(self.root, text="View Discharged Patients", command=self.view_discharged_patients).pack(fill=tk.X)
        tk.Button(self.root, text="Assign Doctor to Patient", command=self.assign_doctor_to_patient).pack(fill=tk.X)
        tk.Button(self.root, text="Update Admin Details", command=self.update_admin_details).pack(fill=tk.X)

    def manage_doctors(self):
        self.clear_frame()
        self.root.geometry("500x400")

        tk.Label(self.root, text="Manage Doctors").pack()
        tk.Button(self.root, text="Register Doctor", command=self.register_doctor).pack(fill=tk.X)
        tk.Button(self.root, text="View Doctors", command=self.view_doctors).pack(fill=tk.X)
        tk.Button(self.root, text="Update Doctor", command=self.update_doctor).pack(fill=tk.X)
        tk.Button(self.root, text="Delete Doctor", command=self.delete_doctor).pack(fill=tk.X)
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack(fill=tk.X)

    def register_doctor(self):
        self.clear_frame()
        tk.Label(self.root, text="Register Doctor").pack()
        tk.Label(self.root, text="First Name").pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()
        tk.Label(self.root, text="Surname").pack()
        self.surname_entry = tk.Entry(self.root)
        self.surname_entry.pack()
        tk.Label(self.root, text="Speciality").pack()
        self.speciality_entry = tk.Entry(self.root)
        self.speciality_entry.pack()

        tk.Button(self.root, text="Register", command=self.handle_register_doctor).pack()
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack()

    def handle_register_doctor(self):
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        speciality = self.speciality_entry.get()
        self.doctors.append(Doctor(first_name, surname, speciality))
        tk.Label(self.root, text="Doctor Registered!").grid(row=5, column=1)
    def view_doctors(self):
        self.clear_frame()
        tk.Label(self.root, text="Doctors List").pack()
        for doc in self.doctors:
            tk.Label(self.root, text=str(doc)).pack()
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack()

    def update_doctor(self):
        self.clear_frame()
        tk.Label(self.root, text="Update Doctor Details").pack()
        self.view_doctors()
        tk.Label(self.root, text="Enter Doctor ID").pack()
        self.update_doc_id_entry = tk.Entry(self.root)
        self.update_doc_id_entry.pack()
        tk.Button(self.root, text="Update", command=self.handle_update_doctor).pack()
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack()

    def handle_update_doctor(self):
        doc_id = int(self.update_doc_id_entry.get()) - 1
        if 0 <= doc_id < len(self.doctors):
            tk.Label(self.root, text="1 - First Name").pack()
            tk.Label(self.root, text="2 - Surname").pack()
            tk.Label(self.root, text="3 - Speciality").pack()
            self.field_entry = tk.Entry(self.root)
            self.field_entry.pack()
            self.new_value_entry = tk.Entry(self.root)
            self.new_value_entry.pack()
            tk.Button(self.root, text="Submit", command=lambda: self.submit_update(doc_id)).pack()
        else:
            messagebox.showerror("Error", "Invalid doctor ID")

    def submit_update(self, doc_id):
        field = int(self.field_entry.get())
        new_value = self.new_value_entry.get()
        if field == 1:
            self.doctors[doc_id].set_first_name(new_value)
        elif field == 2:
            self.doctors[doc_id].set_surname(new_value)
        elif field == 3:
            self.doctors[doc_id].set_speciality(new_value)
        messagebox.showinfo("Success", "Doctor details updated")
        self.manage_doctors()

    def delete_doctor(self):
        self.clear_frame()
        tk.Label(self.root, text="Delete Doctor").pack()
        self.view_doctors()
        tk.Label(self.root, text="Enter Doctor ID").pack()
        self.del_doc_id_entry = tk.Entry(self.root)
        self.del_doc_id_entry.pack()
        tk.Button(self.root, text="Delete", command=self.handle_delete_doctor).pack()
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack()

    def handle_delete_doctor(self):
        doc_id = int(self.del_doc_id_entry.get()) - 1
        if 0 <= doc_id < len(self.doctors):
            self.doctors.pop(doc_id)
            messagebox.showinfo("Success", "Doctor deleted")
            self.manage_doctors()
        else:
            messagebox.showerror("Error", "Invalid doctor ID")

    def view_patients(self):
        self.clear_frame()
        tk.Label(self.root, text="Patients List").pack()
        for patient in self.patients:
            tk.Label(self.root, text=str(patient)).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack()

    def discharge_patient(self):
        self.clear_frame()
        tk.Label(self.root, text="Discharge Patient").pack()
        self.view_patients()
        tk.Label(self.root, text="Enter Patient ID").pack()
        self.discharge_patient_id_entry = tk.Entry(self.root)
        self.discharge_patient_id_entry.pack()
        tk.Button(self.root, text="Discharge", command=self.handle_discharge_patient).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack()

    def handle_discharge_patient(self):
        patient_id = int(self.discharge_patient_id_entry.get()) - 1
        if 0 <= patient_id < len(self.patients):
            self.discharged_patients.append(self.patients.pop(patient_id))
            messagebox.showinfo("Success", "Patient discharged")
        else:
            messagebox.showerror("Error", "Invalid patient ID")
        self.create_main_menu()

    def view_discharged_patients(self):
        self.clear_frame()
        tk.Label(self.root, text="Discharged Patients List").pack()
        for patient in self.discharged_patients:
            tk.Label(self.root, text=str(patient)).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack()

    def assign_doctor_to_patient(self):
        self.clear_frame()
        tk.Label(self.root, text="Assign Doctor to Patient").pack()
        self.view_patients()
        tk.Label(self.root, text="Enter Patient ID").pack()
        self.assign_patient_id_entry = tk.Entry(self.root)
        self.assign_patient_id_entry.pack()
        self.view_doctors()
        tk.Label(self.root, text="Enter Doctor ID").pack()
        self.assign_doctor_id_entry = tk.Entry(self.root)
        self.assign_doctor_id_entry.pack()
        tk.Button(self.root, text="Assign", command=self.handle_assign_doctor_to_patient).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack()

    def handle_assign_doctor_to_patient(self):
        patient_id = int(self.assign_patient_id_entry.get()) - 1
        doctor_id = int(self.assign_doctor_id_entry.get()) - 1
        if 0 <= patient_id < len(self.patients) and 0 <= doctor_id < len(self.doctors):
            self.patients[patient_id].link(self.doctors[doctor_id].full_name())
            self.doctors[doctor_id].add_patient(self.patients[patient_id])
            messagebox.showinfo("Success", "Doctor assigned to patient")
        else:
            messagebox.showerror("Error", "Invalid ID")
        self.create_main_menu()

    def update_admin_details(self):
        self.clear_frame()
        tk.Label(self.root, text="Update Admin Details").pack()
        tk.Label(self.root, text="1 - Username").pack()
        tk.Label(self.root, text="2 - Password").pack()
        tk.Label(self.root, text="3 - Address").pack()
        self.update_field_entry = tk.Entry(self.root)
        self.update_field_entry.pack()
        self.new_value_entry = tk.Entry(self.root)
        self.new_value_entry.pack()
        tk.Button(self.root, text="Submit", command=self.handle_update_admin_details).pack()
        tk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu).pack()

    def handle_update_admin_details(self):
        field = int(self.update_field_entry.get())
        new_value = self.new_value_entry.get()
        if field == 1:
            self.admin.__username = new_value
        elif field == 2:
            self.admin.__password = new_value
        elif field == 3:
            self.admin.__address = new_value
        messagebox.showinfo("Success", "Admin details updated")
        self.create_main_menu()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
