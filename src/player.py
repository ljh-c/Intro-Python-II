# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, items=[]):
        self.name = name
        self.location = location
        self.items = items

    def __str__(self):
        return f'\n{self.__class__.__name__} {self.name} <{", ".join(item.name for item in self.items)}>\
            location: {self.location}'
    
    def print_inventory(self):
        print(f'{"".join(str(item) for item in self.items)}' if len(self.items) > 0 else "You aren't carrying anything.")
        return

    def get(self, item):
        self.items.append(item)
        return
    
    def drop(self,item):
        self.items.remove(item)
        return