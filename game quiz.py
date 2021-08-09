from random import shuffle
from questions import *

shuffle(questions)

for question in questions:
    

    
    print(question["question"])
    for pos,option in enumerate(question["options"]):
        print(f"\t{pos} {option}")
    num = int(input("Enter a number from 0 to 3: "))
    while num >3 or num <0: 
        print("Please input a number between 0 and 3.")
        num = int(input("Try again: "))
    if num == question["answer"]:
        print("Correct!")
    else:
        print ("False!")
