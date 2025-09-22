# WAP to print series of prime number from 1 to n
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


n = int(input("Enter a number so that I will display list of prime numebers: "))

# start = 2, stop = n+1

print(f"Prime numbers from 1 to {n} is = ")
for i in range(2,n+1):
    if(check_prime(i)):
        print(i,end=" ")