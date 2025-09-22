# Recurssion -> A function calling itself within a function is called as recurssion
# We need to specify end condition or else function call stack will be full

# WAP to print factorial of n using recurssion

def calc_fact(num:int):
    if(num == 1 or num == 0):
        return 1


    return num * calc_fact(num-1)


n = int(input("Enter a number: "))

if(n <0):
    print("TO caluclate factorial number should be positive")
else:
    ans = calc_fact(n)

    print(f"The factorial of {n} is {ans}")

# WAP to print addition of first n natural number using recurssion

# Fibonacci series till n
# n = 10
# start = 3, n+1
# 0 1 1 2 3 5 8 13 21 34