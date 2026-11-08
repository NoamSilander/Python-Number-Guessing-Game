# Number Guessing Game
A number guessing game written in Python

Works by utilizing the `Random` module and calling `randint()`

The script picks a number in a specified range, then makes you guess it only helping you by telling if your guess is **higher** or **lower** than the script's choice.

## How to run
1. Run `number_guessing_game.py`

## Example
```
Give me a starting and ending number, I'll choose a number between them, then you're going to have to guess it.
I'll help you by telling you if your guess is higher or lower than my number.
What should my starting number be?: 1
What should my ending number be?: 20
My range will be 1-20, are you sure? (y/n): y
I've chosen a number!
Guess my number!: 10
Lower!
Guess my number!: 5
You did it! My number was 5!
It took you exactly 2 guesses!
Do you want to play again? (y/n) y
Playing again!
Give me a starting and ending number, I'll choose a number between them, then you're going to have to guess it.
I'll help you by telling you if your guess is higher or lower than my number.
What should my starting number be?: 1
What should my ending number be?: 30
My range will be 1-30, are you sure? (y/n): y
I've chosen a number!
Guess my number!: 20
Lower!
Guess my number!: 15
Higher!
Guess my number!: 19
Lower!
Guess my number!: 17
Lower!
Guess my number!: 16
You did it! My number was 16!
It took you exactly 5 guesses!
Do you want to play again? (y/n): n
```