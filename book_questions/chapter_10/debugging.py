import logging
import random
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


guess = ''
toss = ' '
while guess != toss:
    guess = input('\nGuess the coin toss! Enter heads or tails:\n')
    toss = random.randint(0, 1) # 0 é coroa (tails), 1 é cara (heads)
    toss = {0: 'tails', 1:'heads'}[toss]
    logging.debug('toss: %s' % toss)
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')

    guess = input('Gues the coin toss! Enter heads or tails:\n')

    logging.debug('toss: %s' % toss)
    logging.debug('guess: %s' % guess)

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')