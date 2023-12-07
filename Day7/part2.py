def best_joker_transformation(hand):
    cards =['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if hand.count('J') == 0:
        return hand
    jokerHands = []
    for card in cards:
        jokerHands.append(hand.replace('J', card))
    strongest = 0
    id = None
    for i, jokerHand in enumerate(jokerHands):
        if get_hand_combo_str(jokerHand) >= strongest:
            strongest = get_hand_combo_str(jokerHand)
            id = i
    if strongest == 0:
        return hand
    return jokerHands[id]
    

def get_hand_combo_str(hand):
    for card in hand:
        if hand.count(card) == 5: # Five of a kind
            return 6
        if hand.count(card) == 4: # Four of a kind
            return 5
        if hand.count(card) == 3: # Full house
            for crd in hand:
                if hand.count(crd) == 2:
                    return 4
        elif hand.count(card) == 2: # Full house
            for crd in hand:
                if hand.count(crd) == 3:
                    return 4
        if hand.count(card) == 3: # Three of a kind
            for crd in hand:
                if hand.count(crd) == 1:
                    return 3
        if hand.count(card) == 2: # Two pair
            for crd in hand:
                if hand.count(crd) == 2 and crd != card:
                    return 2
        if hand.count(card) == 2: # One pair
            return 1
    return 0 # High card
        

def is_hand2_stronger(hand1, hand2):
    cardStrenght =['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    jokerHand1 = best_joker_transformation(hand1)
    jokerHand2 = best_joker_transformation(hand2)
    hand1ComboStr = get_hand_combo_str(jokerHand1)
    hand2ComboStr = get_hand_combo_str(jokerHand2)
    if hand1ComboStr < hand2ComboStr:
        return True
    if hand1ComboStr == hand2ComboStr:
        for i in range(len(hand1)):
            if cardStrenght.index(hand1[i]) == cardStrenght.index(hand2[i]):
                continue
            if cardStrenght.index(hand1[i]) > cardStrenght.index(hand2[i]):
                return True
            else:
                return False
    return False


def sort_hands(hands):
    isSorted = True
    for i in range(0, len(hands)):
        if i + 2 > len(hands):
            break
        hand1 = hands[i][0]
        hand2 = hands[i + 1][0]
        if is_hand2_stronger(hand1, hand2):
            temp = hands[i]
            hands[i] = hands[i + 1]
            hands[i + 1] = temp
            isSorted = False
    if not isSorted:
        sort_hands(hands)
    return hands
    
    
def main():
    with open('Day7/input.txt') as file:
        lines = file.readlines()
    hands = [line.split() for line in lines]
    sortedHands = sort_hands(hands)
    sortedHands.reverse()
    answer = 0
    for i, sortedHand in enumerate(sortedHands):
        answer += int(sortedHand[1]) * (i + 1)
    print(answer)
    
    
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(1500) # Default 1000 was not enough
    main()