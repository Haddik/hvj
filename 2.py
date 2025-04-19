import random

def dealer_plays(d_hand):
    while sum(d_hand) < 17:
        d_hand.append(grab_card())
    return d_hand

def check_winner(p_total, d_total):
    if p_total > 21: return "ты проиграл"
    if d_total > 21: return "ты выиграл"
    if p_total == d_total: return "ничья"
    return "ты выиграл" if p_total > d_total else "ты проиграл"

def show_cards(p_hand, d_hand, reveal=False):
    print(f"\nYour hand: {p_hand} = {sum(p_hand)}")
    print(f"Dealer shows: {d_hand[0]}" if not reveal else f"Dealer's hand: {d_hand} = {sum(d_hand)}")

def grab_card():
    return random.choice([2,3,4,5,6,7,8,9,10,10,10,11])

def play_round():
    player = [grab_card(), grab_card()]
    dealer = [grab_card(), grab_card()]

    while sum(player) <= 21:
        show_cards(player, dealer)
        if input("Hit? (y/n): ").lower() != 'y':
            break
        player.append(grab_card())

    dealer = dealer_plays(dealer)
    show_cards(player, dealer, True)
    print(check_winner(sum(player), sum(dealer)))

print("приветствую тебя в игре 21 ")
while input("\nPlay again? (y/n): ").lower() == 'y':
    play_round()
print("пока)")