word=input("Enter a sentence : ").split()
temp=len(word[0])
w=word[0]
for i in word:
    if temp<len(i):
        temp=len(i)
        w=i
print("The Longest word :",w,"has :",temp," characters")

# Step 1: Start
# Step 2: Read a sentence from the user and split it into a list of words
# Step 3: Initialize temp with the length of the first word and set w to the first word
# Step 4: Iterate through each word in the list
# Step 5: If the length of the current word is greater than temp, update temp and w with the current word's length and the word
# Step 6: Print the longest word and its length
# Step 7: Stop
