#Hey I have Copyright of this code,truely mine.If You OWned This mail me:saswatamohapatra05@gmail.com
import random
print("WINNIG RULE OF THIS GAME "+"\n"+"\n"+ "1."+"PAPER COVER ROCK SO WINNER IS:>"+"PAPER"+
                                   "\n"+"2."+"scissors Cuts paper SO WINNER IS:>"+"SCISSORS"+
                                   "\n"+"3."+"Rock Smashes Scissors SO WINNER IS:>"+"Rock"+"\n"+"\n"+"\n"+"\n")
  
while True: 
    print("Enter choice \n 1. ROCK \n 2. PAPER \n 3. SCISSOR \n")


    option= int(input("\n HEY! ENTER YOUR CHOICE: "))
    
    #to avoid wrong input
    while option >3 or option <1:
        option = int(input("PLEASE ENTER VALID INPUT:"))

    if option == 1:
        options= 'ROCK'
    elif option == 2:
        options = 'PAPER'
    elif option == 3:
        options = 'SCISSOR'

    print("FINAL SELCTED OPTION FOR USER IS :" + options)
    print("\nNOw Its ALL ABOUT computer choice  ")
    
    master_option=random.randint(1,3)
    
    while master_option == option:
        master_option = random.randint(1,3)

    if master_option== 1:
        moptions= 'ROCK'
    elif master_option == 2:
        moptions = 'PAPER'
    elif master_option == 3:
        moptions = 'SCISSOR'

    if((option == 1 and master_option == 2) or (option == 2 and master_option == 1)):
        print("PAPER WINS ")
        RESULT = "paper"
    if((option == 1 and master_option == 3) or (option == 3 and master_option == 1)):
        print("ROCK WINS ")
        RESULT = "ROCK"
    else:
        print("scissor win:")
        RESULT="scissor"
    
    if RESULT == options: 
        print("..........User wins..........") 
    else: 
        print("..........Computer wins.........") 
          
    #This is string input so enter like this 'y' not like y,if you didn't get it mail me on above mail 
    ans =input("Do you want to play again? (Y/N)")
    
    if ans is 'n' or ans is "N":
        break

print("Come and Play again I wil Miss You")






    
