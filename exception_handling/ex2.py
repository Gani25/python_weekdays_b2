while(True):
    try:
        n1 = int(input("Enter numerator: "))   

        break
    
    except Exception as e:
        print("Please enter number only and try again!!")
while(True):
    try:
        n2 = int(input("Enter denominator: "))   
        if(n2 == 0):
            raise ValueError("Denominator cannot be 0")
        
        break
    
    except Exception as e:
        print(e)
        print("Please try again")
    

print("Number 1 = ",n1)
print("Number 2 = ",n2)
print(f"Division of {n1}, {n2} = {n1/n2}")