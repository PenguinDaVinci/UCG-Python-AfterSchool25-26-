# Countdown timer Program
#Program description: This program counts down from user-given number to 1.

#Importing time module to add a 1 second delay
import time

#Ask the user to enter a number to start counting down from
number = int(input("Enter a number to start the countdown:"))

#Kepp looping as long as the number is greater than 0
while number > 0:
    print(number) # Print the current number
    time.sleep(1) #Wait for 1 second before continuing
    number -= 1     #Subtract 1 from number each time

    # Once the loop ends print a message
print("💩 Time's up")