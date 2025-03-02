
import json


class room:
    def __init__(self):
        self.name = ""
        self.inroom = ""
        self.fight = 0
        self.option1 = ["", None]
        self.option2 = ["", None]
        self.option3 = ["", None]
        
    def __str__(self):
        return f'{self.name}\n{self.inroom}'