class Game:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.categories = []
    

    def add_category(self, category):
        self.categories.append(category)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
    
    def get_categories(self):
        return self.categories
    
    def is_in_category(self, category):
        for cat in self.categories:
            if cat == category:
                return True
        return False
    

class Catalog:

    def __init__(self, games):
        self.games = games

    def add_game(self, game):
        self.games.append(game)

    def filter_catalog_by_name(self, name):
        return [game for game in self.games if name in game.get_name()]
    
    def filter_catalog_by_price(self, price):
        filtered = []
        for game in self.games:
            if game.price == price:
                filtered.append(game)

    def filter_catalog_by_category(self, category):
        filtered = []
        for game in self.games:
            if game.is_in_category(category):
                filtered.append(game)
        return filtered


class Sale:

    def __init__(self, games, customer):
        self.games = games
        self.customer = customer

    def add_game(self, game):
        self.games.append(game)

    def close_sale(self):
        total = 0
        quantity = self.games.__len__() #len(self.games)
        discount = 0
        for game in self.games:
            total += game.get_price()
        if quantity > 7:
            discount += 0.2
        if total > 500:
            discount += 0.4
        self.subtotal = total
        self.discount = total * discount
        self.total = self.subtotal - self.discount




game = Game('God of War', 599.99)
game.add_category('Adventure')
catalog = Catalog([game])
print(catalog.filter_catalog_by_category('Adventure'))
sale = Sale([game], 'Eduardo Flores')
sale.close_sale()
print(f'subtotal: {sale.subtotal}')
print(f'discount: {sale.discount}')
print(f'total: {sale.total}')
