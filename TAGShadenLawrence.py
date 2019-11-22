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
            "\n" +
            ".... *Nothing* ... *Something* Light your flying through space on a long voyage\n"+
            ' *Smack* ... your awake ... your hear in the distance "Ben ?"\n'+
            " you get up. your in a field your old. you dust your self off\n"+
            ' your old bones hurt then you hear it again "Ben!" this time more angry\n '+
            '"what are you doing... i dont pay you a a copper an hour for doing nothing"\n'+
            'Aw so you need money ... guess your job is to get money then.\n'+
            "== Objective Gained ==\n" + "== Get 10 gold== \n")

import random
def random_cliff_text():
    Cliff_Text = ['Whoa this looks dangeroures','i think i see Sharp rocks ','It looks nice today ... Whoa a cliff!']
    return random.choice(Cliff_Text) 
    
    
def create_map():
    return {
        
        'farm house':{
            'neighbors':['field','town of zik'],
            'about':"\n a old house sat on a hill over looking a large ranch it\n"+
                    "looks like it has not seen much use but there is a table nearby\n"+
                    'on the table is 1 gold coin and a bowl of soup\n' +
                    "East is a large field and to the South there is the town of zik",
            'stuff':['mushroom','bowl of soup','shears'],
            'people':[{
                'name':'your boss',
                'about':'What are you doing Ben aw i dont care as long as i get money',
                'sells':{},
                'buys':{}
                }]
            },
            
        'field':{
            'neighbors':['farm house','pasture','small clearing'],
            'about':"\n A large Field of golden wheat\n"+
                    'to the West is a old house to the East is a Large Pasture\n'+
                    'there is a hoe at your feet and wheat all around you\n' +
                    'and to the south is a dense forest',
            'stuff':['wheat','hoe',],
            'people':[],
            },
        
        
        'pasture':{
            'neighbors':['field','clearing'],
            'about':"\n Large Field of grass light seems brighter here and life seems happier \n"+
                    'to the west a field of wheat to the east a dense forest',
            'stuff':['wool','eggs'],
            'people':[],
            },
        
        'clearing':{
            'neighbors':['pasture','ravine','large tree'],
            'about':"\n You are in a clearing in the forest you see the forest continues south"
            + "there is a pasture to the west and a large hole to the east",
            'stuff':[],
            'people':[],
            },
        
        'ravine':{
            'neighbors':['clearing','ravine w/ bridge'],
            'about':"\n there is a big crack in the earth that is very deep and it keeps going" +
            " down to the south and there are some woods to the east",
            'stuff':[],
            'people':[],
            },
        
        'in ravine':{
            'neighbors':['bullywogs huts','in ravine under bridge'],
            'about':'\n you are in a deep chasm your feet are now damp\n'+
                    'to the east is a way up and to the south is deeper into the ravine',
            'stuff':[],
            'people':[],
            },
        
        'bullywogs huts':{
            'neighbors':['in ravine','calm waters','merlock huts'],
            'about':'\n You walk up to a bunch of small huts as 2 small frogs jump out one green the other yellow \n'+
                    'to the west is a way down into a deep ravine to the east is the ocean\n'+
                    'and to the south farther down the beach',
            'stuff':[],
            'people':[{
                'name':'green bullywog',
                'about':'*ribit* hello there my nice fellow *ribit*\n'+
                        'can you help us some slimmy fish stole are flys\n'+
                        '*ribit* will you go get them back. well give back *ribit*\n'+
                        'there seaweed its just in are pond to the east',
                'sells':{},
                'buys':{'jar of flies':{"amount": 3, "currency": 'gold'}}
                },{
                'name':'yellow bullywog',
                'about':'',
                'sells':{},
                'buys':{}
                }]
            },
        
        'calm waters':{
            'neighbors':['bullywogs huts'],
            'about':"\n Calm still waters there might be a ship out there...\n"+
            'But probably not thats the edge of the world',
            'stuff':['tasty seaweed'],
            'people':[],
            },
        
        'town of zik':{
            'neighbors':['farm house','small clearing','river','black smith'],
            'about':'\n A large City full of people from this part of the Germany\n'+
                    'they come in all shapes and sizes some big some small \n'+
                    'But they all seem bigger than you\n'+
                    'to the north is a small House to the east is a small forest\n'+
                    'and to the south is a small house with a forge outside',
            'stuff':[],
            'people':[{
                'name':'Tailor',
                'about':'',
                'sells':{},
                'buys':{'wool':{"amount": 2, "currency": 'gold'},}
                },{
                'name':'Coining Store',
                'about':'',
                'sells':{},
                'buys':{'gold vien':{'amount': 3, 'currency': 'gold'}}
                },{
                'name':'Food Market',
                'about':'',
                'sells':{},
                'buys':{'mushroom':{'amount': 1, 'currency': 'gold'},'bowl of soup':{'amount':1, 'currency': 'gold'},'wheat':{'amount':2, 'currency': 'gold'},'eggs':{'amount':2, 'currency': 'gold'},'Candy':{'amount':1, 'currency': 'gold'},'Meat pie':{'amount':2, 'currency': 'gold'}}
                }],
            },
        
        'small clearing':{
            'neighbors':['town of zik', 'the dark woods','field','river'],
            'about':"\n A small clearing in the woods there is a field to the north"
            + "town to the west and to hear water from the south and see something to"
            +"the east.",
            'stuff':[],
            'people':[],
            },
        
        'the dark woods':{
            'neighbors':['small clearing','large tree','small creek'],
            'about':' a dark forest',
            'stuff':[],
            'people':[],
            },
        
        'large tree':{
            'neighbors':['clearing','the dark woods','ravine w/ bridge','well','up tree'],
            'about':"\n A small clearing with a big tree there is more woods to the west \n" +
            ' and north and opening to the south and a big opening to the east',
            'stuff':[],
            'people':[],
            },
        
        'up tree':{
            'neighbors':['large tree'],
            'about':'you climb up the tree you see a nest with many diffrent eggs a few shine ',
            'stuff':['silver egg'],
            'people':[],
            },
        
        'ravine w/ bridge':{
            'neighbors':['ravine','in ravine under bridge','woods w/ cliff','well','large tree'],
            'about':"\n There is a big Ravine with a small rope Bridge and you can see it going \n" +
            "to the north and you some woods on the other side to the south east and some to the \n"+
            "west and south west.",
            'stuff':[],
            'people':[],
            },
        
        'in ravine under bridge':{
            'neighbors':['ravine w/ bridge','cavern','in ravine'],
            'about':'\n you are in a deep Ravine above you is a small rope bridge\n'+
                    'to the north is farther into the ravine , there is a way up out of the ravine \n'+
                    'and there is a path into a cave to the SouthWest',
            'stuff':['gold vein'],
            'people':[],
            },
        
        
        'merlock huts':{
            'neighbors':['bullywogs huts','deep waters','sandy beach'],
            'about':"\n as you aproch wooden houses elevated above the water\n"+
                    'two merlocks jump out of them one white one blue\n'+
                    'there is a path farther up the beach north \n'+
                    'a way to the ocean east , and a path down the beach south',
            'stuff':[],
            'people':[{
                'name':'white merlock',
                'about':'Hey you big guy can you help us some frogs to the north stole from us\n' +
                'can you get us back are seaweed well give you there flys there to the east in are sea town',
                'sells':{},
                'buys':{'tasty seaweed':{"amount": 3, "currency": 'gold'}}
                },{
                'name':'Blue merlock',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'cavern':{
            'neighbors':['in ravine under bridge',],
            'about':'',
            'stuff':[],
            'people':[{
                'name':'Goblins',
                'about':'a wut dus u think u doing here Grab him',
                'sells':{},
                'buys':{}
                }],
            },
        
        'deep waters':{
            'neighbors':['merlock huts'],
            'about':"\n you are swimming in the water and can not touch the bottom and \n" +
            " you see some huts to the west.",
            'stuff':['jar of flies'],
            'people':[],
            },
        
        'black smith':{
            'neighbors':['town of zik','river',"olga's house"],
            'about':'\n The smell of iorn can be smelled in the air as you aproch \n'+
                    'there is a small man bent over an anvil smashing red hot iron\n'+
                    'into a cast to make nails\n'+
                    'north is the Town of Zik east is a River and south is a large house',
            'stuff':[],
            'people':[
                    {'name': 'Blacksmith',
                    'about':'',
                    'sells':{"pickaxe": {"amount": 2, "currency": 'gold'}},
                    'buys':{'silver egg':{'amount':3, 'currency': 'gold'}, 'golden fork':{'amount':1, 'currency': 'gold'},'hoe':{'amount':1,  'currency': 'gold'},},
                    }],
            },
        
        'river':{
            'neighbors':['black smith','small creek','town of zik'],
            'about':"\n there are trees all around you and a small river that flows to \n" +
            " the east and you see some more woods the the south and a building to the \n"+
            "west and a Town to the north west.",
            'stuff':[],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'small creek':{
            'neighbors':['river','well','the dark woods','woods w/ river','ginger bread house','hidden cave'],
            'about':"\n there is a small creek with a small river to the west and one going \n"+
            " to the south east from with lots of tree all around and you see wood \n" +
            "all around and a small trail of candy to the south.",
            'stuff':[],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'hidden cave':{
            'neighbors':['small creek'],
            'about':"\n a small damp cave hidden by vines in the woods near a river",
            'stuff':['hidden chest'],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'well':{
            'neighbors':['small creek','ravine w/ bridge','woods w/ river', 'large tree',],
            'about':"\n There is a old broken well in the middle of a clearing \n"+
            "to the north is a large tree you also hear some water flowing to the west and south.",
            'stuff':[],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'woods w/ cliff':{
            'neighbors':['ravine w/ bridge','sandy beach'],
            'about':"\n you are in a small group of trees and you see a cliff to the \n"+
            "south and a bridge to the north east and a beach to the east",
            'stuff':[],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'sandy beach':{
            'neighbors':['woods w/ cliff', 'merlock huts','shallow waters'],
            'about':'\n you are standing on the beach and you can see some huts to the north n/'+
            "and some wood to the west and some water to the east.",
            'stuff':[],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        'shallow waters':{
            'neighbors':['sandy beach'],
            'about':"\n you are standing in the water and see a nest with a egg and you can see \n"+
            "the beach to the west.",
            'stuff':['Gold egg'],
            'people':[{
                'name':'',
                'about':'',
                'sells':{},
                'buys':{}
                }],
            },
        
        "olga's house":{
            'neighbors':['black smith','dead forest','high cliff'],
            'about':'\n A small women sits in front of a very large house\n'+
                    'the house looks very old it has many celtic symbols\n'+
                    'and many other drudic symbols\n'+
                    'to the north is a small house with a forge outside\n'+
                    'to the east is a dead forest and to\n'+
                    ' the south is a Hill near a Cliff',
            'stuff':[],
            'people':[{
                'name':'Olga',
                'about':'',
                'sells':{},
                'buys':{'kids': {"amount": 5, "currency": 'gold'}}
                }],
            },
        
        'dead forest':{
            'neighbors':['river',"olga's house",'ginger bread house','grassy cliff'],
            'about':'\n you aproch a what looks like a dead forest.\n'+
                    'Hundreds of crows sit up high in the leafless trees\n'+
                    'there eyes fallow you as you walk deeper into there domain\n'+
                    'to the north is a river and to the west is a large house\n'+
                    'to the east is a Tail made of candy and to the south is a grassy feild',
            'stuff':[],
            'people':[],
            },
        
        'ginger bread house':{
            'neighbors':['small creek','dead forest','woods w/ river','dry cliff','entrance hall'],
            'about':"\n as you fallow a path of candy to a house made of candy deep in the woods\n"+
                    'there is a door into the house and paths made of candy leading in every direction',
            'stuff':['Candy'],
            'people':[],
            },
        
        'dining hall':{
            'neighbors':['entrance hall'],
            'about':'\n A large room made of candy, a table made of candy,\n '+
                    'even painting made of candy a door to the East ',
            'stuff':['candy'],
            'people':[],
            },
        
        'entrance hall':{
            'neighbors':['ginger bread house','dining hall','kitchen','alchemy room'],
            'about':'\n A large hall leading into a house made of candy\n'+
                    'there is a door to the north and rooms to the east, south, and west',
            'stuff':['Candy'],
            'people':[],
            },
        
        'kitchen':{
            'neighbors':['entrance hall','libary'],
            'about':'\n a room made of cobblestone there is a large cooking stove\n'+
                    'there is something in the stove cooking',
            'stuff':['Meat Pie','Golden Fork'],
            'people':[],
            },
        
        'bedroom':{
            'neighbors':['alchemy room'],
            'about':'',
            'stuff':[],
            'people':[],
            },
        
        'alchemy room':{
            'neighbors':['bedroom','library','entrance hall','basement'],
            'about':"\n you look around the room and see bottles of all colors and sizes \n"+
            "and there are four door you can see one to the north one to the south \n"+
            "one to the west and one to the east",
            'stuff':[],
            'people':[],
            },
        
        'library':{
            'neighbors':['alchemy room'],
            'about':'\n you look around and see shelves of books lots and lots of books \n'+
            "and you can see a door to the west.",
            'stuff':[],
            'people':[],
            },
        
        'basement':{
            'neighbors':['alchemy room'],
            'about':'\n you walk down a dark staircase into the wiches basement \n' +
                    'you feel around for a candle and strike a match \n' +
                    'you see two little fat Kids who are tied up with lolipops gaging them\n' +
                    'you can hear them screaming through the lolipop for help\ n'
                    'you can turn back now a get out of here while you still can',
            'stuff':['Kids'],
            'people':[],
            },
        
        'woods w/ river':{
            'neighbors':['above cavern','ginger bread house','big waves','muddy cliff','small creek'],
            'about':"\n A Forest of dead trees and insects with a candy path cutting through\n"+
                    'untell the path reaches a large Stream were it turns into a cobble stone Bridge\n'+
                    'the river continues untell it passes down the beach into the ocean \n'+
                    'you could fallow the river up to the North Weast, East into the sea,\n'+
                    'you could fallow the path West toward a cottege in the woods,\n'+
                    'or head North along the path before it turns into woods',
            'stuff':[],
            'people':['Troll'],
            },
        
        'big waves':{
            'neighbors':['woods w/ river'],
            'about':'',
            'stuff':[],
            'people':['Shark'],
            },
        
        'high cliff':{
            'neighbors':["olga's house",'grassy cliff'],
            'about':'\n you can see farther from this hill near a cliff\n'+
                    'you can see The town of Zik form here you walk down the hill\n'+
                    'and look at the cliff ' + random_cliff_text() +
                    'you can head North to a large house \n' +
                    'and east to another cliff',
            'stuff':[],
            'people':[],
            },
        
        'grassy cliff':{
            'neighbors':['dead forest','high cliff','dry cliff'],
            'about':'\n you are standing in a feild of grass as high as your head you walk a bit south\n'+
                    'Where you see you are standing on a cliff when you yip and say '+ ' " ' + random_cliff_text() + ' "' +
                    'you get up on a rock and can see that you can head North to a forest of dead trees,\n'+
                    'or head West or East to another cliff',
            'stuff':[],
            'people':[],
            },
        
        'dry cliff':{
            'neighbors':['ginger bread house','grassy cliff','muddy cliff'],
            'about':'\n The land here is very weird the ground is dry\n'+
                    'not a animal in sight you aproch the edge of the cliff\n' +
                    'the water looks nice like it wants to give you a big hug \n'+
                    random_cliff_text() + ' you can head North to a small cottage in the woods,\n'+
                    'West into a feild of grass, or East to another cliff in the distance',
            'stuff':[],
            'people':[],
            },
        
        'muddy cliff ':{
            'neighbors':['dry cliff','wodds w/ river'],
            'about':'\n the land here is slippery and slick \n' +
                    'your feet find it hard to find perches in the mud \n' +
                    'you fall and slide toward a Cliff face ' + random_cliff_text() +
                    '',
            'stuff':[],
            'people':[],
            },
        
        'hacker':{
            'neighbors':[],
            'about':'\n Hey what are you doing here wow now you have just sommoned \n'+
                    'CTHULU!!! WERE ALL DOOMED',
            'stuff':[],
            'people':[],
            },
         }
def map_item():
    import Map.py
    open (Map.py)
    
def create_player():
    return {
        'location': 'field',
        'inventory': ['map'],
        'Hunger': False ,
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
        return " You see: " + ', '.join(visible_stuff)


def render_player(world):
    '''
    Consume a world and produce a string describing the player
    '''
    inventory = world['player']['inventory']
    Gold = world['player']['Gold']
    Hunger = world['player']['Hunger']
    
    if Gold >= 39:
        world['status'] = "won"
        
    return "Gold: " + str(Gold) + " Hungry: " + str(Hunger)

def render_location(world):
    '''
    Consume a world and produce a string describing the location
    '''
    location = world['player']['location']
    here = world['map'][location]
    about = here['about']
    people = here['people']
    
    names = [p['name'] for p in people]

    message = f"You are in {location} \n{about}"
    try:
        if names[0]:
            for person in people:
                message += f"\n\n{person['name']}: {person['about']}\n\n"
        else:
            message += "\n\nNobody's here\n\n"
    except IndexError:
        #No People
        message += "\n\nNobody's here\n\n"
    
    return message
#    return ("You are in "+location+"\n"+
#            about +"\n")
    
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
    stuff = location['stuff']
    inventory = world['player']['inventory']
    
    for neighbor in neighbors:
        commands.append("goto " + neighbor)
        
    for item in stuff:
        if item == 'wheat' and not 'hoe' in inventory:
            continue
        if item == 'wool' and not 'shears' in inventory:
            continue
        if item == 'gold vein' and not 'pickaxe' in inventory:
            continue
        commands.append(f"pick up {item}")
        
    for person in world['map'][current_location]['people']:
        
        for item in person['sells']:
            item_data = person['sells'][item]
            commands.append(f"buy {item} for {item_data['amount']} {item_data['currency']}")
        for item in person['buys']:
            item_data = person['buys'][item]
            if item in inventory:
                commands.append(f"sell {item} for {item_data['amount']} {item_data['currency']}")
        
    if 'map' in inventory:
        commands.append("open map")
        
        
        
#    if current_location == 'farm house' and '1 gold coin' in stuff and '1 gold coin' not in inventory:
#        commands.append('pick up gold coin')
#        
#    if current_location == 'farm house' and 'bowl of soup' in stuff and 'bowl of soup' not in inventory:
#        commands.append('pick up bowl of soup')
#        
#    if current_location == 'field' and 'wheat' in stuff and 'wheat' not in inventory and 'hoe' in inventory:
#        commands.append('pick up wheat')
#        
#    if current_location == 'field' and 'hoe' in stuff and 'hoe' not in inventory:
#        commands.append('pick up hoe')
#        
#    if current_location == 'pasture' and 'wool' in stuff and 'wool' not in inventory and 'shears' in inventory:
#        commands.append('shear sheep')
#        
#    if current_location == 'pasture' and 'eggs' in stuff and 'eggs' not in inventory:
#        commands.append('pick up eggs')
        
    return commands

def goto(world, command):
    new_location = command[len('goto '):]
    world['player']['location'] = new_location
    
    if new_location == "the dark woods" or \
       new_location == "big waves" or \
       new_location == "cavern" or \
       new_location == "bedroom":
        world['status'] = "lost"
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
    current_location = world['player']['location']
    location = world['map'][current_location]
    neighbors = location['neighbors']
    inventory = world['player']['inventory']
    
    if command == "quit":
        world['status'] = 'quit'
        return 'you quit the game'
    
    if command.startswith('goto '):
        return goto(world, command)
    
    if command == 'open map':
        map_item()
        
    #command = 'pick up hoe'
    #location['stuff'] = ['wheat', 'hoe']
    
    if command.startswith('pick up '):
        index = location['stuff'].index(command[8:])
        item = location['stuff'].pop(index)
        inventory.append(item)
        
    if command.startswith('buy'):
        end = command.index("for ") - 1
        item = command[4:end]
        for person in location['people']:
            avail_to_buy = person['sells']
            if item in avail_to_buy.keys():
                if world['player']['Gold'] >= avail_to_buy[item]['amount']:
                    #able to buy
                    purchased = avail_to_buy.pop(item)
                    world['player']['inventory'].append(purchased)
                    world['player']['Gold'] -= purchased['amount']
                else:
                    #not able to buy
                    return "not enough gold"
                
    if command.startswith('sell'):
        end = command.index("for ") - 1
        item = command[5:end]
        for person in location['people']:
            avail_to_sell = person['buys']
            if item in avail_to_sell.keys():
                item_data = avail_to_sell[item]
                #remove item from inventory
                pos = world['player']['inventory'].index(item)
                popped_item = world['player']['inventory'].pop(pos)
                #adds item to vendors selling list
                person['sells'][item] = item_data
                #gives gold to player
                world['player']['Gold'] += item_data['amount']
            
                
    
        
    return 'you chose ' + command

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
    
def render_ending_lost(world):
    
    current_location = world['player']['location']
    location = world['map'][current_location]
    
    if current_location == 'the dark woods':
        return ("As you walk through the wood you see some small buildings in the \n" +
                "trees as you get close you hear a loud thump then you black out. You lose.")
         
    if current_location == 'cavern' :
        return("you walk into a dark Cavern as red eyes light up across the walls. You lose.")
    
    if current_location == 'bedroom' :
        return("as you walk in the dark room you see someone and they \n"+
            "see you and thay run and grab you and tie you up and throw you down the basement. You lose.")
    
    if current_location == 'big waves' :
        return("as you wade out into the water you see a shark fin pop out of the water. You lose\n")
    

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
    print('\n List of Commands: \n')
    for option in options:
        print(option)
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
#assert_equal("== Ben ? ==" in render_introduction(), True)
# We should have 5 lines of text
#assert_equal(render_introduction().count("\n"),7)
# Make sure it explicitly mentions "your house" to set up the punchline,
#   that you've been in your own house the entire game.
#assert_equal("old bones" in render_introduction().lower(), True)



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
