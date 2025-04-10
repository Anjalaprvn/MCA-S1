#postive number 

list=[1,-2,4,-7,-8,9]
positive=[i for i in list[:] if(i>0)]
print(positive)

#square


square=[i**2 for i in list[:]]
print(square)

#vowels

x=input("Enter a word : ")
v=['A','a','E','e','I','i','O','o','U','u']
y=[i for i in x[:] if i in v]
print(y)


#ordinal value

word="hello"
ordinal_values=[ord(i) for i in word]
print(ordinal_values)



# Step 1: Start

# Positive Numbers
# Step 2: Create a list with both positive and negative numbers
# Step 3: Use list comprehension to create a new list with only the positive numbers
# Step 4: Print the list of positive numbers

# Square of Numbers
# Step 5: Use list comprehension to create a new list containing the square of each number in the list
# Step 6: Print the list of squared numbers

# Vowels in a Word
# Step 7: Read a word from the user
# Step 8: Create a list of vowels
# Step 9: Use list comprehension to create a list of characters from the word that are vowels
# Step 10: Print the list of vowels found in the word

# Ordinal Values of Characters
# Step 11: Create a word string
# Step 12: Use list comprehension to get the ordinal value of each character in the word
# Step 13: Print the list of ordinal values

# Step 14: Stop



