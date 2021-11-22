start = input("...Welcome to the Quiz World!...")
play = input("Do you want to play ?\n")
if play.lower() != "yes":
    quit()
print("Okay... Let's Play!...")
score = 0

answers = input("What does AI stands for ? \n")
if answers.lower() == "artificial intelligence":
    print("Wow....Correct Answer!")
    score += 1
else:
    print("Oops....It's Incorrect Answer")

answers = input("What does MI stands for ? \n")
if answers.lower() == "machine learning":
    print("Wow....Correct Answer!")
    score += 1
else:
    print("Oops....It's Incorrect Answer")

answers = input("What does RPA stands for ? \n")
if answers.lower() == "robotic process automation":
    print("Wow....Correct Answer!")
    score += 1
else:
    print("Oops....It's Incorrect Answer")

answers = input("What does IoT stands for ? \n")
if answers.lower() == "internet of things":
    print("Wow....Correct Answer!")
    score += 1
else:
    print("Oops....It's Incorrect Answer")

print("You got " + str(score) + " correct answers")
print("You got " + str((score/4)*100) + " %.")






