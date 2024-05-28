class Patient:
    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_doctor(self):
        return self.__doctor

    def link(self, doctor):
        self.__doctor = doctor

    def __str__(self):
        return f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}"
