print("Exam Grade Calculator")
print()
exam_name = input("Name of exam: ")
print()
max_possible_score = int(input("Max. Possible Score: "))
your_score = int(input("Your score: "))
print()

raw_score = float(your_score/max_possible_score)
final_number = round(raw_score, 2)

percentage_score = round(float(your_score/max_possible_score)*100, 2)

print("You got",percentage_score,"%")

if  final_number >= .90:
  print("Your got an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your got an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your got a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your got a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your got a D.")
elif final_number <= .49:
  print("Your got a U.")
else: 
  print("Try again!")