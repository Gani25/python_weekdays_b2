
import player_module as pm
# from player_module import *

# class derived_class(base_class)
class cricket_player(pm.player):

    # Fields
    # constructor
    def __init__(self,first_name = None, last_name = None, gender = None, birth_year = None, team = None):
        # COnstructor is used to create object
        super().__init__(first_name,last_name,gender,birth_year,team)
        
        self.scores = [] # Empty scores
        

    # Methods
    # 1. Add scores

    def add_scores(self, *scores):
        self.scores.extend(scores)

    def sum_and_avg(self):
        scores_sum = sum(self.scores)
        avg_scores = scores_sum / len(self.scores)

        return scores_sum,avg_scores
    
   
    def __str__(self):
        sum_and_average = self.sum_and_avg()
        return f"""
        {super().__str__()}
        Circket Player Info
        Scores = {self.scores}
        Total Scores = {sum_and_average[0]}
        Average Scores = {sum_and_average[1]}
"""