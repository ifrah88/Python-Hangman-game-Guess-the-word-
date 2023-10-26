import hangmanimages
import random
import time


def chooseWord():
    # inFile: file
    inFile = open("hangmanwords.txt", 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    global word
    word=random.choice(wordlist)
    #print(word)
    
chooseWord()

# The parameters we require to execute the game:
def main():
    #declaring global variables so they can be used outside this function as well.
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global limit
    
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def func():	
    global word
    if word == '_' * length:
        if user_setting==1:
            print("score = 200 points")
        elif user_setting==2:
            print("score = 400 points")
        elif user_setting==3:
            print("score = 600 points")
        elif user_setting==4:
            print("score = 800 points")
        elif user_setting==5:
            print("score = 1000 points")
     
# A loop to re-execute the game when the first round ends:     
def play_loop():
    global play_game
    play_game = input("Would you like to play again? Press 'y' for yes and 'n' for no.\n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Would you like to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank you for playing! We hope you'll come back again soon! ")
        

guessed_display_tup=()
guessed_display=set(guessed_display_tup)
# Initializing all the conditions required for the game:
def hangman():
    #global variables need to be declared in each function we are using them: 
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = number_of_lives
    
    
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    #using guess.strip() to remove any spaces in the string
    guessed_display.add(guess)
    
    
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2:
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
        print("already guessed: " + str(guessed_display))

    elif guess in already_guessed:
        print("Try another letter.\n")
        

    else:
        count += 1
     
        
        if limit==10:
            if guess not in word:
                if count == 1:
                    time.sleep(1)
                    print(hangmanimages.dict["first"])
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                    
                elif count == 2:
                     time.sleep(1)
                     print(hangmanimages.dict["second"])
                     print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 3:
                     time.sleep(1)
                     print(hangmanimages.dict["third"])
                     print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 4:
                     time.sleep(1)
                     print(hangmanimages.dict["fourth"])
                     print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 5:
                      time.sleep(1)
                      print(hangmanimages.dict["fifth"])
                      print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 6:
                      time.sleep(1)
                      print(hangmanimages.dict["sixth"])
                      print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 7:
                        time.sleep(1)
                        print(hangmanimages.dict["seventh"])
                        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 8:
                         time.sleep(1)
                         print(hangmanimages.dict["eighth"])
                         print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 9:
                          time.sleep(1)
                          print(hangmanimages.dict["ninth"])
                          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
               
                elif count == 10:
                             time.sleep(1)
                             print(hangmanimages.dict["tenth"])
                             print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                             print("The word was:",already_guessed,word)
                             play_loop()
                
        elif limit==8:
            if guess not in word:
                if count == 1:
                    time.sleep(1)
                    print(hangmanimages.dict["first"])
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 2:
                      time.sleep(1)
                      print(hangmanimages.dict["second"])
                      print("Wrong guess. " + str(limit - count) + " guesses remaining\n") 
                elif count == 3:
                     time.sleep(1)
                     print(hangmanimages.dict["fourth"])
                     print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 4:
                     time.sleep(1)
                     print(hangmanimages.dict["fifth"])
                
                elif count == 5:
                        time.sleep(1)
                        print(hangmanimages.dict["sixth"])
                        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 6:
                        time.sleep(1)
                        print(hangmanimages.dict["eighth"])
                        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 7:
                          time.sleep(1)
                          print(hangmanimages.dict["ninth"])
                          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 8:
                            time.sleep(1)
                            print(hangmanimages.dict["tenth"])
                            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                            print("The word was:",already_guessed,word)
                            play_loop()
               
        elif limit==6:
            if guess not in word:
                if count == 1:
                    time.sleep(1)
                    print(hangmanimages.dict["second"])
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 2:
                      time.sleep(1)
                      print(hangmanimages.dict["fourth"])
                      print("Wrong guess. " + str(limit - count) + " guesses remaining\n") 
                elif count == 3:
                     time.sleep(1)
                     print(hangmanimages.dict["fifth"])
                
                elif count == 4:
                        time.sleep(1)
                        print(hangmanimages.dict["seventh"])
                        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 5:
                          time.sleep(1)
                          print(hangmanimages.dict["ninth"])
                          print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                elif count == 6:
                            time.sleep(1)
                            print(hangmanimages.dict["tenth"])
                            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
                            print("The word was:",already_guessed,word)
                            play_loop()
               
        elif limit==4:
            if guess not in word:
                if count == 1:
                    time.sleep(1)
                    print(hangmanimages.dict["third"])
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
                elif count == 2:
                    time.sleep(1)
                    print(hangmanimages.dict["sixth"])
                    print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
                elif count == 3:
                    time.sleep(1)
                    print(hangmanimages.dict["eighth"])
                    print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        
                elif count == 4:
                    time.sleep(1)
                    print(hangmanimages.dict["tenth"])
                    print("Wrong guess. You are hanged!!!\n")
                    print("The word was:",already_guessed,word)
                    play_loop()
    
        elif limit==2:
            if guess not in word:
                if count == 1:
                   time.sleep(1)
                   print(hangmanimages.dict["fifth"])
                   print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            
                elif count == 2:
                   time.sleep(1)
                   print(hangmanimages.dict["tenth"])
                   print("Wrong guess. You are hanged!!!\n")
                   print("The word was:",already_guessed,word)
                   play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        func()
        
       
        play_loop()

    elif count != limit:
        hangman()

#Welcoming the user to the game and using time.sleep() to increase interactivity:
print("\nWelcome to our Hangman game \n")
time.sleep(2)
user_choice=input("would you like to play? press (1) if yes or (0) if no")

if user_choice=="1":
    print("Enjoy this game!")
    time.sleep(2)
    name=input("Enter your name: ")
    print("Hello " + name + "! Good luck!")
    print("Loading...")
    time.sleep(3)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)
    print("There are multiple difficulty settings shown below:")
    print("\t1. Easy (10 lives)")
    print("\t2. Medium (8 lives)")
    print("\t3. Hard (6 lives)")
    print("\t4. Expert (4 lives)")
    print("\t5. Pro Insane(2 lives)")
    user_setting = input("Choose what mode you would like to play in: ")

    if (str(user_setting) == "1"):
	    number_of_lives = 10
	    print("\nYou have chosen %s and will receive %d lives." % ("Beginner", number_of_lives))
    elif(str(user_setting) == "2"):
	    number_of_lives = 8
	    print("\nYou have chosen %s and will receive %d lives." % ("Intermediate", number_of_lives))
    elif (str(user_setting) == "3"):
	    number_of_lives = 6
	    print("\nYou have chosen %s and will receive %d lives." % ("Expert", number_of_lives))
    elif (str(user_setting) == "4"):
	    number_of_lives = 4
	    print("\nYou have chosen %s and will receive %d lives." % ("Advanced", number_of_lives))
    elif (str(user_setting) == "5"):
	    number_of_lives = 2
	    print("\nYou have chosen %s and will receive %d lives." % ("Insane", number_of_lives))
    else:
	    number_of_lives = 10
	    print("\nYou have made an invalid selection and will receive %d lives by default." % number_of_lives)
    	
    	# Choose a difficulty level
    main()
    hangman()
    
else:
    print("Bye bye...")
    print("Come back again soon!")
