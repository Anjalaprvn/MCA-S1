d = {'a': 3, 'b': 1, 'c': 2}
sorted_asc = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Sorted in Ascending Order:", sorted_asc)
print("Sorted in Descending Order:", sorted_desc)


# Step 1: Start
# Step 2: Create a dictionary with key-value pairs
# Step 3: Sort the dictionary in ascending order by values
# Step 4: Sort the dictionary in descending order by values
# Step 5: Print both sorted dictionaries
# Step 6: End
