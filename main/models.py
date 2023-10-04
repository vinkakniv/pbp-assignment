from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=0)  # Initial quantity
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=0, default=0)  # Using max_digits=12 to handle large numbers in IDR
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    BEVERAGE = "Beverage"
    SNACK = "Snack"
    CANDY = "Candy"
    CATEGORY_CHOICES = [
        (BEVERAGE, "Beverage"),
        (SNACK, "Snack"),
        (CANDY, "Candy"),
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=BEVERAGE)

    def formatted_price(self):
        # Format the price as IDR with commas for thousands separators
        return "Rp {:,}".format(self.price * self.amount)

    def __str__(self):
        return self.name
    