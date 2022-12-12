counter = 0
while counter <= 100:
  print(counter)
  counter+=1

exit =""
while exit != "yes":
  print("🥳")
  exit = input("exit?: ")

counter = 0
while counter < 25:
  print(counter)
  counter +=1

counter = 0
while counter <= 12:
  print(counter)
  counter += 1

exit = ""
while exit != "yes":
  print("🥳")
  exit = input("Exit?: ")

exit = "no"

while exit == "no":
  animal_sound = input("What animal sound do you want to hear?")
  
  if animal_sound == "Dog" or animal_sound == "dog":
    print("🐶 aarf")
  elif animal_sound == "Cat" or animal_sound == "cat":
    print ("🐱 Meow")
  elif animal_sound == "frog" or animal_sound == "frog":
    print ("🐸 ribbet")
  elif animal_sound == "duck" or animal_sound == "Duck":
    print("🦆 Quack")
  elif animal_sound == "Snake" or animal_sound == "snake":
    print("🐍 sssssshhhh")
  elif animal_sound == "Monkey" or animal_sound == "monkey":
    print("🐵 uuuhh aahh")
  else: 
    print("I don't know that animal sound. Try again.")

  exit = input("Do you want to exit?: ")