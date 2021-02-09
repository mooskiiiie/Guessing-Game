secret_word = 'giraffe'
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print('Welcome to a guessing game!')
print('The hint is "an animal that has a long neck"')

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter your guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses == True:
    print('You lost all your guesses')
else:
    print('You win!')
    
