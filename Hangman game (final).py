import random
from words import words
def hangman():
    word=random.choice(words)
 
    turns=10
    guessmade=""
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=""
       
    
    
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        
            
        if main_word==word:
            print(main_word)
            print ("The word was",word,".")
            print("Congratulations!!!, You're great and you have won...")
            print("It was really fun having you here!!!")
            break
            
    
        print("Guess the word", main_word)
        guess=input("Enter a letter:")
        
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("Enter valid character")
            guess=input()
        
        if guess not in word:
            turns=turns-1
        
            if turns==9:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")

                print("-------------------")
                print("9 more chances left!!!")
                print("--------+--+-------")
                print("           |       ")
                print("           |       ")
                print("           |       ")
            
            if turns==8:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("8 more chances left!!!")
                print("---------+--+------")
                print("         o  |      ")
                print("            |      ")
                print("            |      ")
            if turns==7:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("7 more chances left!!!")
                print("---------+--+------")
                print("         o  |       ")
                print("         |  |       ")
                print("            |       ")
            if turns==6:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("6 more chances left!!!")
                print("---------+--+------")
                print("         o  |       ")
                print("         |  |       ")
                print("        /   |       ")
            if turns==5:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("5 more chances left!!!")
                print("---------+--+------")
                print("         o  |       ")
                print("         |  |       ")
                print("        / \ |      ")
            if turns==4:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("4 more chances left!!!")
                print("---------+--+------")
                print("         o  |       ")
                print("        \|  |       ")
                print("        / \ |      ")
            if turns==3:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")

                print("Hurry up, only 3 more chances left!!!")
                print("---------+--+------")
                print("         o  |       ")
                print("        \|/ |       ")
                print("        / \ |      ")
            if turns==2:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")
                print("-------------------")
                print("Only 2 more chances left!!!")
                print("---------+--+------")
                print("        \o/ |      ")
                print("         |  |      ")
                print("        / \ |      ")
            if turns==1:
                print("-------------------")
                print("Sorry the letter you have entered isn't in the word")

                print("-------------------")
                print("Last chance left!!! Hangman on his last breath")
                print("---------+--+------")
                print("         o__|      ")
                print("        /|\ |      ")
                print("        / \ |      ")
            if turns==0:
                print("-------------------")
                print("Oops! You lost")
                print("-------------------")
                print("Sorry, you let a good man die")
                print("-------------------")
                print("The correct word was", word, ".","Better luck next time!!!")
                break
            
            
            
name=input("Enter your name:")
print("Welcome",name,"!")
print("Glad to have you here", name,"!" +" All the best and let's start the Hangman Game... Huhu")
print("-----------------")
print("Try to guess the words in less than 10 attempts")

def main():
    word=hangman()
    hangman()
    while input("Do you wish to play again?(Y/N) ").upper()=="Y":
        word=hangman()
        hangman
if __name__== "__main__":
    main()



    

    

            
            