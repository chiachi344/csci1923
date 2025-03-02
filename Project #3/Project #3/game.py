import json
import random
import rooms
import player


def game_opening():
    '''
    Purpose: Game start!! let user can move, fight and rest
    Parameter(s): nothing
    Return Value: player class
    '''
    classes_list = ["Saber", "Archer", "Lancer", "Caster", "Assassin"]
    classes_d = {}
    with open('Project #3\classes_d', 'r') as openfile:
        classes_d = json.load(openfile)
        for key, value in classes_d.items():
            print(f"{key}: {value}")
            
            
            
            
            


if __name__ == "__main__":
    game_opening()
            
            
            
