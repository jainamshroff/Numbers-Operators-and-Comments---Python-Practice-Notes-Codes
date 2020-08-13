# Rock Paper Scissor
# Instructions

print("---ROCK PAPER SCISSORS---")

playerone = input("Player 1, Make Your Move: ")
playertwo = input("Player 2, Make Your Move: ")

if(playerone == 'rock' and playertwo == 'scissors'):
    print("Player One Wins !")

elif(playerone == 'rock' and playertwo == 'paper'):
    print("Player Two Wins !")

elif (playerone == 'paper' and playertwo == 'rock'):
    print("Player One Wins !")

elif (playerone == 'paper' and playertwo == 'scissors'):
    print("Player Two Wins !")

elif (playerone == 'scissors' and playertwo == 'rock'):
    print("Player Two Wins !")

elif (playerone == 'scissors' and playertwo == 'paper'):
    print("Player One Wins !")

elif(playerone == playertwo):
    print("Its a Tie!")

else:
    print("Something went wrong!, Check Your Input")

