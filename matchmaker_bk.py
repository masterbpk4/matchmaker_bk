##Brenden Kelley 2020 All Rights Reserved
##Just kidding this is all open source
##Just make sure you credit me if you realize that this is a marvel of coding genius and decide to use it in the future



##First we need to get our questions placed in an array and ready to be pulled on command, we'll also need an empty array to keep track of the user's score
question = ["- Cats are better than dogs." , "- Mountains are better than beaches." , "- Sitting down and watching anime is a good pastime" , "- I enjoy tabletop rpgs or would be interested in trying them." , "- I prefer sweet snacks over salty ones."]
score = []
finalscore = []
##We need an introduction to our program
def Intro():
    print("=".center(120, "="))
    print("Hello and Welcome to The Ultimate Matchmaker! You will be given a series of statements where you are asked to rate how\n much you agree or disagree with them on a scale of 1 to 5 where 1 is strongly disagree and 5 is strongly agree.")
    print("=".center(120, "="))
##Next we need to figure out what to do with user inputs
def userInputs():
    k = 0
    while k < 1:
        try:
            k = int(input("Your answer: "))
            if k == 1 or k == 2 or k == 3 or k == 4 or k == 5: 
                score.append(k)
            else:
                raise ValueError
        except ValueError:
            k = 0
            print("Please enter a number between 1 and 5")
##Next we need the function to ask the questions to the user
def askquestions():
    for i in range(0, len(question)):
        print("=".center(120, "="))
        print("Question #"+str(i+1))
        print(question[i])
        print("=".center(120, "="))
        print("Please Type Your Answer: ")
        userInputs()
        print("=".center(120, "="))
##Now we need to do math on the scores to determine if the user is a good match
def scorecalcs():
    for n in range(0, len(score)):
        if n == 0 or n == 4:
            p = int(score[n])
            p = 5 - abs(5-p)
            finalscore.append(p)
        elif n == 1 or n == 3:
            p = int(score[n])
            p = 5 - abs(5-p)
            p = 3 * p
            finalscore.append(p)
        elif n == 2:
            p = int(score[n])
            p = 5 - abs(5-p)
            p = p * 2
            finalscore.append(p)
##And now we need to make the final score
def results():
    total = 0
    for m in range(0, len(finalscore)):
        total = total + finalscore[m]
    total = total * 2
    if total < 40:
        print("I hope we never meet, you got a score of: " + str(total))
    elif total >= 40 and total < 80:
        print("I think we would be good friends, you got a score of: " + str(total))
    elif total >= 80:
        print("I think we were made for each other! You got a score of: "+ str(total))
##Now it's time to put everything we've done to work
Intro()
input("Press any key to continue. . .")
askquestions()
scorecalcs()
results()