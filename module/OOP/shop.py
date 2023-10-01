class Shop:
    shoopping = 'jamuna'
    def __init__(self,name) -> None:
        self.name = name
        self.card = [] # cart is an instance attribute

    def add_to_card(self,item):
        self.card.append(item)

mahjabin = Shop("mah")
mahjabin.add_to_card("shoes")
mahjabin.add_to_card('watch')
print(mahjabin.card)