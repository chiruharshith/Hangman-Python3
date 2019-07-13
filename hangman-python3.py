#importing the time module
import time
#welcoming the user
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
print()
#waiting for a second
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
#playnow function to reuse second time
def playnow():
    wordset={"at","on","in","off","bat","hell", "pet","chemistry", "computer", "electricity", "geology", "energy", "element", "Internet", "light", "mathematics","measurement", "number",
             "physics", "shape"," space", "technology", "plant", "reptile", "rodent", "seed", "spider", "tree", "vegetable", "virus", "worm", "blood", "body", "face",
             "foot", "hair", "head", "health", "hygiene","injury", "muscle", "nerve", "air", "conservation", "continent", "desert", "earth", "ecosystem", "farming",
             "fishing", "forest, ""gardening", "geography", "hunting", "lake", "mountain", "organ", "reproduction", "respiration","communication","legislature", "sense",
             "skeleton", "tooth"}    
    #regestering length of the guessing word from user
    lengthofword = int(input("Choose The Length of the word you would like to guess = "))
    word=""
    count=1
    for char in wordset:
        if lengthofword == len(char):
            word = char
            if word != "":
                break
        else:
            count +=1
    if lengthofword != len(char):
        print("Choose length between 2-13")     
    #creates an variable with an empty value to store guess word
    guesses = ''
    #determine the number of turns
    turns = 10
    # Create a while loop    
    while turns > 0 and word!="":                 
        # make a counter that starts with zero
        failed = 0
        # for every character in secret_word    
        for char in word:      
        # see if the character is in the players guess
            if char in guesses:        
                # print then out the character
                print (char,end=" ")
            else:        
                # if not found, print a dash
                print ("_",end=" ")           
                # and increase the failed counter with one
                failed += 1
        # if failed is equal to zero
        # print You Won
        if failed == 0:
            #won function for understandability
            def won():
                print()
                print()
                for row in range(6):
                    for col in range(39):
                        if (row==0) and ( col==1 or col==2 or col==4 or col==5 or col==33 or col==34 or col==36 or col==37):
                            print("*",end="")
                        elif (row==1) and ( col==0 or col==3 or col==6 or col==13 or col==10 or col==16 or col==20 or col==25 or col==28 or col==21 or col==32 or col==35 or col==38):
                            print("*",end="")
                        elif (row==2) and ( col==0 or col==6 or col==10 or col==12 or col==14 or col==16 or col==19 or col==22 or col==25 or col==28 or col==26 or col==32 or col==38):
                            print("*",end="")
                        elif (row==3) and ( col==1 or col==5 or col==10 or col==11 or col==15 or col==16 or col==22 or col==19 or col==27 or col==25 or col==28 or col==33 or col==37):
                            print("*",end="")
                        elif (row==4) and ( col==2 or col==4 or col==10 or col==16 or col==21 or col==20 or col==25 or col==28 or col==34 or col==36):
                            print("*",end="")
                        elif (row==5) and ( col==3 or col==35):
                            print("*",end="")
                        else:
                            print(end=" ")
                    print()                    
            won()
            print()
            print ("Congratulations!")
            # exit the script
            break
        print()
        # ask the user go guess a character
        input_character = input("guess a character:")
        guess=input_character.lower()
        # set the players guess to guesses
        guesses += guess
        # if the guess is not found in the secret word
        if guess not in word:
         # turns counter decreases with 1 (now 9)
            turns -= 1
        # print wrong
            print ("Wrong")
        # how many turns are left
            print ("You have", + turns, 'more guesses')
        # if the turns are equal to zero
            if turns == 0:
            # print "You Loose"
                print ("You Loose\n The Write Answer is '{}'".format(word))

                
#CALLING THE FUNCTION TO START PLAYING
playnow()
#SECOND ATTEMPT
response=input("Wanna Play Again? [Y/N]")
yes=["Y","y","Yes","yes"]
no=["N","n","No","no"]
if response in yes:    
    playnow()
elif response in no:
    print("Thanks for playing hangman {}".format(name))
    
#END THE GAME
print("Tata Bye Bye!")
