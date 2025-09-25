# Lambda -> Filter (Condition)

names = ["ABDUL","DN","PR","MEMON","PQ","SACHIN","VIRAT"]

# Get all names which have lenght greater than 2
print(names)

names_filter = filter(lambda name: len(name) > 2,names)

print(names_filter)
print(list(names_filter))

