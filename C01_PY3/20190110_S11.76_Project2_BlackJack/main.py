from random import shuffle


def check_value(card_list):
    value_corresp = {"2": 2, "3": 3, "4": 4,
                     "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                     "10": 10, "J": 10, "Q": 10, "K": 10}

    ace_counter = 0
    sum1 = 0

    while "A" in card_list:
        card_list.pop("A")
        ace_counter += 1

    for card in card_list:
        if "A" not in card:
            sum1 += value_corresp.get(card[0])
        else:
            ace_counter += 1

    if ace_counter == 1:
        if sum1 + 11 <= 21:
            sum1 += 11
        else:
            sum1 += 11
    elif ace_counter == 2:
        if sum1 + 12 <= 21:
            sum1 += 12
        else:
            sum1 += 2
    elif ace_counter == 3:
        if sum1 + 11 <= 21:
            sum1 += 13
        else:
            sum1 += 3
    elif ace_counter == 4:
        if sum1 + 14 <= 21:
            sum1 += 14
        else:
            sum1 += 4

    return sum1


def hand_status(hand, hand_value):
    if hand_value > 21:
        finish_cond = True
        print(f"Dude, you bulked with {hand_value} , shame on you!!!!")

    elif hand_value == 21:
        finish_cond = True
        print(f"Your hand is: {hand}, with a total value of {hand_value}\n")

    else:
        print(f"Your hand is: {hand}, with a total value of {hand_value}\n")

        keep_drawing1 = input("Draw? (Y/N): \n")
        if keep_drawing1 == "N":
            finish_cond = True
        else:
            finish_cond = False

    return finish_cond


def contin():
    aux_var = input("You finished your game, do you want to keep on going? (Y/N)")
    if aux_var == "Y":
        finish = False
    else:
        finish = True
    return finish


class Player:
    def __init__(self, money):
        self.hand = []
        self.money = money
        self.hand_v = 0

    def bet(self):
        bet1 = input("How much does the player bet: ")
        self.money -= int(bet1)
        return bet1

    def win(self, bet1):
        self.money += 2 * int(bet1)


class Mazo:
    def __init__(self):
        self.cards = []

    def brand_new(self):
        suits = ["Diamonds", "Hearts", "Spades", "Clubs"]
        # suits = [("Diamonds", "Red"), ("Hearts", "Red"), ("Spades", "Black"), ("Clubs", "Black")]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append((value, suit))
        # for (suit, color) in suits:
        #    for value in values:
        #        self.cards.append((value, suit, color))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self, player_hand):
        player_hand.append(self.cards.pop(0))
        return player_hand


# print(baraja1.cards)


finished = False

player1 = Player(5000)
dealer = Player(1000000)

while not finished:
    for i in range(1, 100):
        print("")

    # New deck is initialized

    baraja1 = Mazo()
    baraja1.brand_new()
    shuffle(baraja1.cards)

    player1.hand = []
    dealer.hand = []

    # Player places a bet
    bet = player1.bet()

    # First cards are drawn
    baraja1.draw(player1.hand)
    baraja1.draw(player1.hand)

    player1.hand_v = check_value(player1.hand)
    baraja1.draw(dealer.hand)
    dealer.hand_v = check_value(dealer.hand)

    # We show cards in the game
    print(f"Your hand is: {player1.hand}, with a total value of {player1.hand_v} \n")
    print(f"Dealer's hand is: {dealer.hand}, with a total value of {dealer.hand_v} \n ")

    # The player must decide if wants to keep the hand or draw more
    if player1.hand_v != 21:
        keep_drawing = input("Do you want to hit another card?  (Y/N): \n")
        if keep_drawing == "Y":
            finish_condition = False
        else:
            finish_condition = True

        # The player decided to draw more
        while finish_condition is False:
            baraja1.draw(player1.hand)
            player1.hand_v = check_value(player1.hand)
            finish_condition = hand_status(player1.hand, player1.hand_v)

        # Check if the player bulked
        if player1.hand_v > 21:
            print(f"Player balance is {player1.money}")
            input("Press ENTER to keep on going")
            finished = contin()
            continue

    # The player stands, now the dealer has to surpass him
    finish_condition = False
    while dealer.hand_v < player1.hand_v and not dealer.hand_v > 21:
        baraja1.draw(dealer.hand)
        dealer.hand_v = check_value(dealer.hand)

    print(f"Dealer's hand is: {dealer.hand}\n")
    print(f"Dealer got: {dealer.hand_v}, You got: {player1.hand_v}")
    # Check who won
    if dealer.hand_v > 21:
        print("Player wins the game")
        player1.win(bet)
        finished = contin()
        print(f"Player balance is {player1.money}")
        input("Press ENTER to keep on going")
        continue

    else:

        print("Player looses the game")
        finished = contin()
        print(f"Player balance is {player1.money}")
        input("Press ENTER to keep on going")
        continue

# Its the time for the dealer to keep on drawing
