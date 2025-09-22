import cricket_player_module as cricket_module

virat = cricket_module.cricket_player("Virat","Kohli","Male","India")

print("Circket Player Info")
print(f"First Name = {virat.first_name}")
print(f"Last Name = {virat.last_name}")
print(f"Gender = {virat.gender}")
print(f"Team = {virat.team}")
print(f"Scores = {virat.scores}")

virat.add_scores(100,50)
print(f"Scores = {virat.scores}")

virat.add_scores(60)
print(f"Scores = {virat.scores}")
# method -> class for sum and average
# Steeve -> birth year - > age
