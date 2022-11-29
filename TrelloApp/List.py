class List:
    def __init__(self, name):
        self.id = name
        self.name = name
        self.cards = {}

    # generic attributes update
    def updateName(self, newName):
        self.name = newName

    # card in by moving or adding
    def addCard(self, card):
        cardId = card.id
        if (cardId in self.cards):
            print("card already exists in list")
        else:
            self.cards[cardId] = 1

    # card removed either by del or moving
    def removeCard(self, cardId):
        if (cardId not in self.cards):
            print("Card does not exist in List")
        else:
            del self.cards[cardId]