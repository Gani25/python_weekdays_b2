# Single Statement Function -> one line
from typing import Callable
def addition(x:int,y:int):
 

    return x + y


add:Callable[[int,int],int] =  lambda x,y:x+y


print(addition(10.566,20))

print(add(50,2))