# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
# [f"{key}: {value}" for key, value in location.items()]

    def __str__(self):
        # printed_items = 
        return f'{self.name}\n\n{self.description}\n\n{"".join(str(item) for item in self.items)}'