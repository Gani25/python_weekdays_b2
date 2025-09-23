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