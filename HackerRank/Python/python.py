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

    # Find the Runner-Up Score!
    arr = list(arr)
    x = max(arr)
    y = -999999
    
    for i in range(0,n):
        if(arr[i]<x and arr[i]>y):
            y = arr[i]
            
    print(y)

# Nested Lists
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    x = 999999
    for i in range(len(students)):
        if(x>float(students[i][1])):
            x = float(students[i][1])
            
    y = 999999
    for i in range(len(students)):
        if float(students[i][1])>float(x) and y >float(students[i][1]):
            y = float(students[i][1])
            
    runner = []
    for i in range(len(students)):
        if(float(students[i][1]) == float(y)):
            runner.append(students[i][0])
            
    runner = sorted(runner)
            
    for i in range(len(runner)):
        print(runner[i])


