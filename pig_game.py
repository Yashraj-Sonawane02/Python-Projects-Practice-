# practice purpose - simple dice game where players roll a dice to accumulate points, but wolling a 1 resets their turn's score , forcing a strategic choice between risk and reward.
import random

def roll():
    min = 1;
    max = 6;
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Enter the number of players(2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4")

    else:
        print("Invalid , Try again !")
        continue

max_score = 50
players_scores = [0 for _ in range(players)]


while max(players_scores) < max_score:

    for player_idx in range(players):
        print(f"\nplayer number {player_idx + 1} turn ha just started")
        print("Your current score is:",players_scores[player_idx],"\n" )
        current_score = 0 

        while True:
            should_roll = input("Would you like to roll(y) : ").lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("Your rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"Yo rolled a {value}")

            print(f"Your score is {current_score}")

        players_scores[player_idx] += current_score
        print(f"Your Total score is {players_scores[player_idx]}")

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"Player number {winning_idx+1} is the winner with a score of {max_score}")
