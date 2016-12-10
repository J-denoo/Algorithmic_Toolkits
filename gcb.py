#! python 3
#This algorithm computes the gcb of two numbers
## This 
##   Option 1    gcb function
def gcb(a,b=0): 
    y=min(a,b)
    x=max(a,b)
       
    while(y):
       x, y = y, x % y 
    return(x)
    
    
########## Option 2 <== reading input from file
    
#! python 3
#This algorithm computes the gcb of two numbers
## This 
import sys
input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
#def gcb(): 
y=min(a,b)
x=max(a,b)

while(y):
    x, y = y, x % y 
print(x)

## execute with python3 gcb1.py < data.txt
## where data is in data.txt   