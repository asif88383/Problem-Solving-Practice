# Python If-Else
if n % 2 != 0:
    print("Weird")
else:
    if(n>2 and n<=5):
        print("Not Weird")
    if(n>6 and n<=20):
        print("Weird")
    if(n>20):
        print("Not Weird")


# Python Loops
i = 0
while(i<n):
    print(i**2)
    i=i+1

# Write a Function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4 == 0):
        leap=True
    
    return leap

