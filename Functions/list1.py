# Lambda examples

numbers = [1,2,3,4,5,6,7,8,9,10]


cube_list_map = map(lambda element:element ** 3,numbers)

# cube of each numbers and store in new list
# cubeList = []
cube_list = list()

# for element in numbers:
#     cubeList.append(element ** 3)

print(f"Numbers = {numbers}")
# print(f"Cubes of Numebrs = {cubeList}")

print(f"Cubes of Numebrs using Map = {cube_list_map}")
print(f"Cubes of Numebrs using Map = {list(cube_list_map)}")




