# Call stack

# Without return without parameter
def addition():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))

    sum = n1 + n2

    print(f"The addition of {n1}, {n2} = {sum}")
    calc_power(n1,n2)

# without return with param
def calc_power(n1:int,n2:int):
    power = n1 ** n2
    print(f"{n1} raise to {n2} = {power}")


if(__name__ == "__main__"):
    addition()
    
    print("Hello")