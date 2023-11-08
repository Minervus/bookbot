with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

def count_words(words):
    counter = 0

    for word in words:
        counter += 1
        
    print(counter)

count_words(words)