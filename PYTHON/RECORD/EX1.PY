x=int(input("Enter to which year you want : "))
for i in range(2024,x):
    if(i%400==0 or (i%4==0 and i%100!=0)):
        print(i," is a leap year")
else:
    print("\n over")




# Step 1: Read the value of x (the year limit) from the user
# Step 2: Loop through all years from 2024 to x-1
# Step 3: If a year is divisible by 400 or divisible by 4 and not divisible by 100, it is a leap year
# Step 4: Print the year if it's a leap year
# Step 5: After the loop finishes, print "over"
