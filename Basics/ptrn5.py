# Butterfly patter

n = int(input("Enter a number: "))

# Upper half

for i in range(1,n+1):
    # Left star
    for j in range(1,i+1):
        print("*",end=" ")
    
    # Mid Space
    for sp in range(1,2*(n-i)):
        print(" ",end=" ")

    # Right star
    for j in range(1,i+1):
        if(j != n):
            print("*",end=" ")
    
    print()

# lower half

for i in range(n-1,0,-1):
    # Left star
    for j in range(1,i+1):
        print("*",end=" ")
    
    # Mid Space
    for sp in range(1,2*(n-i)):
        print(" ",end=" ")

    # Right star
    for j in range(1,i+1):
        if(j != n):
            print("*",end=" ")
    
    print()