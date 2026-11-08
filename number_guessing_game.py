import random
def choice_generator(s, e):
    choice = random.randint(s, e)
    print("I've chosen a number!")
    return choice


def ask_number(question):
    while True:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print('Must be a whole number')

def ask_range():
    while True:
        s = ask_number('What should my starting number be?: ')
        while True:
            e = ask_number('What should my ending number be?: ')
            if e > s:
                break
            print('Ending number must be larger than starting number')
        while True:
            user_confirmation = input(f'My range will be {s}-{e}, are you sure? (y/n): ').lower().strip()
            if user_confirmation == 'y':
                return s, e
            elif user_confirmation == 'n':
                break

def ask_guess(s, e):
    while True:
        guess = ask_number('Guess my number!: ')
        if guess < s or guess > e:
            print(f'My number is in the range {s}-{e}')
        else:
            return guess

def guess_checker(choice, s, e):
    guesses = 0
    while True:
        guess = ask_guess(s, e)
        if guess < choice:
            guesses += 1
            print('Higher!')
        elif guess > choice:
            guesses += 1
            print('Lower!')
        elif guess == choice:
            guesses += 1
            return guesses

     

def main():
    while True:
        print("Give me a starting and ending number, I'll choose a number between them, then you're going to have to guess it.\nI'll help you by telling you if your guess is higher or lower than my number.")
        s, e = ask_range()
        choice = choice_generator(s, e)
        guesses = guess_checker(choice, s, e)
        print(f'You did it! My number was {choice}!\nIt took you exactly {guesses} guesses!')
        while True:
            user_again = input('Do you want to play again? (y/n): ').lower().strip()
            if user_again == 'y':
                print('Playing again!')
                break
            elif user_again == 'n':
                return
if __name__ == '__main__':
    main()
