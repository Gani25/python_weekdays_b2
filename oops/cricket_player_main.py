import cricket_player_module as cricket_module

virat = cricket_module.cricket_player("Virat","Kohli","Male",1987,"India")

print("Circket Player Info")
print(f"First Name = {virat.first_name}")
print(f"Last Name = {virat.last_name}")
print(f"Gender = {virat.gender}")
print(f"Team = {virat.team}")
print(f"Birth Year = {virat.birth_year}")
# Display age
print(f"Age = {virat.calculate_age()}")

virat.add_scores(100,50)

virat.add_scores(60)
print(f"Scores = {virat.scores}")
sum_avg = virat.sum_and_avg()
print(f"Total Scores = {sum_avg[0]}")
print(f"Average Scores = {sum_avg[1]}")


steeve = cricket_module.cricket_player("Steeve","Smith","Male",1985,"India")
print("Circket Player Info")
print(f"First Name = {steeve.first_name}")
print(f"Last Name = {steeve.last_name}")
print(f"Gender = {steeve.gender}")
print(f"Team = {steeve.team}")
print(f"Birth Year = {steeve.birth_year}")
print(f"Age = {steeve.calculate_age()}")
# Display age

steeve.add_scores(60,80,150,10)
print(f"Scores = {steeve.scores}")

sum_avg = steeve.sum_and_avg()
print(f"Total Scores = {sum_avg[0]}")
print(f"Average Scores = {sum_avg[1]}")
