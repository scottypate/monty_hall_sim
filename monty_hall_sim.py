import random

# Three doors on the stage
doors = [1, 2, 3]
wins = 0
losses = 0

# Run the simulation n times
n = 10000

# You keep your original door selection
for i in range(n):
    door_with_the_car = random.choice(doors)
    your_initial_choice = random.choice(doors)
    door_host_reveals = random.choice(
        [
         door for door in doors
         if door not in [door_with_the_car, your_initial_choice]
        ]
    )

    if your_initial_choice == door_with_the_car:
        wins += 1
    else:
        losses += 1

win_pct = wins / (wins + losses)

print(
    'After {} rounds, you won {}% of the time keeping your choice.'.format(
        n, win_pct
    )
)

# Reset the wins and losses
wins = 0
losses = 0

# You change your door selection
for i in range(n):
    door_with_the_car = random.choice(doors)
    your_initial_choice = random.choice(doors)
    door_host_reveals = random.choice(
        [
         door for door in doors
         if door not in [door_with_the_car, your_initial_choice]
        ]
    )

    if your_initial_choice != door_with_the_car:
        wins += 1
    else:
        losses += 1

win_pct = wins / (wins + losses)

print(
    'After {} rounds, you won {}% of the time switching your choice.'.format(
        n, win_pct
    )
)