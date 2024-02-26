class Player():
    def __init__(self, name: str) -> None:
        self.name = name

class Room():
    def __init__(self, name: str, description: str, contents: list = []) -> None:
        self.name = name
        self.description = description
        self.contents = contents

class Item():
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

# Set up rooms
tavern = Room('Tavern', 'It is dark and smoky, with tables packed around a small fireplace.')

# Set up items
dagger = Item('Dagger', 'It is a long dagger, but doesn\'t look very sharp.')

# Put items in rooms
tavern.contents.append(dagger)

# Make a dict to hold players
players = {}

def handle_message(message: str, id: str):
    if id not in players:
        

    if message.lower().startswith('look'):
        currentRoom = tavern
        response = f"You are in {currentRoom.name}. {currentRoom.description}."

    return response
