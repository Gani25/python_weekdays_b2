import cricket_player_module as cricket_module

virat = cricket_module.cricket_player("Virat","Kohli","Male",1987,"India")
virat.add_scores(100,50)

virat.add_scores(60)


print("\n\nPrinting Object -> ",virat)


steeve = cricket_module.cricket_player("Steeve","Smith","Male",1985,"India")

steeve.add_scores(60,80,150,10)


print("\n\nPrinting Object -> ",steeve)
