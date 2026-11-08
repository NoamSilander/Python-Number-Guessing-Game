import random
def choice_generator(s, e):
    choice = random.radint(s, e)
    return choice

def ask_numbers():
    while True:
        while True:
            try:
                start_number = int(input('What should be my starting number?: '))
                break
            except ValueError:
                print('Must be a whole number')
        while True:
                try:
                    end_number = int(input('What should be my ending number?: '))
                    if end_number > start_number:
                        break
                    print('Ending number must be higher than starting number')
                except ValueError:
                    print('Must be a whole number')
        while True:
            user_confirmation = input(f'My range will be {start_number}-{end_number}, are you sure? (y/n): ').lower().strip()
            if user_confirmation == 'y':
                return start_number, end_number
            elif user_confirmation == 'n':
                break
    

def main():
    print("Give me a starting and ending number, I'll choose a number between them, then you're going to have to guess it\nI'll help you by telling you if your guess is higher or lower than my number.")
    s, e = ask_numbers()
ask_numbers()