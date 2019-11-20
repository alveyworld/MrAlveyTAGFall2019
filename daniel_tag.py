"""
##### 0) Header #####
# Text Adventure Game
A chance to make your own Text Adventure Game.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canvas for more information.

# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""

##### 1) Author Info #####

# Change these three fields
__author__ = "20weiledanr@washk12.org"
__title__ = "A mini horror"
__description__ = "XD"

# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"


##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.
'''

Records:
    World:
        status (str): 
        map (dict[str: Location]): 
        player (Player): 

      
    Player:
        location (str): 
        inventory (list[str]):
        
        
    Location:
        about (str): 
        neighbors (list[str]): 
        stuff (list[str]): 
'''

##### 3) Core Game Functions #####
# Implement the following to create your game.

def render_introduction():
    ''' ... '''
    return ("== A MINI HORROR ==\n"+
            " = darky2889 =\n"+
            "\n"+
            "The twins invited you over to their house.\n"+
            "When you arrive to Whales Englind it was dark and cold.\n"+
            "You had a taxi drive you  over to their address.")

def create_world():
    return {
        'map': create_map(),
        'player': create_player(),
        'status': "playing"
    }

def create_player():
    return {
        'location': 'interance',
        'inventory': [],
        'health': 100
    }
def render_player(world):
    health = world['player']['health']
    inventory = world['player']['inventory']
    
    statement = "you have " + str(health) + " health. "
    if health < 50:
        statement += "You are low in health, you Need to rest. "
    return statement

def render_location(world):
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    
    return ("You are in "+location+"\n"+
            about+"\n")

def random_twin():
    pass
    
def create_map():
    return {
        'interance': {
            'neighbors': ['hallway', 'living room'],
            'about': "When you open up the door you felt like there is an Evil talking over the house.\n"+
                     "You know that you not safe",
            'stuff': ["flashlight"],
            'people': random_twin(),
        },
        'livingroom': {
            'neighbors': ['interance', 'kitchen', 'outside'],
            'about': "As you walk into the room and you look around you fell like there is something in the shadows.",
            'stuff': ["note"],
            'people': [],
        },
        'outside': {
            'neighbors': ['living room', 'woods'],
            'about': "The outside was warm but with a breeze. You feel strange. You looked around and see something, but don't know what",
            'stuff': ["sleeping drug"],
            'people': ["dragon"],
        },
        'woods': {
            'neighbors': ['outside', 'cabin'],
            'about': "The woods is a nice place to be right? as you walk deeper into the woods your body feels cold. like someone already killed you.",
            'stuff': ["wood"],
            'people': random_twin(),
        },
        'cabin': {
            'neighbors': ['woods', 'living room'],
            'about': "A cabin in the woods seems to be the best place to be, but is it?",
            'stuff': ["generator"],
            'people': random_twin(),
        },
        'living room': {
            'neighbors': ['bedroom', 'back room', 'basement'],
            'about': "As you walk into the living room things feels like death, but you don't know why.",
            'stuff': ["oil can"],
            'people': random_twin(),
        },
        'back room': {
            'neighbors': ['living room'],
            'about': "This is all the killings that happen this year. Wait... what. this is all their friends that died, and they have a X across there face. Did they kill them? What the hell is going on here.",
            'stuff': [],
            'people': [],
        },
        'bedroom': {
            'neighbors':['living room'],
            'about': "OWO",
            'stuff': ["straps"],
            'people': [],
        },
        'basement': {
            'neighbors':['underground'],
            'about': "As you creep your way through the place you show this basement. What is down here.",
            'stuff': ["nails", "metal"],
            'people': random_twin(),
        },
        'underground': {
           'neighbors': ['tunnel', 'basement'],
           'about': "You show a hole that lead to on opening. There is a in the distance.",
           'stuff': [],
           'people': random_twin(),
        },
        'tunnel': {
            'neighbors': ['door', 'underground'],
            'about': "You wounder how far this goes.",
            'stuff': [],
            'people': random_twin(),
        },
        'door': {
            'neighbors': ['tunnel', 'cave'],
            'about': "As you walk down the tunnel you notice a door at the end of it. Do I want to go in?",
            'stuff': [],
        },
        'cave': {
            'neighbors': ['door', 'hole1', 'hole2', 'storage'],
            'about': "When you enter the door you show blood everywhere. You paniced. You head rocks shifted.",
            'stuff': ["tesla coils"],
            'people': random_twin(),
        },
        'hole1': {
            'neighbors': ['cave'],
            'about': "Mmmm whats over here",
            'stuff': [],
            'people': ["minikane"],
        },
        'hole2': {
            'neighors': ['cave'],
            'about': "Mmmm what's over here",
            'stuff': [],
            'people': ["dragondirgel"],
        },
        'storage': {
            'neighbor': ['tunnel2', 'cave'],
            'about': "The storage is where they kept their tools. Bloody... bloody tools.",
            'stuff': ["wires"],
            'poeple': random_twin(),
        },
        'tunnel2': {
            'neighbors': ['storage', 'docks'],
            'about': "How far does this go",
            'stuff': [],
            'people': [],
        },
        'docks': {
            'neighbors': ['basement', 'island', 'tunnel2'],
            'about': "As you exits the tunnel you walk on a dark and misty dock. You can't see anything but a bout. 'Mmmmm I wounder where this goes,' you thought to yourself.",
            'stuff': ["oil"],
            'people': random_twin(),
        },
        'island': {
            'neigbors': ['dock', 'hidden path', 'struggled path'],
            'about': "You get of the bout and looked around. You see a trail that looks like someone was struggling to drag something, and another trail that looks hidden in the bushes",
            'stuff': ["gears"],
            'people': random_twin(),
        },
        'struggled path': {
            'neighbors': ['island'],
            'about': "As you follow the struggled path you start to see a hole. When you get closer to the hole you can see bodys. You hesitated. You walk closer to the hole. The hole presented more bodys you began to be desgusted. You don't know what to do.",
            'stuff': [],
            'people': random_twin(),
        },
        'hidden path': {
            'neighbors': ['island'],
            'about': "You walk the hidden path. When you reach the end of the path you looked around.\n"+
                     "Nothing was in sight. Then from out of know where you heard a voice.\n"+
                     "Stranger: hey up here.\n"+
                     "You look up and show a strange man. You felt safe with him. you climb up.\n"+
                     "Stranger: Hi I am darky. I'm keep an eye on those two rascal.\n"+
                     "You: So you know what is happing and deided to do nothing about it.\n"+
                     "Darky: Well I can't do anything. I'm not really here. You see I'm here to only obsorve them.\n"+
                     "You can save them. Either kill them or help them though this nighmare. I can tell you how to do either one so you have figure that out on your own.\n"+
                     "Now you must leave or I'll kill you. I don't need people here you not safe. LEAVE!!!!\n"+
                     "You hurried out of the treehouse. For some reason you understand why he kick you out, but still don't know why.\n"+
                     "What am I going to do now. Save or Kill.",
            'stuff': [],
            'people': [],
        },
        'kitchen': {
            'neighbors': ['living room', 'hallway'],
            'about': "There might be something usefull",
            'stuff': [],
            'people': ["minikane"],
        },
        'hallway': {
            'neighbors': ['interance', 'studies', 'basement', 'stairs'],
            'about': "Where to go",
            'stuff': [],
            'people': random_twin(),
        },
        'basement': {
            'neighbors': ['hallway'],
            'about': "This is were they did their experiments. There is blood everywhere",
            'stuff': ["saw"],
            'people': random_twin(),
        },
        'studys': {
            'neighbors': ['interance'],
            'about': "There is a phone",
            'stuff': ["book"],
            'people': ["dragondigel"],
        },
        'upstairs_hallway': {
            'neighbors': ['hallway', 'addic', 'room 1', 'room 2', 'room 3'],
            'about': "More doors.",
            'stuff': [],
            'people': random_twin(),
        },
        'addic': {
            'neighbors': ['upstairs_hallway'],
            'about': "I'm safe up here.",
            'stuff': ["rest"],
            'people': [],
        },
        'room 1': {
            'neighbors': ['upstairs_hallway'],
            'about': "Oh no this is Dragon's room",
            'stuff': ["noise maker"],
            'people': ["dragondirgel"],
        },
        'room 2': {
            'neighbors': ['upstairs_hallway'],
            'about': "Crap this is Mini's room",
            'stuff': [],
            'people': ["minikane"],
        },
        'room 3': {
            'neighbors': ['upstairs_hallway'],
            'about': "This must be where they play games",
            'stuff': ["key"],
            'people': random_twin(),
        },
  }




import random

def searching(world):
    number = random.randint(0,3)
    if number == 3:
        world['player']['health'] -= 5
        return "You were attacked!"
    return "You safely searched"

def render_visible_stuff(world):
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']
    
    return "You have " + str(inventory) + " in inventory."
    
def render(world):
    return (render_location(world) +
            render_player(world) +
            render_visible_stuff(world))

def get_options(world):
    commands = ["quit"]
    current_location = world["player"]["location"]
    location = world['map'][current_location]
    neighbors = location['neighbors']
    
    for neighbor in neighbors:
        commands.append("go to " + neighbor)
    
  
    if current_location == 'interance':
        commands.append('search')
    if current_location == 'livingroom':
        commands.append('search')
    if current_location == 'outside':
        commands.append('search')
    if current_location == 'woods':
        commands.append('search')
    if current_location == 'cabin':
        commands.append('search')
    if current_location == 'living room':
        commands.append('search')
    if current_location == 'back room':
        commands.append('search')
    if current_location == 'bedroom':
        commands.append('search')
    if current_location == 'basement':
        commands.append('search')
    if current_location == 'underground':
        commands.append('search')
    if current_location == 'tunnel':
        commands.append('search')
    if current_location == 'door':
        commands.append('search')
    if current_location == 'cave':
        commands.append('search')
    if current_location == 'hole1':
        commands.append('search')
    if current_location == 'hole2':
        commands.append('search')
    if current_location == 'storage':
        commands.append('search')
    if current_location == 'tunnel2':
        commands.append('search')
    if current_location == 'docks':
        commands.append('search')
    if current_location == 'island':
        commands.append('search')
    if current_location == 'struggled path':
        commands.append('search')
    if current_location == 'hiddenpath':
        commands.append('search')
    if current_location == 'kitchen':
        commands.append('search')
    if current_location == 'hallway':
        commands.append('search')
    if current_location == 'basement':
        commands.append('search')
    if current_location == 'studys':
        commands.append('search')
    if current_location == 'upstairs_hallway':
        commands.append('search')
    if current_location == 'addic':
        commands.append('rest')
    if current_location == 'room1':
        commands.append('search')
    if current_location == 'room2':
        commands.append('search')
    if current_location == 'room3':
        commands.append('search')
    return commands


def goto(world, command):
    new_location = command[len('go to '):]
    world['player']['location'] = new_location
    return "You went to " + new_location

def update(world, command):
    if command == "quit":
        world['status'] = 'quit'
        return "You quit the game"
    
    if command.startswith('go to '):
        return goto(world, command)
    
    if command == "search":
        return searching(world)
    if command == "rest":
        world['player']['health'] = 100
        return "You took a nice nap. Your health is at a 100"
    
    return "Unknown command: " + command

def render_ending_lost(world):
    return "You Lost. Nice try."

def render_ending(world):
    if world['status'] == 'won':
        return "You won! Now you get the twins owo."
    elif world['status'] == 'lost':
        return render_ending_lost(world)
    elif world['status'] == 'quit':
        return "You quit the game, but why?"

def choose(options):
    print("Available commands:")
    for option in options:
        print(option)
        
    command = input("Type a command: ")
    while command not in options:
        command = input("Invalid Command\n\nType a command: ")
    return command


###### 4) Win/Lose Paths #####
# The autograder will use these to try out your game
# WIN_PATH (list[str]): A list of commands that win the game when entered
# LOSE_PATH (list[str]): A list of commands that lose the game when entered.

WIN_PATH = []
LOSE_PATH = []
    
###### 5) Unit Tests #####
# Write unit tests here

from cisc108 import assert_equal


###### 6) Main Function #####
# Do not modify this area

def main():
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))

if __name__ == '__main__':
    main()

