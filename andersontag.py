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
__author__ = "zack.alvey@washk12.org"
__title__ = "Name of your game goes here"
__description__ = "Replace this with a quick description of your game."

# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"


##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.

'''
Records:
    World:
      status (str): Whether or not the game is "playing", "quit", "won", or "lost".
                    Initially "playing".
      map (dict[str: Location]): The lookup dictionary matching location names
                     to their information.
      player (Player): The player character's information.

    Player:
      location (str): The name of the player's current location.
      inventory (list[str]): The player's collection of items. Initially empty.
      hungry (bool): True if Mtr Alvey needs food.
      sanity (bool): False if Mr Alvey is insane
      money (int): how much money Mr. Alvey has

    Location:
      about (str): A sentence that describes what this location looks like.
      neighbors (list[str]): A list of the names of other places that you can
                             reach from this location.
      stuff (list[str]): A collection of things available at this location.
      people (list[Person]): A random list of persons at a location 

    Person:
      name (str): The person’s name
      annoying (bool): True if the person is annoying and causes insanity
'''

##### 3) Core Game Functions #####
# Implement the following to create your game.

def render_introduction():
    '''
    Create the message to be displayed at the start of your game.
    
    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return ("== Mr. Alvey Teacher Adventure ==\n" +
            " = by Mr. Alvey's 3rd period class =\n\n" +
            "After getting to school Mr. Alvey must earn\n" +
            "enough money to get home without going insane.\n" +
            "Mr. Alvey is sitting in his classroom and the\n" +
            "bell rings for first period.\n")

def random_students():
    '''
    Return a random list of students, most sane, some insane
    '''
    
def random_chillstaff():
    '''
    Return a random list of dq workers, most sane, some insane
    '''

def create_map():
    '''
    Creates a dictionary of the world map
    
    Returns:
        Map
    '''
    return {
        'classroom' : {
            'about': 'You are at your desk in your classroom. The students are ready to learn.', 
            'neighbors' : ['lounge', 'car'],
            'stuff': ['ibuprofen', 'cliff bar', 'lotto ticket'],
            'people': random_students()
        },
        'lounge' : {
            'about': 'You sit in your regular spot and Hosner comments on your food.',
            'neighbors' : ['classroom'],
            'stuff': ['salt', 'pepper'],
            'people': ['Kreitzer', 'Holt', 'Roberts', 'Hosner', 'Shaw', 'Dewitt', 'B']   
        },
        'car' : {
            'about': 'You sit in your car and turn on the engine.',
            'neighbors' : ['lins', 'home'],
            'stuff': ['apron', 'name badge'],
            'people': [],
        },
        'lins' : {
            'about': 'You put on your apron and log into your register',
            'neighbors' : ['car', 'dq'],
            'stuff': ['pen', 'spray bottle'],
            'people': ['Ashlee', 'Jeff', 'Collin'],    
        },
        'dq' : {
            'about': 'You yell for help at the dq counter.',
            'neighbors' : ['lins'],
            'stuff': ['french fries'],
            'people': random_chillstaff(),    
        },
        'archam' : {
            'neighbors' : ['home'],
            'stuff': ['bat-erang', 'clown mask'],
            'people': ['Joker', 'Counselor', 'Batman', 'Gordon', 'Dent', 'Alfred']    
        },
        'home' : {
            'about': 'You made it home to your family. You are happy. You win',
            'neighbors' : [],
            'stuff': [],
            'people': []
        }
    }

def create_player():
    '''
    Creates a dictionary of the player
    
    Returns:
        Player
    '''
    return {
        'location': 'classroom',
        'inventory': [],
        'hungry': False,
        'sanity': True,
        'money': 0
        }

def create_world():
    '''
    Creates a new version of the world in its initial state.
    
    Returns:
        World: The initial state of the world
    '''
    return {
        'map': create_map(),
        'player': create_player(),
        'status': "playing"
    }

def render_location(world):
    '''
    Consume a world and produce a string describing the location
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    
    return ("You are in "+location+"\n"+
            about+"\n")

def render_player(world):
    '''
    Consume a world and produce a string describing the player
    '''
    
    hungry = world['player']['hungry']
    sanity = world['player']['sanity']
    money = world['player']['money']
    
    statement = ""
    if hungry:
        statement += "You are hungry, you should eat soon. "
    if not sanity:
        statement += "You are going insane, please get help."
    statement += "You have " + str(money) + " dollars."
    
    return statement
    
def render_visible_stuff(world):
    '''
     Consumes a world and produces a string of visible items
     '''
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']
    
    if location == 'classroom':
        return "You see a desk that might have something useful to you inside."
    else:
        visible_stuff = []
        for thing in stuff:
            visible_stuff.append(thing)
        return "You see: " + ', '.join(visible_stuff)
    
def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''
    return (render_location(world) +
            render_player(world) +
            render_visible_stuff(world))

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    
    commands = ["quit"]
    current_location = world["player"]["location"]
    location = world['map'][current_location]
    neighbors = location['neighbors']
    
    for neighbor in neighbors:
        commands.append("go to " + neighbor)
    
    if current_location == "classroom":
        commands.append("search desk")
        commands.append("teach")
    if current_location == "lounge":
        commands.append("complain")
        commands.append("eat")
    if current_location == "lins":
        commands.append("ring up")
    if current_location == "dq":
        commands.append("eat")
        commands.append("get icecream")
    if current_location == "archam":
        commands.append("counseling")
        commands.append("meet joker")
    return commands
    
def goto(world, command):
    new_location = command[len('go to '):]
    world['player']['location'] = new_location
    return "You went to " + new_location
    
def update(world, command):
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.
    
    Args:
        world (World): The current world to modify.
    
    Returns:
        str: A message describing the change that occurred in the world.
    '''
    if command == "quit":
        world['status'] = 'quit'
        return "You quit the game"
    
    if command.startswith('go to '):
        return goto(world, command)
    
        
    return "Unknown command: " + command

def render_ending_lost(world):
    return "You lost."
    
def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.
    
    Args:
        world (World): The final world state to use in describing the ending.
    
    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world['status'] == 'won':
        return "You won!"
    elif world['status'] == 'lost':
        return render_ending_lost(world)
    elif world['status'] == 'quit':
        return "You quit."

def choose(options):
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.
    
    Note:
        Use your answer to Programming Problem #42.3
    
    Args:
        options (list[str]): The potential commands to select from.
    
    Returns:
        str: The command that was selected by the user.
    '''
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

assert_equal("Mr. Alvey" in render_introduction(), True)
assert_equal("classroom" in render_introduction(), True)

player = create_player()
# Use the built-in isinstance function to confirm that we made a dictionary
assert_equal(isinstance(player, dict), True)
# Does it have the right keys?
assert_equal(len(player.keys()), 2)
assert_equal("location" in player, True)
assert_equal(player['location'], 'classroom')
assert_equal("inventory" in player, True)
assert_equal(player['inventory'], [])
assert_equal("hungry" in player, True)
assert_equal(player['hungry'], False)
assert_equal("sanity" in player, True)
assert_equal(player['sanity'], True)
assert_equal("money" in player, True)
assert_equal(player['money'], 0)

new_map = create_map()

assert_equal("classroom" in new_map, True)
assert_equal("lounge" in new_map, True)
assert_equal("car" in new_map, True)
assert_equal("lins" in new_map, True)
assert_equal("dq" in new_map, True)
assert_equal("archam" in new_map, True)
assert_equal("home" in new_map, True)


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
