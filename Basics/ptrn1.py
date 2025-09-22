# 01 pattern
n = int(input("Enter a number: "))

# ROWS
for i in range(1,n+1):
    # COLUMNS
    for j in range(1,i+1):
        if((i+j)%2 == 0):
            print("0", end=" ")
        else:
            print("1", end=" ")
    
    # end of column loop
    # new line
    print()