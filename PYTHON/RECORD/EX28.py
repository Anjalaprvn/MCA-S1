a=int(input("Enter the number you want "))
b=1
temp=a
for i in range(1):
    for i in range(1,a+temp):
        if i<=a:
            print(i*"*")
        else:
            print((temp-b)*"*")
            b+=1
    
# Step 1: Start
# Step 2: Read the number (a) from the user
# Step 3: Initialize b to 1 and set temp equal to a
# Step 4: Iterate over a range (1) (this outer loop runs only once)
# Step 5: Iterate over a range from 1 to (a + temp)
# Step 6: If the current index (i) is less than or equal to a, print i stars
# Step 7: Otherwise, print stars based on (temp - b) and increment b
# Step 8: Stop
