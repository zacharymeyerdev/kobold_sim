# event_system.py

class Event:
    def __init__(self, name, description, effects, duration):
        """
        Initialize a new event.

        :param name: str - The name of the event.
        :param description: str - A brief description of the event.
        :param effects: dict - The effects of the event on the tribe or kobolds.
        :param duration: int - The number of game cycles the event lasts.
        """
        self.name = name
        self.description = description
        self.effects = effects
        self.duration = duration

    def apply_effects(self, tribe):
        """
        Apply the effects of the event to the given tribe.

        :param tribe: Tribe - The tribe affected by the event.
        """
        # Implement the logic to apply event effects
        # Example: Change in resources, impact on kobold health, etc.
        pass

    def is_active(self):
        """
        Check if the event is still active.

        :return: bool - True if the event is still active, False otherwise.
        """
        return self.duration > 0

    def update(self):
        """
        Update the event status each game cycle.
        """
        if self.duration > 0:
            self.duration -= 1
        # Additional logic can be added here if needed

class EventSystem:
    def __init__(self):
        """
        Initialize the event system.
        """
        self.active_events = []

    def trigger_event(self, event, tribe):
        """
        Trigger a new event and apply its effects.

        :param event: Event - The event to be triggered.
        :param tribe: Tribe - The tribe affected by the event.
        """
        self.active_events.append(event)
        event.apply_effects(tribe)

    def update_events(self, tribe):
        """
        Update all active events and their effects on the tribe.

        :param tribe: Tribe - The tribe affected by the events.
        """
        for event in self.active_events:
            if event.is_active():
                event.apply_effects(tribe)
            else:
                self.active_events.remove(event)

# This system provides a basic framework for managing events within the game, 
# which can be expanded to include a variety of dynamic scenarios affecting the kobold colony.