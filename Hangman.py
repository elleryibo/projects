#Ellery Ibo - 3/11/19
#Hangman Project

#converts the secret phrase to dashes
def wordToDash(w):
    count=0
    dash=""
    while len(w)>count:
        if w[count]>="A" and w[count]<="z":
            dash=dash+"_ "
        else:
            dash=dash+w[count]+" "
        count=count+1
    return dash

#checks if the guess is a letter 
def validate(g):
    while g<"A" or g>"z":
        print("Not a valid character. Please enter a letter.")
        g=input("Your guess (letters only):")
    return g

#checks if the guess has only been entered once
def checkUsed(oldGuess,guess):
    n=0
    while len(oldGuess)>n:
        if oldGuess[n]==guess:
            guess=input("Letter has already been used. Please enter another letter:")
        n=n+1
    return guess

#checks that the guess is correct
def missedLetters(guess,word):
    for n in range(len(word)):
        if word[n]==guess:  
            return False   
    return True

#determines the number of guesses the user has left
def triesLeft(word, guess, tries):
    n=0
    while len(word)>n:
        if guess==word[n]:
            print("Chances remaining:"+str(tries))
            return tries
        n=n+1
    n=n-1
    if guess!=word[n]:
        tries=tries-1
        print("Chances remaining:"+str(tries))
        return tries

#replaces the dash with the corrrect guess
def guessCheck(word,guess,dash):
    for n in range(len(word)):
        if guess==word[n]:
            dash=dash[:2*n]+guess+dash[(2*n)+1:]
    return dash

#checks if the user has won
def winCheck(dash):
    for n in range(len(dash)):
        if dash[n]=="_":
            return False
    return True
       
def main():
#intro
    print("""Hangman is a popular word game. You are given a number of blanks
representing a hidden phrase. The goal of this game is to guess this
phrase correctly using a maximun of 6 chances. Good luck!""")
    word=input("Please enter phrase to guess: ")
    word=word.lower()
    print("Chances Remaining: 6")
    print("Missed Letters: None")
#addtional variables to be used with the game functions
    tries=6
    oldGuess=""
    missed=""
    c=0
    dash=wordToDash(word)
    print(dash)

#loop to determine the end of the game
#this runs the game
    while tries>0:
        print("")
        guess=input("Your guess (letters only):")
        guess=(validate(guess))
        guess=(checkUsed(oldGuess,guess))
        oldGuess=oldGuess+guess
        tries=triesLeft(word,guess,tries)
        if missedLetters(guess,word)==True:
            missed=missed+guess
            print("Missed Letters:",missed)
            c=c+1
        if c==0:
            clear="None"
            print("Missed Letters:",clear)
        elif c!=0 and missedLetters(guess,word)==False:
            print("Missed Letters:",missed)
        dash=guessCheck(word,guess,dash)
        print(dash)
        print("")
        if winCheck(dash)==True:
            print("The phrase has been guessed!")
            return 0
        elif winCheck(dash)==False and tries==0:
            print("You ran out of turns! The phrase was",word+". Try again next time!")
            return 0
                    
main()
#asks the user if they want to play again
replay=input("""Type 'yes' to play again!
Or type 'no' to exit: """)

def rerun(rePlay):
    while replay=="yes":
        print("")
        main()
rerun(replay)
    
    
