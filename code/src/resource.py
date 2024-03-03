# resource.py

# This module defines the resources in your colony game.
# Resources could include food, wood, stone, etc., and their management.

class Resource:
    def __init__(self, name, quantity=0):
        """
        Initialize a new resource.

        :param name: str - The name of the resource.
        :param quantity: int - The initial quantity of the resource.
        """
        self.name = name
        self.quantity = quantity

    def add(self, amount):
        """
        Add a certain amount to the resource.

        :param amount: int - The amount to add to the resource.
        """
        self.quantity += amount

    def subtract(self, amount):
        """
        Subtract a certain amount from the resource.

        :param amount: int - The amount to subtract from the resource.
        """
        self.quantity -= amount
        if self.quantity < 0:
            self.quantity = 0  # Prevent negative resources

    def set_quantity(self, amount):
        """
        Set the resource quantity to a specific amount.

        :param amount: int - The new amount for the resource.
        """
        self.quantity = amount if amount >= 0 else 0

# You can expand this class with more functionalities as needed,
# such as resource expiration, resource type specific attributes, etc.
