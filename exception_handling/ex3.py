class User:

    def __init__(self, name, age):
        if age < 18:
            raise InvalidAgeError("You are below 18 you cannot access")

        print("User created successfully")
        self.name = name
        self.age = age
    
    def __str__(self):
        
        return f"User Info\nName = {self.name}\nAge = {self.age}"
        

class InvalidAgeError(Exception):

    def __init__(self, *args):
        super().__init__(*args)

try:
    user1 = User("Demo",10)
except Exception as e:
    print("Exception -> ",e)
else:
    print(user1)
finally:
    print("Closing Connection / File")

    
try:
    user2 = User("Demo 1",18)
except Exception as e:
    print(e)
else:
    print(user2)
finally:
    print("Closing Connection / File")