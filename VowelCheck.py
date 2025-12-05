#Instructions and Hints for the Vowel Counter Program

#1. Create a function that will count vowels in a piece of text
#Hint: Use def to define your function and give it a name, like count_vowels.

def count_vowels(Count):


#2. Inside the function, create a list of characters that are considered vowels
#Hint: Include both lowercase and uppercase vowels so the program counts all of them (a, e, i, o, u, A, E, I, O, U).
    Vowel_List = ["a","e", "i", "o", "u", "A", "E", "I", "O", "U"]
#3. Make a counter that starts at 0
#Hint: This counter will increase each time the program finds a vowel.
    counter = 0
#4. Loop through the text one character at a time
#Hint: Use a for loop to check each letter in the user’s input.
    for letter in Count:
#5. Check whether the current character is a vowel
#Hint: Use an if statement and the keyword in to see if the character is inside the vowel list.
        if letter in Vowel_List:
#6. If the character is a vowel, increase the counter
#Hint: Add 1 to your counter each time a vowel is found.
            counter += 1
#7. After the loop ends, return the final number of vowels counted
#Hint: The return statement sends the final count back to the main program.
    return counter
#8. Ask the user to type in a word or sentence
#Hint: Use input() to collect text from the user.
n = input("Type something, I don't really care: ")
#9. Call your function and pass the user’s text into it
#Hint: Place the user’s input inside the parentheses when calling the function.
print(f"there are {count_vowels(n)} in your text")
#10. Print the result inside a clear sentence
#Hint: Use an f-string to neatly show the number of vowels to the user.
