from random import randint

print("="*120)
print("Welcome to python Number Guessing Game")
print("="*120)

rand_num = randint(1,100)

play_agi="yes" 

while play_agi.lower() == "yes" :
    print("-"*10)
    difuc= input("What difficulty you choose? (E/M/H):")
    print("-"*10)
    if difuc.lower() == "e":
        dif_chances = 20
        chances= 20
        print(f"The easy mode:you have {chances} chances.")
        while True:
            guess = int(input("Can you give a guess from 1 to 100?:"))
            if guess == rand_num :
                print(f"Congrats! you won The number was {rand_num} you took {dif_chances-chances } attempts to get it.")
                break
            elif chances < 1 :
                print(f"You ran out of chances the number was {rand_num}.")
                break
            elif guess > rand_num :
                print(f"The number is less than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.")
            elif guess < rand_num :
                print(f"The number is greater than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.")
    if difuc.lower() == "m":
        dif_chances = 15
        chances=15
        print(f"The medium mode: you have {chances} chances.")
        while True:
            guess = int(input("Can you give a guess from 1 to 100?:"))
            if guess == rand_num :
                print(f"Congrats! you won The number was {rand_num} you took {dif_chances-chances } attempts to get it.")
                break
            elif chances < 1 :
                print(f"You ran out of chances the number was {rand_num}.")
                break
            elif guess > rand_num :
                print(f"The number is less than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.")
            elif guess < rand_num :
                print(f"The number is greater than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.") 
    if difuc.lower() == "h":
        dif_chances = 10
        chances=10 
        print(f"The hard mode: you have {chances} chances.")
        while True:
            guess = int(input("Can you give a guess from 1 to 100?:"))
            if guess == rand_num :
                print(f"Congrats! you won The number was {rand_num} you took {dif_chances-chances } attempts to get it.")
                break
            elif chances < 1 :
                print(f"You ran out of chances the number was {rand_num}. ")
                break
            elif guess > rand_num :
                print(f"The number is less than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.")
            elif guess < rand_num :
                print(f"The number is greater than {guess}.")
                chances = chances - 1
                print(f"You have {chances} chances left.")
            
    print("\nWould you like to play again?")
    play_agi = input("Enter 'yes' to continue, or anything else to quit: ")
    if not play_agi.lower() == "yes":
        break
print("\nThanks for playing! Come back soon! 👋")
print("=== ==="*10 )