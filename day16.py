while True:
  print("This program is running")
  goAgain = input("Go again:? ")
  if goAgain == "no":
    break
print("Aww, I was having fun")

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

counter = 0
while True:
  answer = int(input("Enter a number: "))
  print("Adding it up!")
  counter += answer
  print("Current total is", counter)
  addAnother = input("Add another? ")
  if addAnother == "no":
    break
print("Bye!")

while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")
print("I don't like red")

print("Name the artist!")
print()
print("Type the name of the artist of the song as quickly as you can!")
print()

counter = 1
while True:
  song = input("And I....eeeh I will always love you. ")
  if song == "Whitney Houston" or song == "whitney houston" or song == "whitney":
    print("You got it!")
  else:
    print("Nope! Try again!")
    counter +=1
  if song == "Whitney Houston":
    break
print("Thanks for playing!")

print("You got the correct lyrics in", counter, "attempt(s).")