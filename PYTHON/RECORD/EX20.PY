def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return(n*factorial(n-1))
n=int(input("Enter the value : "))
print(factorial(n))



# Step 1: Start
# Step 2: Define a function 'factorial' that takes an integer n as input
# Step 3: If n is 0 or 1, return 1 (base case for the recursion)
# Step 4: Otherwise, return n multiplied by the factorial of n-1 (recursive case)
# Step 5: Read the input value n from the user
# Step 6: Call the factorial function with n as argument and print the result
# Step 7: Stop
