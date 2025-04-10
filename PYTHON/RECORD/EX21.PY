x=int(input("Enter the number of values you want to print : "))
a=-1
b=1
for i in range (0,x):
    c=a+b
    print (c)
    a=b
    b=c

# Step 1: Start
# Step 2: Ask the user to enter the number of values to print
# Step 3: Set two numbers a = -1 and b = 1
# Step 4: Repeat x times (based on user input)
# Step 5: Add a and b to get c
# Step 6: Print c
# Step 7: Set a to b and b to c for the next round
# Step 8: Stop
