def new_game():
    # створюємо колоду
    d = Deck()
    # задаємо "руки" для гравця та дилера
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    # здаємо дві карти гравцю
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    # здаємо одну картку дилеру
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print(player_hand)
    # Прапор перевірки необхідності продовжувати гру
    in_game = True
    # набирати карти гравцеві має сенс тільки якщо у нього на руці менше 21 очка
    while player_hand.get_value() < 21:
        ans = input("Hit or stand? (h/s) ")
        if ans == "h":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            # Якщо у гравця перебір - дилеру немає сенсу набирати карти
            if player_hand.get_value() > 21:
                print("You lose")
                in_game = False
        else:
            print("You stand!")
            break
    print("=" * 20)
    if in_game:
        # За правилами дилер зобов'язаний набирати картки доки його рахунок менше 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            # Якщо у дилера перебір грати далі немає сенсу – гравець виграв
            if dealer_hand.get_value() > 21:
                print("Dealer bust")
                in_game = False
    if in_game:
        # Ні в кого не було перебору – порівнюємо кількість очок у гравця та дилера.
        # У нашій версії якщо у дилера та гравця рівна кількість очок - виграє казино
        if player_hand.get_value() > dealer_hand.get_value():
            print("You win")
        else:
            print("Dealer win")
