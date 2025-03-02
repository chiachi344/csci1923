
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