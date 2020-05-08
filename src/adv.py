from room import Room
from player import Player
from item import Item

# Define all items

item = {
    'lantern': Item('lantern', 'A rusted lantern, crudely wrought ages ago.'),

    'sword': Item('sword', 'A blunt wooden sword, more a hefty branch than \
a weapon.'),

    'spear': Item('spear', 'A tarnished grunt spear, long-abandoned by a \
deserter.'),

    'bread': Item('bread', 'Stale bread that has the texture of a rock, and \
tastes like one too.'),

    'tonic': Item('tonic', 'An invigorating herbal extract stored in a \
clouded vial.'),

    'horn': Item('horn', 'A horn carved into the shape of a dragon, covered \
in worn runes.')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['lantern']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item['sword'], item['bread']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item['spear'], item['tonic']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item['horn']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('What is your name? '), room['outside'])

# Clear screen
print('\x1bc')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def skip():
    print('Not a valid command.')

while True:
    print(f"\t{player}")

    command = input('Enter "n", "s", "e", "w" to move north, south, east, \
or west. "q" or "quit" to quit\n\n')

    if command == 'q' or command == 'quit':
        print('Thanks for playing')
        break
    
    elif command == 'i':
        player.print_inventory()

    elif command in ['n', 's', 'e', 'w']:
        # Error handling if user tries to go to a non-existent room
        try:
            player.location = getattr(player.location, f'{command}_to')
        except AttributeError:
            print("There's nowhere to go in that direction.")

    elif len(command.split(' ')) > 1:
        action, item_name = command.split(' ')

        if action == 'get' or action == 'take':
            if item_name not in item or item[item_name] not in getattr(player.location, 'items'):
                print("You can't take it with you. Because that item isn't here.")
            else:
                picked_up_item = item[item_name]
                player.location.remove_item(picked_up_item)
                player.get(picked_up_item)
                picked_up_item.on_take()
        
        if action == 'drop':
            if item_name not in item or item[item_name] not in getattr(player, 'items'):
                print("You can't lose what you don't have. Because you're not carrying that item.")
            else:
                dropped_item = item[item_name]
                player.drop(dropped_item)
                player.location.store_item(dropped_item)
                dropped_item.on_drop()

    # if len(command.split(' ')) > 1 and (command.split(' ')[0] == 'get' or command.split(' ')[0] == 'take'):
    #     if command.split(' ')[1] not in item or item[command.split(' ')[1]] not in getattr(player.location, 'items'):
    #         print("You can't take it with you. Because that item isn't here.")
    #     else:
    #         picked_up_item = item[command.split(' ')[1]]
    #         player.location.remove_item(picked_up_item)
    #         player.get(picked_up_item)
    #         picked_up_item.on_take()

    # if len(command.split(' ')) > 1 and command.split(' ')[0] == 'drop':
    #     if command.split(' ')[1] not in item or item[command.split(' ')[1]] not in getattr(player, 'items'):
    #         print("You can't lose what you don't have. Because you're not carrying that item.")
    #     else:
    #         dropped_item = item[command.split(' ')[1]]
    #         player.drop(dropped_item)
    #         player.location.store_item(dropped_item)
    #         dropped_item.on_drop()
    
    else:
        skip()