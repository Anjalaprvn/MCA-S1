l=input("Enter a Sentence : ")
w=l.lower().split()
a={}
for i in w:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
for x,y in a.items():
    print(x,y)


# Step 1: Start
# Step 2: Ask the user to enter a sentence
# Step 3: Convert the sentence to lowercase and split it into words
# Step 4: Create an empty dictionary to store word counts
# Step 5: For each word in the list, check if it is already in the dictionary
# Step 6: If it is, increment its count; if not, add it to the dictionary with a count of 1
# Step 7: Print each word and its count from the dictionary
# Step 8: Stop
