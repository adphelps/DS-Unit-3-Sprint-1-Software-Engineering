import unittest
from acme import Product
from acme_report import generate_products, adjectives, nouns


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default weight price being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explode(self):
        """Test functionality of explode() and stealability() methods."""
        prod = Product('Big Bertha', price=50, weight=100, flammability=2.5)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Test for Acme product generation."""

    def test_default_num_products(self):
        """Checking default number of products is 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Checking that all products generated have valid names"""
        for product in generate_products():
            adjective, noun = product.name.split()
            self.assertIn(adjective, adjectives)
            self.assertIn(noun, nouns)
            self.assertIn(' ', product.name)


if __name__ == '__main__':
    unittest.main()
