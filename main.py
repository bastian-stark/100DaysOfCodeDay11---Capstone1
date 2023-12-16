#Game of Blackjack - Capstone Project 1

########## Rules Of The Game ##########
# The deck is unlimited in size
# There are no jokers
# The Jack/Queen/King all count as 10
# The Ace can be used as an 11 or 1, depending on your choice
# All cards in the list have equal probability of being drawn
# Cards are not removed from the deck after being drawn

import random

def initialize_deck(deck):
    """Generates initial 2 cards for a deck"""
    newDeck1 = draw_card(deck)
    newDeck2 = draw_card(newDeck1)
    return newDeck2

def draw_card(deck):
    """Draw another card for a deck"""
    # List of possible cards in deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    deck.append(card)
    return deck

def compare_scores(score1, score2):
    """Compare scores of both decks to determine winner (1 = player1 lost; 2 = player2 lost; 3 = tied)"""
    if score1 > 21 and score2 < 21:
        return 1
    elif score1 < 21 and score2 > 21:
        return 2
    elif score1 == score2:
        return 3
    elif score1 > 21 and score2 > 21:
        return 4
    elif score1 < score2:
        return 1
    elif score1 > score2:
        return 2
    else:
        print(f'Error, score1: {score1}')
        print(f'Error, score2: {score2}')
        return 0

def determine_score(deck):
    """Calculates the current score (as close to 21 as possible) of deck"""
    # Checks for Aces in deck and changes from score of 11 to score of 1 if sum of deck is greater than 21
    if sum(deck) > 21:
        for n in range(0, len(deck)):
            if deck[n] == 11:
                deck[n] = 1
    return sum(deck)

# Begin game
startGame = input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower()
if startGame == "y":
    gameState = True
    # Begin game turn loop
    while gameState == True:
        # Creates both decks
        playerDeck = []
        pcDeck = []
        # Initialize player decks
        playerDeck = initialize_deck(playerDeck)
        pcDeck = initialize_deck(pcDeck)
        # Ask player to draw card
        drawCard = ''
        while drawCard != "n":
            print(f"Your cards: {playerDeck}, current score: {determine_score(playerDeck)}")
            print(f"Computer's first card: {pcDeck[0]}")
            drawCard = input('Type "y" to get another card, type "n" to pass: ').lower()
            if drawCard == "y":
                playerDeck = draw_card(playerDeck)
            # Determine if PC draws card
            pcDrawChoice = random.randint(0, 1)
            if pcDrawChoice == 1:
                pcDeck = draw_card(pcDeck)
        # Determine outcome of round
        playerScore = determine_score(playerDeck)
        print(f'Your score was: {playerScore}')
        pcScore = determine_score(pcDeck)
        print(f'PC score was: {pcScore}')
        outcome = compare_scores(playerScore, pcScore)
        if outcome == 1:
            print('You lose! ')
        elif outcome == 2:
            print('You win! ')
        else:
            print('Tied! ')
        # Determine if game will continue or not
        playAgain = input('Do you want to play again? ("y"/"n"): ').lower()
        if playAgain == "y":
            print('Beginning new game...')
        else:
            gameState = False
else:
    print('Goodbye...')