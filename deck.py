from random import shuffle

class Deck(object):
    def __init__(self):
        # ранги
        ranks = "23456789TJQKA"
        # масті
        suits = "DCHS"
        # генератор списків, що створює колоду з 52 карт.
        self.cards = [Card(r, s) for r in ranks for s in suits]
        # перетасовуємо колоду. Не забудьте імпортувати функцію shuffle із модуля random
        shuffle(self.cards)


    def deal_card(self):
        "Функція здачі карти"
        return self.cards.pop()
    







    
