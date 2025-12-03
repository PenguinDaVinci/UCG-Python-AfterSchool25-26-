SecretNumber = 7


tries = 0


while tries != SecretNumber:
    if tries < SecretNumber:
        print("Too low try again")
    else: tries > SecretNumber
    print("Too high try again")
    

   
    
while tries > SecretNumber and tries < 3:
    tries = input("Too high, try again")
   



if tries == SecretNumber:
    print("Dangit, I guess you win")

 