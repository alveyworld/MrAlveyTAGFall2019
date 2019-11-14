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
__author__ = "21gilmoethm@washk12.org"
__title__ = "Name of your game goes here"
__description__ = "Replace this with a quick description of your game."

# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"

import time
import random
import math


##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.

'''
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

    Location:
        about (str): A sentence that describes what this location 
                     looks like.
        neighbors (list[str]): A list of the names of other places 
                               that you can reach from this 
                               location.
        stuff (list[str]): A collection of things available at 
                           this location.
'''

##### 3) Core Game Functions #####
# Implement the following to create your game.

moves = {
    "scratch": {"name": "scratch", "power": 40, "type": "normal", "category": "physical", },
    "ember": {"name": "ember", "power": 40, "type": "fire", "category": "special"},
    "fire fang": {"name": "fire fang", "power": 65, "type": "fire", "category": "physical"},
    "flamethrower": {"name": "flamethrower", "damage": 90, "type": "fire", "category": "special"},
    "tackle": {"name": "tackle", "power": 40, "type": "normal", "category": "physical"},
    "bubble": {"name": "bubble", "power": 40, "type": "water", "category": "special"},
    "bite": {"name": "bite", "power": 66, "type": "dark", "category": "physical"},
    "hydro pump": {"name": "hydro pump", "power": 110, "type": "water", "category": "special"},
    "vine whip": {"name": "vine whip", "power": 45, "type": "grass", "category": "physical"},
    "razor leaf": {"name": "razor leaf", "power": 55, "type": "grass", "category": "physical"},
    "solar beam": {"name": "solar beam", "power": 120, "type": "grass", "category": "special"},
    "quick attack": {"name": "quick attack", "power": 30, "type": "normal", "category": "special"},
    "iron tail": {"name": "iron tail", "power": 65, "type": "steel", "category": "physical"},
    "thunder": {"name": "thunder", "power": 90, "type": "electric", "category": "special"},
    "defense curl": {"name": "defense curl", "power": 0, "type": "normal", "category": "status", "effect": {"self": {"defense": 1}}},
    "screech": {"name": "screech", "power": 0, "type": "normal", "category": "status", "effect": {"other": {"defense": -1}}}
    }

def get_moves(string):
    move_list = []
    for name in string.split(", "):
        move_list.append(moves[name])
    return move_list

def format_base(health, attack, defense, spattack, spdef, speed):
    # names = ['health', 'attack', 'defense', 'spattack', 'spdef', 'speed']
    stats = {'health': health, 'attack': attack, 'defense': defense, 'spattack': spattack, 'spdef': spdef, 'speed': speed}
    return stats

def base_to_real(base, level):
    stats = {}
    for name, value in base.items():
        if name == 'health':
            stats[name] = (value * 2 * level) / 100 + level
        else:
            stats[name] = (value * 2 * level) / 100 + 5
    return stats
        
def create_mon(name, t, level, base_stats, moves):
    '''
    returns mon(dict): {name, level, type, base stats, moves, stats}
    '''
    stats = base_to_real(base_stats, level)
    mon = {'name': name.title(), 'level': level, 'type': t, 'base': base_stats, 'moves': moves, 'stats': stats}
    return mon

def refresh(mon):
    stats = base_to_real(mon['base'], mon['level'])
    mon['stats'] = stats

def level_up(mon):
    prev_health = mon['stats']['health']
    mon['level'] += 1
    stats = base_to_real(mon['base'], mon['level'])
    stats['health'] = prev_health
    mon['stats'] = stats
    return mon
    
starters = {
#    'charmander': {"name": "Charmander", "type": ["fire"], "level": 5, "stats": format_base(39,52,43,60,50,65), "moves": get_moves("scratch, ember, fire fang, flamethrower")},
    'charmander': create_mon('charmander', 'fire', 5, format_base(39,52,43,60,50,65), get_moves("scratch, ember, fire fang, flamethrower")),
    'squirtle': create_mon('squirtle', 'water', 5, format_base(44,48,65,50,64,43), get_moves("tackle, bubble, bite, hydro pump")),
    'bulbasaur': create_mon('bulbasaur', 'grass', 5, format_base(45,49,49,65,65,45), get_moves("tackle, vine whip, razor leaf, solar beam"))
#    'squirtle': {"name": "Squirtle", "type": ["water"], "level": 5, "stats": format_base(44,48,65,50,64,43), "moves": get_moves("tackle, bubble, bite, hydro pump")},
#    'bulbasaur': {"name": "Bulbasaur", "type": ["grass"], "level": 5, "stats": format_base(45,49,49,65,65,45), "moves": get_moves("tackle, vine whip, razor leaf, solar beam")}
    }

pokemon = [
#    "pikachu": {"name": "Pikachu", "type": ["electric"], "level": 5,"stats": format_base(35,55,40,50,50,90), "moves": get_moves("tackle, quick attack, iron tail, thunder")}
    create_mon('pikachu', 'electric', 5, format_base(35,55,40,50,50,90), get_moves("tackle, quick attack, iron tail, thunder")),
    create_mon('charmander', 'fire', 5, format_base(39,52,43,60,50,65), get_moves("scratch, ember, fire fang, flamethrower")),
    create_mon('squirtle', 'water', 5, format_base(44,48,65,50,64,43), get_moves("tackle, bubble, bite, hydro pump")),
    create_mon('bulbasaur', 'grass', 5, format_base(45,49,49,65,65,45), get_moves("tackle, vine whip, razor leaf, solar beam"))
    ]

gyms = {
    "Pewter City": [create_mon('geodude', ['rock', 'ground'], 12, format_base(40,80,100,30,30,20), get_moves("tackle, defense curl")),
                    create_mon('onix', ['rock', 'ground'], 14, format_base(35,45,160,30,45,70), get_moves("tackle, screech"))]
    }

def health(pokemon):
    bar = ''
    total = base_to_real(pokemon['base'], pokemon['level'])['health']
    current = pokemon['stats']['health']
    percent = current/total
    percent *= 15
    for i in range(15):
        if i < percent:
            bar = bar + "-"
    return bar
    
def say(name, strings):
    for phrase in strings:
        print(f"\n>{name}: {phrase}")
        time.sleep(1)
        
def random_encounter():
    return [pokemon[0].copy()]

def render_introduction():
    '''
    Create the message to be displayed at the start of your game.
    
    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return '''
    Welcome to the wold of Pokemon
    Just play the game it's not that hard
    '''

def create_world():
    '''
    Creates a new version of the world in its initial state.
    
    Returns:
        World: The initial state of the world
    '''
    world = {"status": "playing", 
            "player": {"location": "Home", "inventory": [], "party": [starters['squirtle']], "battle": None, "traveling": None, "city": "Pallet Town", "action": None},
            "map": {"Pallet Town": {"about": "first city",
                                    "neighbors": ["Viridian City"],
                                    "stuff": ["travel"]},
                    "Viridian City": {"about": "second city",
                                      "neighbors": ["Pallet Town", "Viridian Forest"],
                                      "stuff": ["challenge gym", "pokemart", "pokecenter", "travel"]},
                    "Viridian Forest": {"about": "forest",
                                        "neighbors": ["Viridian City", "Pewter City"],
                                        "stuff": ["battle", "trainer", "travel"]},
                    "Pewter City": {"about": "pewter city",
                                    "neighbors": ["Mt Moon", "Viridian Forest"],
                                    "stuff": ["challenge gym", "pokemart", "pokecenter", "travel"]},
                    "Mt Moon": {"about": "Mt Moon",
                                "neighbors": ["Pewter City", "Saffron City"],
                                "stuff": ["battle", "travel"]},
                    
                    "Home": {"about": "players house",
                             "neighbors": [], "stuff":
                             ["sleep", "go outside"]},
                    "Professors Lab": {"about": "Professors Lab",
                                       "neighbors": [], "stuff":
                                       ["go outside"]},
                    "PokeMart": {"about": "shop",
                                 "neighbors": [],
                                 "stuff": ["buy", "sell", "go outside"]},
                    "PokeCenter": {"about": "pokecenter",
                                   "neighbors": [],
                                   "stuff": ["heal", "go outside"]}}}
    return world

def render(world):
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.
    
    Args:
        world (World): The current world to describe.
    
    Returns:
        str: A textual description of the world.
    '''
    location = world['player']['location']
    battle = world['player']['battle']
    message = ""

    if world['player']['traveling']:
        message = "\n---travel where?---"
    elif world['player']['battle']:
        battle_mon = battle[0]
        pokemon = world['player']['party'][0]
        opp_bar = health(battle_mon)
        while(len(opp_bar) < 15):
            opp_bar = " " + opp_bar

        message = f'''\n---in battle---\n
                          {opp_bar}[{battle_mon['name']} {battle_mon['level']}]
                          
    [{pokemon['name']} {pokemon['level']}]{health(pokemon)}
    '''
    else:
        message = f"\n---at {location}---"
    return message

#------OPTIONS-------

def battle_options(world):
    action = world['player']['action']
    if action == 'fight':
        options = [move['name'] for move in world['player']['party'][0]['moves']]
        world['player']['action'] = None
    elif action == 'bag':
        options = [item['name'] for item in world['player']['inventory'][0]['moves']]
    elif action == 'pokemon':
        pass
    else:
        options = ['fight', 'bag', 'pokemon', 'run']
    return options

def travel_options(world):
    location = world['player']['location']
    options = world['map'][location]['neighbors']
    return options

def special_options(world):
    location = world['player']['location']
    options = []
    if(location == 'Professors Lab' and not world['player']['party']):
        options = ['charmander', 'bulbasaur', 'squirtle']
    return options

def get_options(world):
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.
    
    Args:
        world (World): The current world to get options for.
    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    location = world['player']['location']
    if(special_options(world)):
        return special_options(world)
    
    if(world['player']['battle']):
        options = battle_options(world)
    elif(world['player']['traveling']):
        options = travel_options(world)
    else:
        options = world['map'][location]['stuff']
    return options

#-------BATTLE---------

def calc_damage(attacker, defender, move):
    level_mod = attacker['level'] * 2 / 5 + 2
    attack_stat = attacker['stats']['attack'] if move['category'] == 'physical' else attacker['stats']['spattack']
    def_stat = defender['stats']['defense'] if move['category'] == 'physical' else attacker['stats']['spdef']
    raw = level_mod * move['power'] * attack_stat / def_stat / 50
    mod = 1
    if move['type'] in attacker['type']:
        mod *= 1.5
    return round(raw * mod)

def attack(world, attack, from_player):
    defender = world['player']['party'][0] if not from_player else world['player']['battle'][0]
    attacker = world['player']['party'][0] if from_player else world['player']['battle'][0]

    try:
        for stat, effect in attack['effect']['self'].items():
            if(effect == 1):
                attacker['stats'][stat] *= 1.5
            elif(effect == -1):
                attacker['stats'][stat] *= .66
    except:
        pass
    try:
        for stat, effect in attack['effect']['other'].items():
            if(effect == 1):
                defender['stats'][stat] *= 1.5
            elif(effect == -1):
                defender['stats'][stat] *= .66
    except:
        pass
    
    damage = calc_damage(attacker, defender, attack)
    defender['stats']['health'] -= damage
    
    print(f"\n{attacker['name']} used {attack['name']}")
    print(f"\nIt did {damage} damage!")
    
    if(defender['stats']['health'] <= 0):
        faint(world, defender)
        
def faint(world, pokemon):
    print(f"\n{pokemon['name']} fainted!")
    battle = world['player']['battle']
    if(pokemon == world['player']['battle'][0]):
        world['player']['battle'].pop(0)
        if(len(battle) > 1):
            print(f"{battle[0]['name']} was sent out!")
        current_mon = world['player']['party'][0]   
        print(f"\n{current_mon['name']} leveled up!")
        level_up(world['player']['party'][0])
    if(pokemon == world['player']['party'][0]):
        print("your mon fainted")
    

def battle(world, command):
    moves = [move['name'] for move in world['player']['party'][0]['moves']]
    
    if command in moves:
        for move in world['player']['party'][0]['moves']:
            if move['name'] == command:
                attack(world, move, True)
                try:
                    attack(world, random.choice(world['player']['battle'][0]['moves']), False)
                except IndexError:
                    #no battle
                    pass
        
        
    if(command == 'fight'):
        world['player']['action'] = 'fight'
    elif(command == 'run'):
        world['player']['battle'] = False
    elif(command == 'pokemon'):
        world['player']['action'] = 'pokemon'
    elif(command == 'bag'):
        world['player']['action'] = 'bag'
        
#---------UPDATE----------

def update_battle(world, command):
    if(world['player']['battle']):
        battle(world, command)
    elif(command == "battle"):
        world['player']['battle'] = random_encounter()
    elif(command == 'challenge gym'):
        world['player']['battle'] = gyms[world['player']['location']]

def update_travel(world, command):
    if(command == "travel"):
        world['player']['traveling'] = True
    elif(command in world['map']):
        world['player']['traveling'] = False
        world['player']['location'] = command
        world['player']['city'] = command
        world['player']['battle'] = random_encounter()
    elif(command == 'go outside'):
        world['player']['location'] = world['player']['city']
    elif(command == 'pokemart'):
        world['player']['location'] = 'PokeMart'
    elif(command == 'pokecenter'):
        world['player']['location'] = 'PokeCenter'
    
def update_special(world, command):
    if(command == 'Viridian City' and not world['player']['party']):
        world['player']['location'] = 'Professors Lab'
        world['player']['traveling'] = False
        say("Proffessor", ["Wait!",
                           "You can't go out there just yet!",
                           "You need a Pokemon"])
    elif(command in starters):
        world['player']['party'].append(starters[command])
        say('Professor', ["Oh!",
                          f"So you pick {command}!",
                          "Good choice!",
                          "Now go and start your Pokemon Journey!"])
    elif(command == 'heal'):
        for mon in world['player']['party']:
            mon = refresh(mon)

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
    if(command == 'quit'):
        world['status'] = command
    update_special(world,command)
    update_battle(world, command)
    update_travel(world, command)

def render_ending(world):
    '''
    Create the message to be displayed at the end of your game.
    
    Args:
        world (World): The final world state to use in describing the ending.
    
    Returns:
        str: The ending text of your game to be displayed.
    '''

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
    
    chosen = ""
    while(chosen not in options):
        for command in options:
            print(command)
        chosen = input("\nWhat would you like to do? : ")
    return chosen
    

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
        update(world, command)
    print(render_ending(world))

if __name__ == '__main__':
    main()
