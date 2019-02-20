# convert string to uppercase
x = "please work."
print(x.upper())
print("break")

# capitalize a string
print(x.capitalize())

print("break")

# print string out backwords
#  creates a slice, same as [11:0:-1],whichs means begins at the last position and 
# moves backwords printing each letter.
backwords = x[::-1]
print(backwords)

print("break, next leetspeek")
# ask user to enter a phrase to translate.
text = input("please enter a phrase")
# add variables for the letters that will be converted 
letters_convert = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
# add variable of what the letters in letters_convert will be changed into.
numbers = [4, 3, 6, 1, 0, 5, 7]
# add empty string that resuot will be printed into.
translation = ""
# need all letters in the inputed string to be the same case.
# since letters_convert is given in uppercase use .upper() to do this.
uppercase_text = text.upper()
# add variable to use in first while loop.
i = 0
# use while loop to loop through the inputed phrase until it reaches the end.
while i < len(uppercase_text):
    # use variable (letter in this case) to grab each letter from the input phrase.
    letter = uppercase_text[i]
    # add to go through each letter
    i = i + 1
    # need variable (counter) to make loop go through the phrase and the end of while loop
    counter = 0
    # string that will be added to the final translation
    add_to_translation = ""
    # random variable to use is second while loop
    j = 0
    # second while loop 
    while j < len(letters_convert):
        letters_convert = letters_convert[j]
        # if the letter in the input is the same one of the letters that need translation.
        if letter == letters_convert:
            # if the letter from given input is to be translated
            # use number in same index in numbers string. need to convert number into string
            add_to_translation = str(numbers([counter])
            # need to add a break to stop loop otherwise it will overwrite with original letter.
# WHY IS BREAK STATEMENT INVALID SYNTAX?????
            break
        else:
            # if letter is not one in need of translation simple use original letter from input
            add_to_translation = letter
        # incriment counter to move to the next letter and restart the loop.
        counter = counter + 1
        # add translated letters(now numbers) to letters that are not translated
    translation = translation + add_to_translation
    # print result
print(translation)