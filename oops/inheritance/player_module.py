import datetime as dt
class player:

    # Fields
    # constructor
    def __init__(self,first_name = None, last_name = None, gender = None, birth_year = None, team = None):
        # COnstructor is used to create object
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.team = team 
        self.birth_year = birth_year
    
    # Age
    def calculate_age(self):
        current_year = dt.datetime.now().year
        return current_year - self.birth_year
    
    def __str__(self):
        
        return f"""
        Player Info
        First Name = {self.first_name}
        Last Name = {self.last_name}
        Gender = {self.gender}
        Team = {self.team}
        Birth Year = {self.birth_year}
        Age = {self.calculate_age()}
"""
    
def check_name():
    print("Name of __name__ -> ",__name__)

if(__name__ == "__main__"):
    check_name()