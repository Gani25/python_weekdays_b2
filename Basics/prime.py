# WAP to check whether the number is a prime number or not
# Divisible by 1 and divisible by itself

def check_prime(number:int):
    # Any value of number we are assuming as prime
    isPrime = True
    if (number <=1):
        isPrime = False
        return isPrime
    
    for i in range(2,number):
        # CHeck if number is divisible by i
        if(number % i == 0):
            # Not Prime
            isPrime = False
            return isPrime
        
    return isPrime


n = int(input("Enter a number to check it is prime or not: "))

prime = check_prime(number=n)
if(prime):
    print(f"Number = {n} is a prime number")
else:
    print(f"Number = {n} is not a prime number")