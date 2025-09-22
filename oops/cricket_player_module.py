class cricket_player:

    # Fields
    # constructor
    def __init__(self,first_name = None, last_name = None, gender = None, team = None):
        # COnstructor is used to create object
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.team = team 
        self.scores = [] # Empty scores
        

    # Methods
    # 1. Add scores

    def add_scores(self, *scores):
        self.scores.extend(scores)