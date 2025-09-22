n = int(input("Enter a number: "))

# ROWS

for i in range(1,n+1):

    # SPACE
    for sp in range (1,n-i+1):
        print(" ",end=" ")
    
    # STAR
    for j in range(1, 2*i):
        print("*",end=" ")
    
    # new line
    print()