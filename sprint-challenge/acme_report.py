from acme import Product
from random import randint, sample, uniform

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(n_products=30):
    products = []
    for _ in range(n_products):
        name = sample(adjectives, 1)[0] + ' ' + sample(nouns, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price=price,
                                weight=weight, flammability=flammability))
    return products


def inventory_report(products):
    product_names = []
    product_prices = []
    product_weights = []
    product_flammabilities = []
    for product in products:
        if product.name not in product_names:
            product_names.append(product.name)
        product_prices.append(product.price)
        product_weights.append(product.weight)
        product_flammabilities.append(product.flammability)
    avg_price = sum(product_prices) / len(product_prices)
    avg_weight = sum(product_weights) / len(product_weights)
    avg_flammability = sum(product_flammabilities) / \
        len(product_flammabilities)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(product_names))
    print('Average price: ', avg_price)
    print('Average weight: ', avg_weight)
    print('Average flammability: ', avg_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
