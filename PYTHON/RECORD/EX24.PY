n=int(input("Enter the limit : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j," ",end="")
    print()

# Step 1: Start
# Step 2: Read the limit (n) from the user
# Step 3: Loop through numbers from 1 to n (outer loop)
# Step 4: For each number i, loop through numbers from 1 to i (inner loop)
# Step 5: Print the product of i and j, followed by a space
# Step 6: After each inner loop, print a new line to move to the next row
# Step 7: Stop
