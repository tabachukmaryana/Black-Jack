class Hand(object):
    def __init__(self, name):
        # Ім'я гравця
        self.name = name
        # Спочатку рука порожня
        self.cards = []


    def add_card(self, card):
        """Додає карту на руку"""
        self.cards.append(card)



    def get_value(self):
        """Метод отримання числа очок на руці"""
        result = 0
        # Кількість тузів на руці.
        aces = 0
        for card in self.cards:
            result += card.card_value()
            # Якщо на руці є туз - збільшуємо кількість тузів
            if card.get_rank() == "A":
                aces += 1
        # Вирішуємо рахувати тузи за 1 очко або за 11
        if result + aces * 10 <= 21:
            result += aces * 10
        return result


    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text
    