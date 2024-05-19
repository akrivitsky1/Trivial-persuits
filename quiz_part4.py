score = 0

###Question 1
question_1 ="ART AND LITERATURE: Who painted Starry Night?"
answer_1a = "Vincent van Gogh"
answer_1b = "Michelangelo"
answer_1c = "Leonardo da Vinci"

print(question_1)
print("a.",answer_1a)
print("b.", answer_1b)
print("c.", answer_1c) 
answer_1 = input("Enter your choice:")
if (answer_1 == "a"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

###Question 2
question_2 = "ENTERTAINMENT: How many oscars did Alfred Hitchcock win?"
answer_2a = "None"
answer_2b = "One"
answer_2c = "Two"

print(question_2)
print("a.",answer_2a)
print("b.", answer_2b)
print("c.", answer_2c) 
answer_2 = input("Enter your choice:")
if (answer_2 == "a"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

###Question 3
question_3 = "GEOGRAPHY: Which is the largest ocean?"
answer_3a = "Pacific"
answer_3b = "Atlantic"
answer_3c = "Indian"

print(question_3)
print("a.",answer_3a)
print("b.", answer_3b)
print("c.", answer_3c) 
answer_3 = input("Enter your choice:")
if (answer_3 == "a"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

###Question 4
question_4 = "HISTORY: Who was the first U.S. president to appear on a coin?"
answer_4a = "Washington"
answer_4b = "Lincoln"
answer_4c = "Jefferson"

print(question_4)
print("a.",answer_4a)
print("b.", answer_4b)
print("c.", answer_4c) 
answer_4 = input("Enter your choice:")
if (answer_4 == "b"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was b")

###Question 5
question_5 = "SCIENCE AND NATURE: Can pigs swim?"
answer_5a = "Yes"
answer_5b = "No"
answer_5c = "Only in salt water"

print(question_5)
print("a.",answer_5a)
print("b.", answer_5b)
print("c.", answer_5c) 
answer_5 = input("Enter your choice:")
if (answer_5 == "a"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was a")

###Question 6
question_6 = "SPORT AND LEISURE: What color is the middle Olympic ring?"
answer_6a = "Red"
answer_6b = "Blue"
answer_6c = "Black"

print(question_6)
print("a.",answer_6a)
print("b.", answer_6b)
print("c.", answer_6c)
answer_6 = input("Enter your choice:")
if (answer_6 == "c"):
    print("Correct!")
    score = score + 1
else:
    print("The correct answer was c")

###Geunuis Question
question_g = "GENIUS: What is D divided by X?"

print(question_g)
answer_g = input("Enter your answer:")
if (answer_g == "L" or int(answer_g) == 50):
    print("Correct!")
    score = score + 1
else:
    print("Correct answers were L or 50")


###Final score
print("Your final score is",score)



    
    


    
