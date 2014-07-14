'''
Created on Jun 11, 2014
@author: Dibyendu
'''

def ScoreHand(game_manager_object):
    # This method scores a hand and updates the scores of each team.
    score, priority, trumpPriority, trumpFlag = 0, 0, 0, False
    suit = game_manager_object.previous_turn_cards[0].suit
    if game_manager_object.trump_shown:
        for card, player in zip(game_manager_object.previous_turn_cards, game_manager_object.players):
            if card.suit == game_manager_object.trump and card.priority > trumpPriority:
                winner = player
                trumpPriority = card.priority
                trumpFlag = True
            elif card.suit == suit and card.priority > priority and trumpFlag == False:
                winner = player
                priority = card.priority
            score += card.value
    else:
        for card, player in zip(game_manager_object.previous_turn_cards, game_manager_object.players):
            if card.suit == suit and card.priority > priority:
                winner = player
                priority = card.priority
            score += card.value
    if winner in game_manager_object.team1: game_manager_object.team1[2] += score
    else: game_manager_object.team2[2] += score
    
        