# import string module
import string

# take an input form user
text = input("Enter your Text : \n")


# create lists

words = [] # list has all words
repeat_word = [] # list has repeated words


# Function count letters with all (punctuation marks, spaces)
def count_string(text):
    # count the length of all text
    letter = len(text)
    return str(letter) + " letters"


# Function count words
def count_words(text):
    # count the words 
    count_words_var = 0 # Number of Words
    var = "" # variable has a word after join
    word = [] # List has individual characters 
    words = [] # List has words
    
    # looping over string 
    for i in text: 
        # check if i is letter (capital or small)
        if i in string.ascii_letters: 
            # Add letter in word
            word.append(i) 
        else:
            try: 
                # check if there is a letter in list word and check the latest
                if word[-1] in string.ascii_letters:
                    var = "".join(word) # Join individual characters to be one word
                    words.append(var) # Then, add it to list words
                    word.clear() # Then, Delete all characters and start a new
            except:
                pass
    
    # Sometimes, there a word in list word and don't make join for it
    try:
        if word[-1] in string.ascii_letters:
            var = "".join(word)
            words.append(var)
            word.clear()
    except:
        pass

    # The length of words
    count_words_var = len(words) + 1

    list_word = []
    repeated_word = []

    # looping over list (list word)
    for x in words:
        if x in list_word: # check if it is in list word
            if x in repeated_word: # check if it is in list repeated word, Don't repeat words 
                continue
            else: # If it is not in repeated list, Add word to it
                repeated_word.append(x)
        else: # finally, Add word in list word
            list_word.append(x)

    # Join list to show as words instead of list
    repeated_word_var = ",".join(repeated_word)

    # In the End, Show Result !
    return str(count_words_var) + " words , " + " [ " + str(repeated_word_var) + " ] " + " was repeated"


# Function count other things (spaces, punctuation marks)
def count_others(text):
    # count number of spaces, punctuation marks and letter
    count_letter_only = 0 # Number of letter without any thing
    count_spaces = 0 # number of spaces
    count_punctuation_marks = 0 # number of punctuation marks 
   
    for i in text:
        # check if i is letter 
        if i in string.ascii_letters:
            count_letter_only += 1
        # Check if i is punctuation mark
        elif i in string.punctuation:
            count_punctuation_marks += 1
        # Check if i is space
        elif i in " ":
            count_spaces += 1
    
    # Return Result
    return str(count_letter_only) + " letter only , " + str(count_spaces) + " spaces , " + str(count_punctuation_marks) + " punctuation mark "






# results and show it
print("Your Article has : ")
print(count_string(text))

print("Your Article has : ")
print(count_words(text))

print("Your Article has : ")
print(count_others(text))
