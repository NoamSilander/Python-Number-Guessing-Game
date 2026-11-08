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
    

def main():
    print("Give me a starting and ending number, I'll choose a number between them, then you're going to have to guess it.\nI'll help you by telling you if your guess is higher or lower than my number.")
    s, e = ask_range()
    choice = choice_generator(s, e)

main()
