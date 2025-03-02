
import json

class player:
    def __init__(self):
        self.name = "room01"
        self.HP = 0
        self.ATK = 0
        self.SPEED = 0
        self.LUK = 0
        self.money = 0
        self.inventory = []
    
    def write_player(self):
        play_d = {
            "name": self.name, 
            "HP": self.HP,
            "ATK": self.ATK,
            "SPEED": self.SPEED,
            "LUK": self.LUK,
            "money": self.money,
            "inventory": self.inventory,
        }
        
        with open("play_d", "w") as outfile:
            json.dump(play_d, outfile, indent=4)
            
    def reset_player(self):
        play_d = {
            "name": "room01", 
            "HP": 0,
            "ATK": 0,
            "SPEED": 0,
            "LUK": 0,
            "money": 0,
            "inventory": [],
        }
        with open("play_d", "w") as outfile:
            json.dump(play_d, outfile, indent=4)
        
            
    def read_player(self):
        play_d = {}
        with open('play_d', 'r') as openfile:
            play_d = json.load(openfile)
        
        self.name = play_d["name"]
        self.HP = play_d["HP"]
        self.ATK = play_d["ATK"]
        self.SPEED = play_d["SPEED"]
        self.LUK = play_d["LUK"]
        self.money = play_d["money"]
        self.inventory = play_d["inventory"]
            
            
    def add_to_inventory(self, item):
        '''
        Purpose: add something to inventory, but the name is too long, this makes me think I'm stupid
        Parameter(s): self
        Return Value: 0
        '''
        self.inventory.append(item)
    
    def list_inventory(self):
        '''
        Purpose: print the inventory
        Parameter(s): self
        Return Value: 0
        '''
        print("You now have [", end="")
        for key in self.inventory:
            print(f"{key} ", end="")
        print("] in your bag.")
    
    def __str__(self):
        data = f"Name:{self.name} HP:{self.HP} ATK:{self.ATK} SPEED:{self.SPEED} LUK:{self.LUK}\n"
        data += f'{self.inventory}'
        return data