# take an input form user
text = input("Enter your Text : \n")

# create variables
count = 0 # Number of Words
letter = 0 # Number of letters with spaces
words = [] # list has all words
repeat_word = [] # list has repeated words
letter_without_space = 0 # Number of letters without spaces
spaces = 0 # Number of Spaces

# number of letter in text
letter = len(text)


# number of spaces
for z in text:
    if z == " ":
        spaces = spaces + 1
# split the text by " " (space)
text_after_split = text.split(" ")


# looping over the text
for i in text_after_split:
    # count the number of words
    count = count + 1
    # count the repeated words and put them in the list (repeat_word)
    if i in words:
        repeat_word.append(i)
    # puting the word in the list (words)
    words.append(i)
    # count the number of letters without space
    for z in i:
        if z == " ":
            spaces += 1
        else:
            letter_without_space = letter_without_space + 1

# make the list (repeat_word) string
repeat_word_a = ",".join(repeat_word)


# result and show it
print("Your Article has : " + str(count) + " word")
print("Your Article has : " + str(letter) + " letter with space")
print("Your Article has : " + str(letter_without_space) + " letter without space")
print("Your Article has : " + str(spaces) + " spaces")
print("Your Article has : " + "[" + str(repeat_word_a) + "]" + " words are repeat")

