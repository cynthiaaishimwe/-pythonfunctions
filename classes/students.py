class Student:
    name = "Emily"
    age = 21
    school = "Akirachix"
    nationality = "Kenyan"
    first_name = "Jane"
    last_name = "chege"
    age = 20
    country = "Congo"
    

class Student:
    school = "Akirachix"
      
    def  __init__(self,name,age,nationality,first_name,last_name,country,):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
       

    def greet_student(self):
        return f"hello {self.name}welcome to{self.school}proudly{self.nationality}"
    
    def  show_full_name(self):
        return f"I am {self.first_name} {self.last_name}"
    
    def year_of_birth(self):
       return f"{self.age}"
    

    def show_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    




#  Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials


# Create 3 files in the classes directory car.py, fruit.py, and bank.py.
# Define the following classes in each module respectively. 

