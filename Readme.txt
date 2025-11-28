Project URL:https://roadmap.sh/projects/number-guessing-game

This code implements a Number Guessing Game with multiple difficulty levels. Here's a step-by-step description of how it runs:

                                                  ****Program Flow****

1. Initial Setup

    Prints a welcome banner with decorative lines

    Generates a random number between 1-100 using randint(1,100)

2. Main Game Loop

The program enters a while loop that continues as long as the player wants to play.

3. Difficulty Selection

    Asks the player to choose difficulty: Easy (E), Medium (M), or Hard (H)

    Each difficulty gives different numbers of attempts:

        Easy: 20 chances

        Medium: 15 chances

        Hard: 10 chances

4. Gameplay Loop

For the selected difficulty, the program enters an inner while True loop where:

    Player guesses a number between 1-100

    The program checks if the guess matches the random number

    If correct: Shows congratulatory message with number of attempts used

    If incorrect:

        Tells if the actual number is higher or lower

        Decreases remaining chances by 1

        Shows remaining chances

    If chances run out: Reveals the secret number and ends the game

5. Play Again Prompt

After each game round, the program asks if the player wants to play again:

    If they enter "yes": A new random number is generated and the game restarts

    If they enter anything else: The program exits

6. Exit

    Displays a thank you message

    Prints decorative closing lines

                                       ****Key Features****

    -Three difficulty levels with different challenge levels

    -Feedback on whether guesses are too high or too low

    -Attempt counter

    -Replay functionality

    -User-friendly messages and formatting