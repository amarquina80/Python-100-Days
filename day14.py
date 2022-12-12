from getpass import getpass as input

print("EPIC ✂️ 📜 🪨 BATTLE")
print()

print("Select your move (R, P or S)")
print()

player1Move = input("Player 1 > ")
print()
player2Move = input("Player 2 > ")
print()

if player1Move=="R" or player1Move=="r":
  if player2Move=="R" or player2Move=="r":
    print("You both picked Rock, draw!")
  elif player2Move=="S" or player2Move=="s":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  elif player2Move=="P" or player2Move=="p":
    print("Player1's Rock is smothered by Player2's Paper!")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="P" or player1Move=="p":
  if player2Move=="R" or player2Move=="r":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player2Move=="S" or player2Move=="s":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  elif player2Move=="P" or player2Move=="p":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  else:
    print("Invalid Move Player 2!")
elif player1Move=="S" or player1Move=="s":
  if player2Move=="R" or player2Move=="r":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player2Move=="S" or player2Move=="s":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
  elif player2Move=="P" or player2Move=="p":
    print("Player1's Scissors make confetti out of Player2's paper!")
  else:
    print("Invalid Move Player 2!")
else:
  print("Invalid Move Player 1!")