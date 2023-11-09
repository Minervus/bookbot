with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
text_string = file_contents

# Word counter function
def count_words(words):
    counter = 0

    for word in words:
        counter += 1
        
    return counter

# Letter counter function
def letter_counter(text_string):
    text = text_string.lower()
    letter_dictionary = {}

    for letter in text:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 0
    
    return letter_dictionary


num_words = count_words(words)
letter_count_dict = letter_counter(text_string)

# Convert dictionary into a list
letter_list = []
for key, value in letter_count_dict.items():
    temp = [key,value]
    letter_list.append(temp)

# Initialize empty array to populate with alpha characters
sorted_letter_list = []

for i in range(0,len(letter_list)):
    if letter_list[i][0].isalpha():
        sorted_letter_list.append(letter_list[i])

# Sorting the list alphabetically (doesn't return a value, sorts in place)
sorted_letter_list.sort()

# Printing the final report
print(f"--- Begin report of {f.name} ---")
print(f"{num_words} words found in the document")
print()

for i in range(0,len(sorted_letter_list)):
    print(f"The '{sorted_letter_list[i][0]}' character was found {sorted_letter_list[i][1]} times")

print("--- End report ---")