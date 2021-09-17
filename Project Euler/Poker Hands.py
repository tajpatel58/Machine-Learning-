
with open('p054_poker.txt', 'r') as f:
    player_hands = []
    for line in f:
        player_hands.append(line)


def poker(hand):
    val_in_hand = []  # Array to store the values of the cards. Clearly needed.
    useful_hand = []  # Array to store the useful cards in our hand, useful for comparing hands.
    for i in hand:
        val_in_hand += list(i)
    array = [1, 2, 3, 4, 5]
    for j in array:
        del val_in_hand[j]
    num_of_pairs = 0
    three_of_a_kind = 0  # Three of a kind is reassigned if we have a 3 of a kind and assigned the value of the card.
    four_of_a_kind = 0  # Indicator of if we have a four of a kind of not.
    for x in range(0, 5):
        try:  # Here we need a try block as if we have a 'K' for example then we clearly can't change to an integer.
            val_in_hand[x] = int(val_in_hand[x])
        except:  # In the event we have a 10,King,Queen,Ace, we assign ascending values.
            if val_in_hand[x] == 'T':
                val_in_hand[x] = 10
            elif val_in_hand[x] == 'J':
                val_in_hand[x] = 11
            elif val_in_hand[x] == 'Q':
                val_in_hand[x] = 12
            elif val_in_hand[x] == 'K':
                val_in_hand[x] = 13
            else:
                val_in_hand[x] = 14
    set_of_hand = set(val_in_hand)  # For each different value we need to count how many times that card appears.
    # The following checks if we have pairs, 3ofK, 4ofK.
    for i in set_of_hand:
        card = i
        num_of_instances = val_in_hand.count(card)
        if num_of_instances == 2:
            num_of_pairs += 1
            useful_hand.append(card)  # Again we store the useful cards in our hand.
        elif num_of_instances == 3:
            three_of_a_kind = card
            useful_hand.append(card)
        elif num_of_instances == 4:
            four_of_a_kind = 1
            useful_hand.append(card)
        else:
            continue
    useful_hand = [int(n) for n in useful_hand]
    unrefined_hand = []
    flush = 0  # Have an indicator for flush.
    suits_in_hand = []  # An Array to hold suits of the cards, to indicate if we have a flush or not.
    suits = ['C', 'H', 'S', 'D']
    for i in hand:
        unrefined_hand += list(i)
    for j in range(0, len(unrefined_hand)):
        if unrefined_hand[j] in suits:
            suits_in_hand.append(unrefined_hand[j])
        else:
            continue
    for j in suits:
        num_of_occurance = suits_in_hand.count(j)  # We the number of times a suit appears is 5 then we have a flush.
        if num_of_occurance == 5:
            flush = 1
        else:
            continue
    val_in_hand.sort()  # Sort the values so it's easier to compare hands and to check if we have a straight or not.
    indicator_of_straight = 0
    for x in range(1, 5):  # Check if difference between each value is 1.
        if val_in_hand[x] - val_in_hand[x-1] == 1:
            indicator_of_straight += 1
        else:
            break
    # The Following determines what hand we have. We associate a value to the ranking of hands. eg Royal Flush = 10.
    if indicator_of_straight == 4 and flush == 1 and val_in_hand[4] == 14:
        return 10, max(useful_hand)
    elif indicator_of_straight == 4 and flush == 1:
        return 9, val_in_hand[4]
    elif four_of_a_kind == 1:
        return 8, max(useful_hand)
    elif three_of_a_kind != 0 and num_of_pairs == 1:
        return 7, three_of_a_kind  # We return three of a kind as this denotes the card value that we have 3 of.
    elif flush == 1:
        return 6, val_in_hand[4]
    elif indicator_of_straight == 4:
        return 5, val_in_hand[4]
    elif three_of_a_kind != 0:
        return 4, three_of_a_kind
    elif num_of_pairs == 2:
        return 3, max(useful_hand)
    elif num_of_pairs == 1:
        return 2, max(useful_hand)
    else:
        return 1, val_in_hand[4]


def winner(a, b):
    outcome_1 = poker(a)
    outcome_2 = poker(b)
    if outcome_1[0] > outcome_2[0]:
        return 1
    elif outcome_1[0] < outcome_2[0]:
        return 2
    else:
        if outcome_1[1] > outcome_2[1]:
            return 1
        else:
            return 2


# Our hands array is 10 cards, first 5 is player 1, second 5 is player 2.
# E.g = ['10H 9H 6K 7S 9D 8H 3C 4S JS KD'] . We return the players hands seperately.
def hand_splitter(hands):
    hands = list(hands)
    player_1 = []
    player_2 = []
    player1_indexes = [0, 3, 6, 9, 12]
    # player2_indexes = [15, 18, 21, 24, 27], We won't use this as this array is just adding 15 to player1_indexes.
    for j in player1_indexes:
        player_1_card = ''.join([hands[j], hands[j+1]])
        player_2_card = ''.join([hands[j+15], hands[j+16]])
        player_1.append(player_1_card)
        player_2.append(player_2_card)

    return player_1, player_2


def number_of_times_1_wins(poker_hands):
    counter = 0
    for i in range(0, len(poker_hands)):
        hands_i = poker_hands[i]
        player_1_hand = hand_splitter(hands_i)[0]
        player_2_hand = hand_splitter(hands_i)[1]
        if winner(player_1_hand, player_2_hand) == 1:
            counter += 1
        else:
            continue
    return counter


print(number_of_times_1_wins(player_hands))
