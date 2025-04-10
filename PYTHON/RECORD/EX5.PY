n=int(input("Enter the number of names: "))
x=[]
c=0
for i in range (n):
    y=input("Enter the name : ")
    x.append(y)
for i in x[:]:
    for j in i.lower():
        if 'a' in j:
            c=c+1
print(c)

# Step 1: Start
# Step 2: Get the number of names to enter
# Step 3: Collect names in a list
# Step 4: Count occurrences of 'a' in all names
# Step 5: Print the count of 'a'
# Step 6: End
