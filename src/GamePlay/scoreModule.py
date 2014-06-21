'''
Created on Jun 11, 2014
@author: Dibyendu
'''

def ScoreHand(playersObject):
    # This method scores a hand and decides the winning team after it has been played.
    score = 0
    priority = 0
    trumpPriority = 0
    trumpFlag = False
    suit = playersObject.previousTurn[0].suit
    if playersObject.trumpShown:
        for card, player in zip(playersObject.previousTurn, playersObject.players):
            if card.suit == playersObject.trump and card.priority > trumpPriority:
                winner = player
                trumpPriority = card.priority
                trumpFlag = True
            elif card.suit == suit and card.priority > priority and trumpFlag == False:
                winner = player
                priority = card.priority
            score += card.value
    else:
        for card, player in zip(playersObject.previousTurn, playersObject.players):
            if card.suit == suit and card.priority > priority:
                winner = player
                priority = card.priority
            score += card.value
    if winner in playersObject.team1: playersObject.team1[2] += score
    else: playersObject.team2[2] += score
    
        