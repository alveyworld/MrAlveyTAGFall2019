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
__author__ = "21lawresha@washk12.org"
__title__ = " Ben ? "
__description__ = ('You are a Germen medieval peasant Farmmer who was in \n'+
'his field who has just thrown down his hoe down win by making 10 gold')

# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"


##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.

''''
Records:
    World:
        status (str): Whether or not the game is "playing", "won",
                      "quit", or "lost". Initially "playing".
        map (dict[str: Location]): The lookup dictionary matching 
                                   location names to their
                                   information.
        player (Player): The player character's information.

      
    Player:
        location (str): The name of the player's current location.
        inventory (list[str]): The player's collection of items.
                               Initially empty.
        state (bool: Hungry): the current health of the player
    
    Location:
        about (str): A sentence that describes what this location 
                     looks like.
        neighbors (list[str]): A list of the names of other places 
                               that you can reach from this 
                               location.
        stuff (list[str]): A collection of things available at 
                           this location.
        people (list[Person(s)]): a list of person(s) at a location
        
        Person:
            name (str): the person's name
            r_info (str): they say somthing random lore based
            Buy/sell (str): what the person sells/buys
            
            
'''

##### 3) Core Game Functions #####
# Implement the following to create your game.

def render_introduction():
    '''...'''
    return ("== Ben ? ==\n"+
            "= By Shaden Lawrence =\n"+
            "\n"+
            ".... *Nothing* ... *Something* Light your flying through space on a long voyage\n"+
            ' *Smack* ... your awake ... your hear in the distance "Ben ?"\n'+
            " you get up. your in a field your old. you dust your self off\n"+
            ' your old bones hurt then you hear it again "Ben!" this time more angry\n '+
            '"what are you doing... i dont pay you a a copper an hour for doing nothing"\n'+
            'Aw so you need money ... guess your job is to get money then.\n'+
            "== Objective Gained ==\n" + "== Get 10 gold==")

import random
def random_cliff_text():
    Cliff_Text = ['Whoa this looks dangeroures','i think i see Sharp rocks ','It looks nice today ... Whoa a cliff!']
    return random.choice(Cliff_Text) 
    
    
def create_map():
    return {
        
        'farm house':{
            'neighbors':['Field','Town of Zik'],
            'about':"a old house sat on a hill over looking a large ranch it\n"+
                     "looks like it has not seen much use but there is a table nearby\n"+
                     "East is a large Field and to the South there is the town of Zik",
            'stuff':['1 gold coin','bowl of soup'],
            'people':['Your boss']
            },
            
        'Field':{
            'neighbors':['farm house','Pasture','Small Clearing'],
            'about':"A large Field of golden wheat\n"+
                    'to the West is a old house to the East is a Large Pasture\n'+
                    'and to the south is a dense forest',
            'stuff':["wheat","hoe"],
            'people':[]
            },
        
        
        'Pasture':{
            'neighbors':['Field','Clearing'],
            'about':"Large Field of grass light seems brighter here and life seems happier \n"+
                    'to the west a field of wheat to the east a dense forest',
            'stuff':['wool','eggs'],
            'people':[]
            },
        
        'Clearing':{
            'neighbors':['Pasture','Ravine','Large tree'],
            'about':"You are in a clearing in the forest you see the forest continues south"
            + "there is a pasture to the west and a large hole to the east",
            'stuff':[],
            'people':[]
            },
        
        'Ravine':{
            'neighbors':['Clearing','Ravine w/ Bridge'],
            'about':"there is a big crack in the earth that is very deep and it keeps going" +
            " down to the south and there are some woods to the east",
            'stuff':[],
            'people':[],
            },
        
        'In Ravine':{
            'neighbors':['Bullywogs Huts','in Ravine Under Bridge'],
            'about':'you are in a deep chasm your feet are now damp\n'+
                    'to the east is a way up and to the south is deeper into the ravine',
            'stuff':[],
            'people':[],
            },
        
        'Bullywogs Huts':{
            'neighbors':['In Ravine','Calm waters','Merlock Huts'],
            'about':'You walk up to a bunch of small huts as 2 small frogs jump out one green the other yellow'+
                    'to the west is a way down into a deep ravine to the east is the ocean\n'+
                    'and to the south farther down the beach',
            'stuff':[],
            'people':['Green Bullywog','Yellow Bullywog']
            },
        
        'Calm waters':{
            'neighbors':['Bullywogs'],
            'about':"Calm still waters there might be a ship out there...\n"+
            'But probably not thats the edge of the world',
            'stuff':[],
            'people':[],
            },
        
        'Town of Zik':{
            'neighbors':['Farm house','Small Clearing','River','Blacksmith'],
            'about':'A large City full of people from this part of the Germany\n'+
                    'they come in all shapes and sizes some big some small \n'+
                    'But they all seem bigger than you\n'+
                    'to the north is a small House to the east is a small forest\n'+
                    'and to the south is a small house with a forge outside',
            'stuff':[],
            'people':['Tailor','Coining Store','Food vendor 1','Food vendor 2'],
            },
        
        'Small Clearing':{
            'neighbors':['Town of Zik', 'Thief Hideout','Field','River'],
            'about':"A small clearing in the woods there is a field to the north"
            + "town to the west and to hear water from the south and see something to"
            +"the east.",
            'stuff':[],
            'people':[],
            },
        
        'Thief Hideout':{
            'neighbors':['Woods 2','woods 3','Wood w/ River 1'],
            'about':'',
            'stuff':[],
            'people':[],
            },
        
        'Woods with a large tree':{
            'neighbors':['Clearing','Thief Hideout','Ravine w/ Bridge','Above Cavern'],
            'about':"A small clearing with a big tree there is more woods to the west \n" +
            ' and north and opening to the south and a big opening to the east',
            'stuff':[],
            'people':[],
            },
        
        'Ravine w/ Bridge':{
            'neighbors':['Ravine','in Ravine Under Bridge','Woods w/ Cliff','Above Cavern','Large tree'],
            'about':"There is a big Ravine with a small rope Bridge and you can see it going \n" +
            "to the north and you some woods on the other side to the south east and some to the \n"+
            "west and south west.",
            'stuff':[],
            'people':[],
            },
        
        'In Ravine Under Bridge':{
            'neighbors':['Ravine w/ Bridge','Goblin Cavern'],
            'about':'you are in a deep Ravine above you is a small rope bridge\n'+
                    'to the north is farther into the ravine , there is a way up out of the ravine \n'+
                    'and there is a path into a cave to the SouthWest',
            'stuff':['Gold vein'],
            'people':[],
            },
        
        
        'Merlock Huts ':{
            'neighbors':['Bullywogs Huts','Deep waters','Sandy Beach'],
            'about':"as you aproch wooden houses elevated above the water\n"+
                    'two merlocks jump out of them one white one blue\n'+
                    'there is a path farther up the beach north \n'+
                    'a way to the ocean east , and a path down the beach south',
            'stuff':[],
            'people':['white merlock','Blue merlock'],
            },
        
        'Goblin Cavern':{
            'neighbors':['In Ravine Under Bridge',],
            'about':'',
            'stuff':[],
            'people':['Goblins'],
            },
        
        'Deep waters':{
            'neighbors':['Ravine w/ Bridge'],
            'about':"you are swimming in the water and can not touch the bottom and \n" +
            " you see some huts to the west.",
            'stuff':[],
            'people':[],
            },
        
        'Black Smith':{
            'neighbors':['Town of Zik','River',"Olga's House"],
            'about':'The smell of iorn can be smelled in the air as you aproch \n'+
                    'there is a small man bent over an anvil smashing red hot iron\n+'
                    'into a cast to make nails\n'+
                    'north is the Town of Zik east is a River and south is a large house',
            'stuff':[],
            'people':['Blacksmith'],
            },
        
        'River':{
            'neighbors':['Black Smith','Wood w/ River 1','Town of Zik'],
            'about':"there are trees all around you and a small river that flows to \n" +
            " the east and you see some more woods the the south and a building to the \n"+
            "west and a Town to the north west.",
            'stuff':[],
            'people':[],
            },
        
        'Small creek':{
            'neighbors':['River','Cavern 2','Thief Hideout','Wood w/ River','Ginger Bread House'],
            'about':"there is a small creek with a small river to the west and one going \n"+
            " to the south east from with lots of tree all around and you see wood \n" +
            "all around and a small trail of candy to the south.",
            'stuff':[],
            'people':[],
            },
        
        'hidden Cave':{
            'neighbors':['Wood w/ River 1'],
            'about':"a small damp cave hidden by vines in the woods near a river",
            'stuff':['hidden chest'],
            'people':[],
            },
        
        'Above Cavern':{
            'neighbors':['Small creek','Ravine w/ Bridge','Woods w/ River', 'Woods with a large tree'],
            'about':"there is a small hole in the ground and some woods to the south and \n"+
            "to the north you also hear smo water flowing to the west.",
            'stuff':[],
            'people':[],
            },
        
        'Woods w/ cliff':{
            'neighbors':['Ravine w/ Bridge','Sandy beach'],
            'about':"you are in a small group of trees and you see a cliff to the \n"+
            "south and a bridge to the north east and a beach to the east",
            'stuff':[],
            'people':[],
            },
        
        'Sandy beach':{
            'neighbors':['Woods w/ cliff', 'Merlock Huts','Shallow waters'],
            'about':'you are standing on the beach and you can see some huts to the north n/'+
            "and some wood to the west and some water to the east.",
            'stuff':[],
            'people':[],
            },
        
        'Shallow waters':{
            'neighbors':['Sandy beach'],
            'about':"you are standing in the water and see a nest with a egg and you can see \n"+
            "the beach to the west.",
            'stuff':['Gold egg'],
            'people':[],
            },
        
        "Olga's House":{
            'neighbors':['Black Smith','Dead forest','High Cliff'],
            'about':'A small women sits in front of a very large house\n'+
                    'the house looks very old it has many celtic symbols\n'+
                    'and many other drudic symbols\n'+
                    'to the north is a small house with a forge outside\n'+
                    'to the east is a dead forest and to\n'+
                    ' the south is a Hill near a Cliff',
            'stuff':[],
            'people':['Olga'],
            },
        
        'Dead forest':{
            'neighbors':['River',"Olga's House",'Ginger Bread House','Grassy Cliff'],
            'about':'you aproch a what looks like a dead forest.\n'+
                    'Hundreds of crows sit up high in the leafless trees\n'+
                    'there eyes fallow you as you walk deeper into there domain\n'+
                    'to the north is a river and to the west is a large house\n'+
                    'to the east is a Tail made of candy and to the south is a grassy feild',
            'stuff':[],
            'people':[],
            },
        
        'Ginger Bread House':{
            'neighbors':['Small Creek','Dead Forest','Woods w/ River','Dry Cliff','Entrance Hall'],
            'about':"as you fallow a path of candy to a house made of candy deep in the woods\n"+
                    'there is a door into the house and paths made of candy leading in every direction',
            'stuff':['Candy'],
            'people':[],
            },
        
        'Dining Hall':{
            'neighbors':['Entrance Hall'],
            'about':'A large room made of candy, a table made of candy,\n '+
                    'even painting made of candy a door to the East ',
            'stuff':['candy'],
            'people':[],
            },
        
        'Entrance Hall':{
            'neighbors':['Ginger Bread House','Dining hall','Kitchen','Alchemy room'],
            'about':'A large hall leading into a house made of candy\n'+
                    'there is a door to the north and rooms to the east, south, and west',
            'stuff':['Candy'],
            'people':[],
            },
        
        'Kitchen':{
            'neighbors':['Entrance Hall','Libary'],
            'about':'a room made of cobblestone there is a large cooking stove\n'+
                    'there is something in the stove cooking',
            'stuff':['Meat Pie','Golden Fork'],
            'people':[],
            },
        
        'Bedroom':{
            'neighbors':['Alchemy room'],
            'about':'',
            'stuff':[],
            'people':[],
            },
        
        'Alchemy room':{
            'neighbors':['Bedroom','Library','Entrance hall','Basement'],
            'about':"you look around the room and see bottles of all colors and sizes \n"+
            "and there are four door you can see one to the north one to the south \n"+
            "one to the west and one to the east",
            'stuff':[],
            'people':[],
            },
        
        'Library':{
            'neighbors':['Alchemy room'],
            'about':'you look around and see shelves of books lots and lots of books \n'+
            "and you can see a door to the west.",
            'stuff':[],
            'people':[],
            },
        
        'Basement':{
            'neighbors':['Alchemy room'],
            'about':'',
            'stuff':[],
            'people':[],
            },
        
        'Woods w/ River':{
            'neighbors':['Above Cavern','Ginger Bread House','Shark infested waters','Muddy Cliff','Small Creek'],
            'about':"A Forest of dead trees and insects with a candy path cutting through\n"+
                    'untell the path reaches a large Stream were it turns into a cobble stone Bridge\n'+
                    'the river continues untell it passes down the beach into the ocean \n'+
                    'you could fallow the river up to the North Weast, East into the sea,\n'+
                    'you could fallow the path West toward a cottege in the woods,\n'+
                    'or head North along the path before it turns into woods',
            'stuff':[],
            'people':['Troll'],
            },
        
        'Shark infested waters':{
            'neighbors':['Woods w/ River'],
            'about':'',
            'stuff':[],
            'people':['Shark'],
            },
        
        'High Cliff':{
            'neighbors':["Olga's House",'Grassy Cliff'],
            'about':'you can see farther from this hill near a cliff\n'+
                    'you can see The town of Zik form here you walk down the hill\n'+
                    'and look at the cliff' + random_cliff_text() +
                    'you can head North to a large house \n' +
                    'and east to another cliff',
            'stuff':[],
            'people':[],
            },
        
        'Grassy Cliff':{
            'neighbors':['Dead Forest','High Cliff','Dry Cliff'],
            'about':'you are standing in a feild of grass as high as your head you walk a bit south\n'+
                    'Where you see you are standing on a cliff when you yip and say'+ ' " ' + random_cliff_text() + ' "' +
                    'you get up on a rock and can see that you can head North to a forest of dead trees,\n'+
                    'or head West or East to another cliff',
            'stuff':[],
            'people':[],
            },
        
        'Dry Cliff':{
            'neighbors':['Ginger Bread House','',''],
            'about':'The land here is very weird the ground is dry\n'+
                    'not a animal in sight you aproch the edge of the cliff\n' +
                    'the water looks nice like it wants to give you a big hug\n'+
                    random_cliff_text() + 'you can head North to a small cottage in the woods,\n'+
                    'West into a feild of grass, or East to another cliff in the distance',
            'stuff':[],
            'people':[],
            },
        
        'Muddy Cliff ':{
            'neighbors':[],
            'about':'the land here is slippery and slick \n' +
                    'your feet find it hard to find perches in the mud\n' +
                    'you fall and slide toward a Cliff face' + random_cliff_text() +
                    '',
            'stuff':[],
            'people':[],
            },
        
        'hacker':{
            'neighbors':[],
            'about':'Hey what are you doing here wow now you have just sommoned \n'+
                    'CTHULU!!! WERE ALL DOOMED',
            'stuff':[],
            'people':['Cthulu'],
            },
         }
def create_player():
    return {
        'location': 'Field',
        'inventory': [],
        'Hunger': False,
        'Gold': 0
        }

def create_world():
    return{
        'map': create_map(),
        'player': create_player(),
        'status':"playing"
        
    }

def render_visible_stuff(world):
    
    location = world['player']['location']
    here = world['map'][location]
    stuff = here['stuff']
    inventory = world['player']['inventory']
    
    if location == 'Farm House':
        return "you see a Bowl of Soup"+'and'+'you can a gold coin on the table'
    else:
        visible_stuff = []
        for thing in stuff:
            visible_stuff.append(thing)
        return "You see: " + ', '.join(visible_stuff)


def render_player(world):
    '''
    Consume a world and produce a string describing the player
    '''
    inventory = world['player']['inventory']
    Gold = world['player']['Gold']
    Hunger = world['player']['Hunger']
    return "Gold: " + str(Gold) + " Hungry: " + str(Hunger)

def render_location(world):
    '''
    Consume a world and produce a string describing the location
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    
    return ("You are in "+location+"\n"+
            about+"\n")
    
def render(world):
    
    return (render_location(world) +
            render_player(world) +
            render_visible_stuff(world))
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''

def get_options(world):
    
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
     # ...
    commands = ["Quit"]
    current_location = world['player']['location']
    l = current_location
    location = world['map'][current_location]
    neighbors = location['neighbors']
    
    
    for neighbor in neighbors:
        commands.append("go to " + neighbor)
    
    if location == 'farm house' and '1 gold coin' in stuff not in inventory:
        commands.append('pick up gold coin')
        
    if location == 'farm house' and 'bowl of soup' in stuff not in inventory:
        commands.append('pick up bowl of soup')
        
    if location == 'field' and 'wheat' in stuff and 'wheat' not in inventory and 'hoe' in inventory:
        commands.append('pick up wheat')
        
    return commands

def goto(world, command):
    new_location = command[len('go to '):]
    world['player']['location'] = new_location
    return "You went to "+new_location

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
        return 'you quit the game'
    
    if command.startswith('go to '):
        return goto(world, command)
    
    return 'unknown command: ' + command

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
        return "You lost."
    elif world['status'] == 'quit':
        return "You quit."
    
def render_ending_lost(world):
    if world['player'] ['location'] == 'Thief Hideout' :
        return ("As you walk through the wood you see some small buildings in the \n" +
                "trees as you get close you hear a loud thump then you black out")
         
    if world['player'] ['location'] == 'goblin cavern' :
        return("you walk into a dark Cavern as red eyes light up across the walls")
    
    if world['player'] ['location'] == 'Bedroom' :
        return("as you walk in the dark room you see some one and then \n"+
            "you see them look at you and then they grab you and tie you up \n"+
            "and then thay throw you down the basement.")
    
    if world['player'] ['location'] == 'Shark infested waters' :
        return("as you wade out into the water you see a shark fin pop out of the water\n")

    if world['player'] ['location'] == 'goblin cavern' :
        return('')

    
    return ("You were eaten by a Grue.\n"+
                "You lose!")
    

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
    command = input("type a command: ")
    while command not in options:
        command = input("Invalid Cammand \n\nType a command: ")
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

# Confirm that we printed the name of the game
assert_equal("== Ben ? ==" in render_introduction(), True)
# We should have 5 lines of text
assert_equal(render_introduction().count("\n"),7)
# Make sure it explicitly mentions "your house" to set up the punchline,
#   that you've been in your own house the entire game.
assert_equal("old bones" in render_introduction().lower(), True)



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
