'''
@author : Dibyendu Das
This module contains the decision logics of the computer players
'''
import random
    
# def random_card_select(cpu_player):
#     if len(cpu_player.parent.previous_turn_cards) == 0:                     # Check to see if it is the first player
#         choice = random.choice(cpu_player.hand)
#     else:
#         suit = cpu_player.parent.previous_turn_cards[0].suit
#         suit_cards = [card for card in cpu_player.hand if card.suit == suit]
#         trump_cards = [card for card in cpu_player.hand if card.suit == cpu_player.parent.trump]
#         if len(suit_cards) > 0:                                             # If it has cards of the played suit
#             choice = random.choice(suit_cards)
#         elif cpu_player.parent.trump_shown:                                 # If trump is shown, it'll play trump
#             if len(trump_cards) > 0:
#                 choice = random.choice(trump_cards)
#             else:                                                           # If no trump selects a random card
#                 choice = random.choice(cpu_player.hand)
#         else:
#             cpu_player.parent.trump_shown = True                            # If trump not shown, will show it
#             print "Trump revealed! It is :", cpu_player.parent.trump
#             if len(trump_cards) > 0:
#                 choice = random.choice(trump_cards)
#             else:
#                 choice = random.choice(cpu_player.hand)
#     cpu_player.hand.remove(choice)
#     cpu_player.parent.previous_turn_cards.append(choice)


    
def random_card_select(player, turn_cards):
    ''' A simple card selection algorithm for the AI
    If a suit card is present plays a random, else plays a random of any suit.'''
    if len(turn_cards) == 0:            # if first player, selects a random card
        print 'first player'
        return player.hand.pop(random.choice(xrange(len(player.hand))))
    else:                               # if not first player
        suit = turn_cards[0].suit
        suit_cards = [card for card in player.hand if card.suit is suit]
        if len(suit_cards) != 0:    # if there is some suit card presents, selects it
            print 'suit card present'
            choice = random.choice(suit_cards)
            player.hand.remove(choice)
            return choice
        else:                           # if not suit card present, selects a random card
            print 'random choice!'
            return player.hand.pop(random.choice(xrange(len(player.hand))))
    