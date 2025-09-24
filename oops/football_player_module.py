import datetime as dt
class football_player:

    # Fields
    # constructor
    def __init__(self,first_name = None, last_name = None, gender = None, birth_year = None, team = None):
        # COnstructor is used to create object
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.team = team 
        self.birth_year = birth_year
        self.goals = [] # Empty goals
        

    # Methods
    # 1. Add Goals

    def add_goals(self, *goals):
        self.goals.extend(goals)

    def sum_and_avg(self):
        goals_sum = sum(self.goals)
        avg_goals = goals_sum / len(self.goals)

        return goals_sum,avg_goals
    
    # Age
    def calculate_age(self):
        current_year = dt.datetime.now().year
        return current_year - self.birth_year
    
    def __str__(self):
        sum_and_average = self.sum_and_avg()
        return f"""
        FootBall Player Info
        First Name = {self.first_name}
        Last Name = {self.last_name}
        Gender = {self.gender}
        Team = {self.team}
        Birth Year = {self.birth_year}
        Age = {self.calculate_age()}
        Goals = {self.goals}
        Total Goals = {sum_and_average[0]}
        Average Goals = {round(sum_and_average[1],2)}
"""