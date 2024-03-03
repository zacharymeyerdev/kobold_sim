# building.py

# This module would define the buildings in your colony game.
# Each building could have attributes like cost, resource production/consumption, etc.

class Building:
    def __init__(self, name, cost, production_rate, consumption_rate):
        """
        Initialize a new building.

        :param name: str - The name of the building.
        :param cost: dict - The cost to build this building, in resources.
        :param production_rate: dict - The rate of resource production per cycle.
        :param consumption_rate: dict - The rate of resource consumption per cycle.
        """
        self.name = name
        self.cost = cost
        self.production_rate = production_rate
        self.consumption_rate = consumption_rate

    def produce_resources(self):
        """
        Produce resources at the building's production rate.
        This method would be called every game cycle to update resources.
        """
        # Logic to produce resources
        pass

    def consume_resources(self):
        """
        Consume resources at the building's consumption rate.
        This method would be called every game cycle to update resources.
        """
        # Logic to consume resources
        pass

    # Additional methods can be added here for building functionality.
    # For example, upgrade_building(), repair_building(), etc.

# You can also define specific building types by inheriting from the Building class.
# class Farm(Building):
#     def __init__(self, ...):
#         super().__init__(...)
#         # Additional attributes or methods specific to Farm

# class Factory(Building):
#     def __init__(self, ...):
#         super().__init__(...)
#         # Additional attributes or methods specific to Factory

# This modular approach allows for easy expansion and customization of different building types.
