# Classes - type of obj

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print("WOOF!")

# dog1 = Dog("Murphy", "Mutt")
# dog2 = Dog("Kudjo", "Lab" )

# print(f"{dog1.name.upper()} is a {dog1.breed}")
# print(f"{dog2.name} is a {dog2.breed}")


# print(f"{dog1.bark()}")


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary 

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary
    
    def change_salary(self, new_salary):
        self.salary = new_salary
        return f"I have updated the salary to {self.salary}"

employee1 = Employee("Alice", "Mgr", 50000)
employee2 = Employee("Jo", "Stkr", 10000)



# Old way of doing it print(" {} {} {} ".format(employee2.get_name(), employee2.get_position(), employee2.get_salary()))
# print(f"{employee2.get_salary()}")

# employee2.change_salary(18000)

# print(f"{employee2.get_salary()}")






























