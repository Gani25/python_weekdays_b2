try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))

    result = n1 /n2 

    print(f"Division of {n1}, {n2} = {result}")
except Exception as e:
    print(e)
except ZeroDivisionError as ze:
    print("Inside Zero Div Error ->",ze)
# except ValueError as ve:
#     print(ve)
print("Hello")