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
   def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leap=True
                return leap
            leap=False
            return leap
        leap=True
        return leap    
    return leap



# Print Function
for i in range(1, n+1):
    print(i, end='')


# List Comprehensions
answer = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i + j + k) != n)]
print(answer)

