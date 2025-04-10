l1=[]
l2=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    x=int(input("Enter the value"))
    l1.append(x)
    if x>100:
        l2.append('over')
    else:
        l2.append(x)
print(l1)
print(l2)


# Step 1: Start

# Step 2: Create two empty lists, l1 and l2
# Step 3: Ask the user how many numbers they want to enter
# Step 4: For each number:
# Step 5: Ask the user to enter a number and add it to list l1
# Step 6: If the number is greater than 100, add 'over' to list l2, otherwise add the number to list l2
# Step 7: Print both lists l1 and l2

# Step 8: End
