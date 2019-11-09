import random


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name, self.price, self.weight, self.flammability, self.identifier = name, price, weight, flammability, identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            print('Not so stealable...')
        elif ratio >= 0.5 and ratio < 1:
            print('Kinda stealable.')
        else:
            print('Very stealable!')

    def explode(self):
        product = self.flammability * self.weight
        if product < 10:
            print('...fizzle.')
        elif product >= 10 and product < 50:
            print('...boom!')
        else:
            print('...BABOOM!!')


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name, self.price, self.weight, self.flammability, self.identifier = name, price, weight, flammability, identifier

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif self.weight >= 5 and self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')
