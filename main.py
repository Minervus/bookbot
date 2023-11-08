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


#count_words(words)
#letter_counter(text_string)

num_words = count_words(words)
letter_count_dict = letter_counter(text_string)

# Convert dictionary into a list
letter_list = []
for key, value in letter_count_dict.items():
    temp = [key,value]
    letter_list.append(temp)

sorted_letter_list = letter_list.sort()


print(sorted_letter_list)
print(f"--- Begin report of {f.name} ---")
print(f"{num_words} words found in the document")