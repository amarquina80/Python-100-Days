adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

# 👉 # Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
multiplication = 3.4 * 6.8
print(multiplication)

# division
division = 2467 / 4673
print(division)

#raise 10 to the power of 2
squared = 10**2
print(squared)

# print the remainder when 343 is divided by 4
modulo = 343 % 4
print(modulo)

myBill = float(input("what was the bill? "))
numberOfPeople = int(input("How many people ate? "))
answer = myBill / numberOfPeople
answer = round(answer, 2)
print("you pay ", answer)

print("Tip Calculator")
myBill = float(input("How much was the bill? "))
numberOfPeople = int(input("How many people ate? "))
answer = myBill / numberOfPeople
tipIncluded = answer * 1.1
tipIncluded = round(tipIncluded, 2)
print("you owe, with 10% tip included", tipIncluded)

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))


bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)


print("You all owe", final_amount)