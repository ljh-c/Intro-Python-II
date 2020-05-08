# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def remove_item(self, item):
        self.items.remove(item)
        return

    def store_item(self,item):
        self.items.append(item)
        return

    def __str__(self):
        return f'{self.name}\n\n{self.description}\n\n{"".join(str(item) for item in self.items)}'