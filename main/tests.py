from django.test import TestCase
from main.models import Item


class mainTest(TestCase):
    def setUp(self):
        Item.objects.create(name="Good day", amount="8", description="Funtastic Mocaccino Coffee", price=11000, category="Beverage")
        Item.objects.create(name="Fanta", amount=7, description="Orange flavoured", price=9000, category="Beverage")

    def test_item_is_in_stock(self):
        """Items in vending machine that correctly identified"""
        good_day = Item.objects.get(name="Good day")
        fanta = Item.objects.get(name="Fanta")
        self.assertEqual(good_day.description, "Funtastic Mocaccino Coffee")
        self.assertEqual(fanta.amount, 7)