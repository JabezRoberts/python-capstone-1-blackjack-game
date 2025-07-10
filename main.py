import random
from art import logo

def deal_card():
    """This functions returns a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards (hand for a player) and returns the sum of the hand"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Game drawn!"
    elif c_score == 0:
        return "User loses"
    elif u_score == 0:
        return "Computer loses"
    elif u_score > 21:
        return "Your total is over 21. You lose."
    elif c_score > 21:
        return "The computer went over 21. You win."
    elif u_score > c_score:
        return "User wins"
    else:
        return "Computer wins"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    cpu_total = -1
    user_total = -1
    is_game_over = False

    for i in range(2):
        """Deals 2 random cards to the hands of both the player and the cpu"""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        """Allows user to continue taking cards until they choose not to"""
        user_total = calculate_score(user_cards)
        cpu_total = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score:{user_total}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_total == 0 or cpu_total == 0 or user_total > 21:
            is_game_over = True
        else:
            user_choice = input("Do you want to draw another card? Type 'yes' or 'no' to decide.\n").lower()
            if user_choice == "yes":
                user_cards.append(deal_card())
                # user_total = calculate_score(user_cards)
            elif user_choice == "no":
                is_game_over = True
            else:
                print("You made an incorrect choice. Type 'yes' or 'no' to decide.\n")


    while cpu_total != 0 and cpu_total < 17:
        """Allows the computer to take cards"""
        computer_cards.append(deal_card())
        cpu_total = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, and your final score: {user_total}")
    print(f"Computer's final hand: {computer_cards}, and its final score: {cpu_total}")
    print(compare(user_total, cpu_total))


while input("Do you want to play the game? Type y for yes and n for no: ") == "y":
    print("\n" *20)
    play_game()