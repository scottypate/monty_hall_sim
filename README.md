### The Monty Hall Problem

This is probability problem is modeled off of the old game show "Let's Make A Deal". Suppose the host of the show presents you with 3 doors. 1 door contains a new car. 2 doors contain a goat.
You get to choose a single door with the hopes of selecting the car.

```python
import random

doors = [1, 2, 3]
door_with_the_car = random.choice(doors)
your_initial_choice = random.choice(doors)

print('You selected door #{}'.format(your_initial_choice))
``` 

Output: `You selected door #1`

The host of the show then opens one of the doors you didn't choose to reveal a goat.

```python
door_host_reveals = random.choice(
    [
     door for door in doors 
     if door not in [door_with_the_car, your_initial_choice]
    ]
)

print('The host reveals door #{}'.format(door_host_reveals))
```

Output: `The host reveals door #2`

Now there are 2 doors remaining on unopened on stage.
Just to confuse you, the host offers you the opportunity to switch your choice of doors to the one remaining unopened.
Now you have a choice. Do you switch your choice to the remaining door that is left unrevealed, or stay with your original choice?
Two doors left on stage. You don't know what is behind either one. You might think you have a 50/50 probability at this point. Lets see....

##### Scenario 1: You keep your original door choice.

```python
# All the code has been copied here so that we can run 
# this problem numerous times in the simulation.

doors = [1, 2, 3]
wins = 0
losses = 0
n = 10000

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
```

Output: `After 10000 rounds, you won 0.3318% of the time keeping your choice.`

##### Scenario 2: You switch doors.

```python
# All the code has been copied here so that we can run 
# this problem numerous times in the simulation.

doors = [1, 2, 3]
wins = 0
losses = 0
n = 10000

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
```

Output: `After 10000 rounds, you won 0.6682% of the time switching your choice.`

So you win twice as often switching doors as you do keeping your original choice.

#### Intuition behind this problem

When you select you initial door choice the probability of selecting the door with the car is 0.33 (1/3).
The probability of selecting a door without the car is 0.66 (2/3). These initial probabilites do not change with the reveal of a door by the host. 
When the host gives you the option to switch doors, you now have the chance to take "the field" against your initial choice which is 0.66.


[Here is a link to more information about this brain teaser](http://marilynvossavant.com/game-show-problem/)