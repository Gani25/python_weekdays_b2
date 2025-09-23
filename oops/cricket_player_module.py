import datetime as dt
class cricket_player:

    # Fields
    # constructor
    def __init__(self,first_name = None, last_name = None, gender = None, birth_year = None, team = None):
        # COnstructor is used to create object
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.team = team 
        self.birth_year = birth_year
        self.scores = [] # Empty scores
        

    # Methods
    # 1. Add scores

    def add_scores(self, *scores):
        self.scores.extend(scores)

    def sum_and_avg(self):
        scores_sum = sum(self.scores)
        avg_scores = scores_sum / len(self.scores)

        return scores_sum,avg_scores
    
    # Age
    def calculate_age(self):
        current_year = dt.datetime.now().year
        return current_year - self.birth_year
    
    # def __str__(self):
    #     sum_and_average = self.sum_and_avg()
    #     return f"\nCircket Player Info\nFirst Name = {self.first_name}\nLast Name = {self.last_name}\nGender = {self.gender}\nTeam = {self.team}\nBirth Year = {self.birth_year}\nAge = {self.calculate_age()}\nScores = {self.scores}\nTotal Scores = {sum_and_average[0]}\nAverage Scores = {sum_and_average[1]}"

    def __str__(self):
        sum_and_average = self.sum_and_avg()
        return f"""
        Circket Player Info
        First Name = {self.first_name}
        Last Name = {self.last_name}
        Gender = {self.gender}
        Team = {self.team}
        Birth Year = {self.birth_year}
        Age = {self.calculate_age()}
        Scores = {self.scores}
        Total Scores = {sum_and_average[0]}
        Average Scores = {sum_and_average[1]}
"""