myScore = int(input("What is your score: "))
if myScore > 100000:
  print("Winner!🥳")
else:
  print("Try again🥲")  

myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😞")

score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")

print("Generation Identifier")

birthYear = int(input("Which year were you born? "))
if birthYear <=1900 :
  print("Ha! You are from Lost Generation!")
elif birthYear >= 1901 and birthYear <=1927: 
  print("Greatest generation")
elif birthYear >= 1928 and birthYear <=1945: 
  print("Silent genaration")
elif birthYear >= 1946 and birthYear <=1964: 
  print("Baby boomers")
elif birthYear >= 1965 and birthYear <=1980: 
  print("Generation X")
elif birthYear >= 1981 and birthYear <=1996: 
  print("Millenials")
elif birthYear >= 1997 and birthYear <=2012: 
  print("Generation Z")
elif birthYear >= 2013 : 
  print("Generation Alpha")  
else:
  print("Enlighten me, try again")