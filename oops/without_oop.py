# Cricket Player -> K V dict

def add_scores(*scores, player):
    scores_list = player["scores"]
    scores_list.extend(scores)

def calculate_total_and_avg_scores(player):
    scores_list = player["scores"]
    total_scores = sum(scores_list)
    average_scores = total_scores / len(scores_list)    
    return total_scores,average_scores

def calculate_age(birth_year):
    return 2025-birth_year


virat = {
    "first_name":"Virat",
    "last_name":"Kohli",
    "birth_year":1987,
    "gender":"Male",
    "scores":[],
    "team":"India"
}

# virat["scores"]

print("-----------------------------------------------")
print(f"~~~~Without scores {virat['first_name']} Is~~~~")
print(virat)
add_scores(100,120,50,player=virat)

print()
print("-----------------------------------------------")
print(f"~~~~After Adding {virat['first_name']} Scores~~~~")
print(virat)

virat_total_score, virat_avg_score = calculate_total_and_avg_scores(virat)

print(f"Total Scores = {virat_total_score}\nAverage Scores = {virat_avg_score}")
print(f"Age = {calculate_age(virat['birth_year'])}")


# add scores in virat

steeve = {
    "first_name":"Steeve",
    "last_name":"Smith",
    "birth_year":1985,
    "gender":"Male",
    "scores":[],
    "team":"Australia"
}

print()
print("-----------------------------------------------")
print(f"~~~~Without scores {steeve['first_name']} Is~~~~")
print(steeve)
add_scores(80,50,90,100,player=steeve)

print()
print("-----------------------------------------------")
print(f"~~~~After Adding {steeve['first_name']} Scores~~~~")
print(steeve)
steeve_total_score, steeve_avg_score = calculate_total_and_avg_scores(steeve)
print(f"Total Scores = {steeve_total_score}\nAverage Scores = {steeve_avg_score}")
print(f"Age = {calculate_age(steeve['birth_year'])}")