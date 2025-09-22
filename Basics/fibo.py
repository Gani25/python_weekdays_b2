'''
# Fibonacci series till n
# n = 10
# start = 3, n+1
# 0 1 1 2 3 5 8 13 21 34
'''

n = int(input("Enter a number: "))

n1 = 0
n2 = 1

print(f"{n1} {n2} ",end="")
for i in range(3,n+1):
    n3 = n1+n2
    print(f"{n3} ",end="")
    n1 = n2
    n2 = n3 