score = 0  ### Beggining score

###Question 1
question_1 ="ART AND LITERATURE: Who painted Starry Night?"
answer_1a = "Vincent van Gogh" ### Choice A
answer_1b = "Michelangelo"   ### Choice B
answer_1c = "Leonardo da Vinci" ### Choice C
 
print(question_1)
print("a.",answer_1a)
print("b.", answer_1b)
print("c.", answer_1c)  ###Printing Prompt
answer_1 = input("Enter your choice:")   ### Asks user for input
if answer_1 != "a" and answer_1 != "b" and answer_1 != "c": ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.") 
if (answer_1 == "a"): 
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was a")

###Question 2
question_2 = "ENTERTAINMENT: How many oscars did Alfred Hitchcock win?"
answer_2a = "None" ### Choice A
answer_2b = "One" ### Choice B
answer_2c = "Two" ### Choice C
 
print(question_2) 
print("a.",answer_2a)
print("b.", answer_2b)
print("c.", answer_2c)  ####Printing Prompt
answer_2 = input("Enter your choice:") ### Asks user for input
if answer_2 != "a" and answer_2 != "b" and answer_2 != "c": ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.")
if (answer_2 == "a"):
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was a")

###Question 3
question_3 = "GEOGRAPHY: Which is the largest ocean?"
answer_3a = "Pacific" ### Choice A
answer_3b = "Atlantic" ### Choice B
answer_3c = "Indian" ### Choice C

print(question_3)  
print("a.",answer_3a)
print("b.", answer_3b)
print("c.", answer_3c) ####Printing Prompt
answer_3 = input("Enter your choice:") ### Asks user for input
if answer_3 != "a" and answer_3 != "b" and answer_3 != "c":  ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.")
if(answer_3 == "a"):
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was a")

###Question 4
question_4 = "HISTORY: Who was the first U.S. president to appear on a coin?"
answer_4a = "Washington" ### Choice A
answer_4b = "Lincoln" ### Choice B
answer_4c = "Jefferson" ### Choice C

print(question_4) 
print("a.",answer_4a)
print("b.", answer_4b)
print("c.", answer_4c) ####Printing Prompt
answer_4 = input("Enter your choice:") ### Asks user for input
if answer_4 != "a" and answer_4 != "b" and answer_4 != "c":  ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.")
if (answer_4 == "b"):
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was b")
    

###Question 5
question_5 = "SCIENCE AND NATURE: Can pigs swim?"
answer_5a = "Yes" ### Choice A
answer_5b = "No" ### Choice B
answer_5c = "Only in salt water" ### Choice C

print(question_5) 
print("a.",answer_5a)
print("b.", answer_5b)
print("c.", answer_5c)  ####Printing Prompt
answer_5 = input("Enter your choice:") ### Asks user for input
if answer_5 != "a" and answer_5 != "b" and answer_5 != "c":  ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.")
if (answer_5 == "a"):
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was a")

###Question 6
question_6 = "SPORT AND LEISURE: What color is the middle Olympic ring?"
answer_6a = "Red" ### Choice A
answer_6b = "Blue" ### Choice B
answer_6c = "Black" ### Choice C

print(question_6) 
print("a.",answer_6a)
print("b.", answer_6b)
print("c.", answer_6c)  ####Printing Prompt
answer_6 = input("Enter your choice:") ### Asks user for input
if answer_6 != "a" and answer_6 != "b" and answer_6 != "c":   ### If not one of three choices
    print("Invalid input! Enter a, b, or c next time.")
if (answer_6 == "c"):
    print("Correct!")
    score = score + 1 ##Adds a point to the score
else:
    print("The correct answer was c")

###Geunuis Question
question_g = "GENIUS: What is D divided by X?"

print(question_g)
answer_g = input("Enter your answer:")
if (answer_g == "L" or answer_g == "50"):
    print("Correct!")
    score = score + 1
else:
    print("Correct answers were L or 50")


###Final score
print("Your final score is",score)

#### Grading score

if score >= 0 and score <= 2:  ### Score between 0 and 2
    print("You were unlucky!")
elif score >= 3 and score <= 4: ### Score between 3 and 4
    print("You did better than chance!")
elif score >= 5 and score <= 6: ### Score between 5 and 6
    print("You are a trivia star!")
else:
    print("Genius!")
    
    
    


    
