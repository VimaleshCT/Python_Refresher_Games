import random
from hangman_guess  import guess_list

guess_word = random.choice(guess_list).lower()
word_letters = len(guess_word)

game_over = False
tries = 6

from hangman_life import game_name
print(game_name)




result = []

for _ in range(word_letters):
    result += '_'
    
while not game_over:
    user_guess = input("guess a letter:")
    
    if user_guess in result:
        print(f'The letter you have guessed is {user_guess}')
        
    for pos in range(word_letters):
            letter = guess_word[pos]
            if letter == user_guess:
                result[pos] = letter
    
    if user_guess not in guess_word:
        print(f'you guessed {user_guess}, this letter is not in the word,you lose a try')
        
        
        tries -= 1
        if tries == 0:
            game_over = True
            print("GAME OVER, you Lose, try again later")
            print(guess_word)
            
         
    print(f"{' '.join(result)}")
    
    if "_" not in result:
        game_over  =True
        print("you WON,Congrats")
    
    from hangman_life import lives
    print(lives[tries])
        
    