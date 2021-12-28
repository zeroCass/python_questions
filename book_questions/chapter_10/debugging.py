import logging
import random
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


guess = ''
toss = ' '
toss_option = {0: 'tails', 1:'heads'}
while guess != toss:
    guess = input('\nGuess the coin toss! Enter heads or tails:\n')
    toss = toss_option[random.randint(0,1)]
    logging.debug('toss: %s' % toss)
    
    if toss == guess:
        print('You got it!')
    else:
        guess = input('Nope! Guess again!')

        logging.debug('toss: %s' % toss)
        logging.debug('guess: %s' % guess)

        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')