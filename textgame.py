answer_yes=("Yes","Y","yes","y")
answer_no=("No","N","no","n")

print("""
WELCOME! LET'S START THE ADVENTURE

You are going home in your car where you see a women in dirty clothes running

towards you and asking for a ride

Will you give her a ride home.(yes/no)

""")

ans1=input(">>")

if ans1 in answer_yes:
    print("\n After five minutes,you are stopped at a checkpoint and police asks you if you seen a suspicious women. Will you say(yes/no)")

    ans2=input(">>")

    if ans2 in answer_yes:
        print("\n You are an honest persion. she was a murderer & you won the game")

    elif ans2 in answer_no:
        print("\n You helped a murderer. Now, go to jail.GAME OVER")

    else:
        print("\n You have enterd the wrong input. GOODBYE!")

elif ans1 in answer_no:
    print("\n Now,she is trying to kill you. Will you knock her down?(yes/no)")

    ans3=input(">>")

    if ans3 in answer_yes:
        print("\n Congrats! She was a murderer & You helped the police to catch her with your bravery.")

    elif ans3 in answer_no:
            print("\n Sorry! You are dead. She was a murderer & she killes you. GAME OVER")

    else:
            print("\n You have enterd a wrong input. GOODBYE!")
else:
    print("\n You have enterd a wrong input. GOODBYE!")
            
        



















    
    
