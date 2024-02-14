import random

options=['rock','paper','scissor']


print("Rock paper scissors game ! ")
print("----------------------------------------------------")

player=None
pcchoice=random.choice(options)
playing=True

scoreme=0
scorepc=0
while playing:
    i=input("Enter rock,paper or scissor : ")
    if i==pcchoice:
        print("Tie")
        scoreme+=1
        scorepc+=1
        print("Your score : ",scoreme)
        print("Computer score : ",scorepc)


    elif i=="rock":
        if pcchoice=="paper":
            print("Computer wins")
            scorepc+=1
        else:
            print("You win!")
            scoreme+=1
        print("Your score : ",scoreme)
        print("Computer score : ",scorepc)


    elif i=="paper":
        if pcchoice=="scissor":
            print("Computer wins")
            scorepc+=1
        else:
            print("You win!")
            scoreme+=1
        print("Your score : ",scoreme)
        print("Computer score : ",scorepc)

    elif i=="scissor":
        if pcchoice=="rock":
            print("Computer wins")
            scorepc+=1
        else:
            print("You win!")
            scoreme+=1
        print("Your score : ",scoreme)
        print("Computer score : ",scorepc)

    c=input("Want to play again(y/n)? : ")
    if c=='y':
        playing=True
    else:
        playing=False
