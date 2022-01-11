print("Welcome to Aniquiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Begin :)")
Score = 0
answer = input("What three shows are considered the big three? ").lower()
if answer == "one piece, bleach and naruto":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What are the names of the protagonists from each show? ").lower()
if answer == "luffy, ichigo and naruto":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("How old was killua when he was sent to Heavens arena? ").lower()
if answer == "6 years old":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What number was Kurapikas badge during the hunter exam? ").lower()
if answer == "404":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("In Hajime no Ippo, how did Takamura get the scars on his chest? ").lower()
if answer == "by fighting a bear":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("Who did Ippo consider His Greatest Rival? ").lower()
if answer == "ichiro miyata":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("How old was Luffy when he first set out to sea? ").lower()
if answer == "17 years old":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("Who is Considered Luffy's Right hand Man. Ussop, Sanji or Zoro? ").lower()
if answer == "zoro":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What is the meaning behind Ichigo's Name? ").lower()
if answer == "strawberry":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What are Ichigo's sisters names? ").lower()
if answer == "yuzu and karin":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("How did Rimru get a Human body? ").lower()
if answer == " by absorbing shizu":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What kind of woman does Yuji Itadori like ? ").lower()
if answer == "a tall woman with a big ass":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("Kuga Yuma is a character from which anime? ").lower()
if answer == "world trigger":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("In One Punch Man what is the name of the villain that beat up Mumen rider? ").lower()
if answer == "deep sea king":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What is the name of the special abilities some characters have in World trigger called? ").lower()
if answer == "side effects":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("In dragon ball super, who hired an assassin to kill Goku? ").lower()
if answer == "goku":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What is the name of the galatic Patrol officer that appeared in dragon ball super? ").lower()
if answer == "jaco":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("In Naruto what is the name of the ninja who tricks naruto into stealing the forbidden scroll? ").lower()
if answer == "mizuki":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What is the name of Zabuza's sword? ").lower()
if answer == " executioner's blade":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("Why is Kakashi always late? ").lower()
if answer == "he visits the memorial stone":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("How long can a ghoul survive when only eating one human body? ").lower()
if answer == "a month":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")

answer = input("What was Suzuya's Original Name before he changed it? ").lower()
if answer == "rei":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!!:(")
print("You got" + str(Score) + "questions correct!")
print(" You got" + str((Score/22) * 100) + "%")
print(" Thanks for participating!! hope you had fun!! :)")
