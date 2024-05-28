class Admin:
    def __init__(self, username, password, address=''):
        self.__username = username
        self.__password = password
        self.__address = address

    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f'{index + 1:3}|{item}')

    def login(self, username, password):
        if username == self.__username and password == self.__password:
            return True
        else:
            return False

    def find_index(self, index, doctors):
        return 0 <= index < len(doctors)

    def get_doctor_details(self):
        first_name = input("Enter doctor's first name: ")
        surname = input("Enter doctor's surname: ")
        speciality = input("Enter doctor's speciality: ")
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        print("-----Doctor Management-----")
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        op = input('Choose the operation: ')
        
        if op == '1':
            print("-----Register-----")
            first_name, surname, speciality = self.get_doctor_details()
            if any(doc.get_first_name() == first_name and doc.get_surname() == surname for doc in doctors):
                print('Doctor already exists.')
            else:
                doctors.append(Doctor(first_name, surname, speciality))
                print('Doctor registered.')

        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        elif op == '3':
            print("-----Update Doctor's Details-----")
            self.view(doctors)
            index = int(input('Enter the ID of the doctor: ')) - 1
            if self.find_index(index, doctors):
                print(' 1 - First name')
                print(' 2 - Surname')
                print(' 3 - Speciality')
                field = int(input('Choose the field to update: '))
                if field == 1:
                    doctors[index].set_first_name(input('Enter new first name: '))
                elif field == 2:
                    doctors[index].set_surname(input('Enter new surname: '))
                elif field == 3:
                    doctors[index].set_speciality(input('Enter new speciality: '))
                print('Doctor details updated.')

        elif op == '4':
            print("-----Delete Doctor-----")
            self.view(doctors)
            index = int(input('Enter the ID of the doctor: ')) - 1
            if self.find_index(index, doctors):
                doctors.pop(index)
                print('Doctor deleted.')

    def view_patient(self, patients):
        print("-----View Patients-----")
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        print("-----Assign Doctor to Patient-----")
        self.view(patients)
        patient_index = int(input('Enter patient ID: ')) - 1
        if 0 <= patient_index < len(patients):
            self.view(doctors)
            doctor_index = int(input('Enter doctor ID: ')) - 1
            if self.find_index(doctor_index, doctors):
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('Doctor assigned to patient.')

    def discharge(self, patients, discharge_patients):
        print("-----Discharge Patient-----")
        self.view(patients)
        patient_index = int(input('Enter patient ID: ')) - 1
        if 0 <= patient_index < len(patients):
            discharge_patients.append(patients.pop(patient_index))
            print('Patient discharged.')

    def view_discharge(self, discharged_patients):
        print("-----Discharged Patients-----")
        self.view(discharged_patients)

    def update_details(self):
        print(' 1 - Username')
        print(' 2 - Password')
        print(' 3 - Address')
        field = int(input('Choose the field to update: '))
        if field == 1:
            self.__username = input('Enter new username: ')
        elif field == 2:
            password = input('Enter new password: ')
            if password == input('Re-enter new password: '):
                self.__password = password
        elif field == 3:
            self.__address = input('Enter new address: ')
