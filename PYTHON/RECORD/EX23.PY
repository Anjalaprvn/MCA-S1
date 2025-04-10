import math
p=[]
count=0
for i in range(1000,9999,2):
    a=math.sqrt(i)
    if a%1==0:
        for j in str(i):
            if int(j)%2==0:
                count+=1
        if count==4:
            p.append(i)
        count=0
print("The values :" ,p)


# Step 1: Start
# Step 2: Create an empty list p and set count to 0
# Step 3: Loop through numbers from 1000 to 9999, stepping by 2
# Step 4: For each number, calculate its square root
# Step 5: Check if the square root is an integer
# Step 6: Loop through each digit of the number and check if it is even
# Step 7: If all digits are even, add the number to the list p
# Step 8: Reset count to 0 after each number
# Step 9: Print the list p
# Step 10: Stop
