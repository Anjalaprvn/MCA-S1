import math
import random
import datetime

random_number = random.randint(1, 10)
pi_value = math.pi
sqrt_value = math.sqrt(121)

current_day = datetime.datetime.now().strftime("%A")

print(f"Random Number: {random_number}")
print(f"Value of Pi: {pi_value}")
print(f"Square Root of 121: {sqrt_value}")
print(f"Current Day: {current_day}")



# Step 1:Start
# Step 2: Import the 'math', 'random', and 'datetime' libraries
# Step 3: Generate a random number between 1 and 10 using 'random.randint'
# Step 4: Get the value of Pi using 'math.pi'
# Step 5: Calculate the square root of 121 using 'math.sqrt'
# Step 6: Get the current day of the week using 'datetime.datetime.now().strftime("%A")'
# Step 7: Print the results
# Step 8:Stop
