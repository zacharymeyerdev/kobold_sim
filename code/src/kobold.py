# Modified kobold.py to account for the 5 kobold tribes

class Kobold:
    def __init__(self, kobold_type, skills, health, tribe, tribe_affinity):
        """
        Initialize a new kobold character with tribal affinity.

        :param kobold_type: str - The type of kobold (e.g., 'Miner', 'Warrior', 'Shaman', etc.).
        :param skills: dict - Specific skills and abilities the kobold has.
        :param health: int - Health level of the kobold.
        :param tribe: str - The tribe to which the kobold belongs.
        :param tribe_affinity: str - The specific affinity of the kobold's tribe (e.g., 'Flameclaw', 'Tunnelshade', etc.).
        """
        self.kobold_type = kobold_type
        self.skills = skills
        self.health = health
        self.tribe = tribe
        self.tribe_affinity = tribe_affinity

    def perform_task(self, task):
        """
        Perform a specific task based on the kobold's type, skills, and tribal affinity.

        :param task: str - The task to be performed.
        """
        # Implement task logic based on kobold type, skills, and tribal affinity
        pass

    def take_damage(self, damage):
        """
        Reduce the health of the kobold when taking damage.

        :param damage: int - The amount of damage taken.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Prevent negative health
            # Optional: Implement logic for when a kobold's health reaches 0

    def heal(self, amount):
        """
        Heal the kobold by a certain amount.

        :param amount: int - The amount of health to restore.
        """
        self.health += amount
        # Optional: Implement maximum health cap

    # Additional methods related to kobold functionality can be added here,
    # such as upgrading skills, interacting with other kobolds, etc., based on tribal affinity.

# This enhanced implementation accounts for the unique characteristics and abilities 
# associated with each kobold's tribe, adding depth to their roles and actions in the game.