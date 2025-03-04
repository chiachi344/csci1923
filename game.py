import json
import random
from rooms import room
from player import player


class game:
    def __init__(self):
        self.current = "room01"
        self.player = player()
        self.rooms_d = {}
        self.count_rest = 3
        self.fight_pass = False
        
    def game_write(self):
        '''
        Purpose: write the current room and how many time user can rest in to user_data, and call the write_player
        Parameter(s): nothing
        Return Value: nothing
        '''
        rest_and_room = [self.current, self.count_rest, self.fight_pass]
        with open("user_data.json", "w") as outfile:
            json.dump(rest_and_room, outfile)
            outfile.close()
            # print(rest_and_room)
            
        self.player.write_player()
        
    def game_reset(self):
        '''
        Purpose: reset the user_data and call reset_player()
        Parameter(s): nothing
        Return Value: nothing
        '''
        rest_and_room = ["room01", 3, False]
        with open("user_data.json", "w") as outfile:
            json.dump(rest_and_room, outfile)
            outfile.close()
        self.player.reset_player()
        self.current = "room01"
        self.count_rest = 3
        self.fight_pass = False
        
        
    def game_read(self):
        '''
        Purpose: read the file user_data and call read_player
        Parameter(s): nothing
        Return Value: nothing
        '''
        rest_and_room = []
        with open('user_data.json', 'r') as openfile:
            rest_and_room = json.load(openfile)
            openfile.close()
        self.current = str(rest_and_room[0])
        self.count_rest = rest_and_room[1]
        self.fight_pass = rest_and_room[2]
        self.player.read_player() 


    def game_opening(self):
        '''
        Purpose: Game start!! let user can move, fight and rest
        Parameter(s): nothing
        Return Value: nothing
        '''
        classes_list = ["Saber", "Archer", "Lancer", "Caster", "Assassin"]
        classes_d = {}
        with open('classes_d', 'r') as openfile:
            classes_d = json.load(openfile)
            # for key, value in classes_d.items():
            #     print(f"{key}: {value}")
            openfile.close()
                
        print("\nHello, player! Please choose your class.\n")
        print("You will have the following options:")
        num_show = 1
        for show_classes in classes_d:
            print(f"{num_show}. {show_classes}: HP:{classes_d[show_classes]['HP']} ATK:{classes_d[show_classes]['ATK']} ", end = "")
            print(f"SEPPD:{classes_d[show_classes]['SPEED']} LUK:{classes_d[show_classes]['LUK']}")
            num_show += 1
        
        user_input_class = 10
        while True:
            try:
                user_input_class = int(input("\nPlease enter a number from 1 to 5 to select your desired class: "))
            except ValueError:
                print("Sorry, pleace try again.")
                continue
            if user_input_class <= 0 or user_input_class >= 6:
                print("Sorry, your input number is too big or small. Pleace try again")
                continue
            else:
                break
            
        user_input_class -= 1
        # print(classes_list[user_input_class])
        player_class_str = classes_list[user_input_class]
        self.player.name = player_class_str
        self.player.HP = classes_d[player_class_str]["HP"]
        self.player.ATK = classes_d[player_class_str]["ATK"]
        self.player.SPEED = classes_d[player_class_str]["SPEED"]
        self.player.LUK = classes_d[player_class_str]["LUK"]    
        #-----------------------------end-----------------------------
        
    def set_rooms(self):
        '''
        Purpose: I don't want to put every thing inside of init so I use this method to set the rooms
        Parameter(s): self
        Return Value: nothing
        '''            
        room_data = {}
        with open('rooms_data', 'r') as openfile:
            room_data = json.load(openfile)
            openfile.close()
        
        for room_name, room_info in room_data.items():
            new_room = room()
            new_room.name = room_name
            new_room.inroom = room_info["inroom"]
            new_room.fight = room_info["fight"]
            
            if "option1" in room_info:
                new_room.option1 = room_info["option1"]
            if "option2" in room_info:
                new_room.option2 = room_info["option2"]
            if "option3" in room_info:
                new_room.option3 = room_info["option3"]

            self.rooms_d[room_name] = new_room
        #-----------------------------end-----------------------------
        
    def now_fight(self):
        '''
        Purpose: now is fight time. randomly pick an enemy and let the enemy fight will use. Note :LUK
        Parameter(s): self
        Return Value: 0
        '''
        drop_item = ["branches", "monster teeth", "smelly meat", "expired potion", "cabbage"]
        enemies_list = ["slime", "goblin", "skeleton", "troll", "orc"]
        enemies_d = {}
        
        with open('enemies_d', 'r') as openfile:
            enemies_d = json.load(openfile)
            openfile.close()
        
        now_enemy = {
            "name": "emply",
            "HP": 5,
            "ATK": 0,
            "money": 0,
        }
        
        enemy_name = enemies_list[random.randint(0, self.rooms_d[self.current].fight)]

        if self.current == "room51" or self.current == "room52":
            enemy_name = enemies_list[4]
            
        now_enemy["name"] = enemy_name
        now_enemy["HP"] = enemies_d[enemy_name]["HP"]
        now_enemy["ATK"] = enemies_d[enemy_name]["ATK"]
        now_enemy["money"] = enemies_d[enemy_name]["money"]
        
        print(f"\nYou see {now_enemy['name']} in front. It seems that in order to move on, you have no choice but to fight.")
        
        user_type = ""
        
        while now_enemy["HP"] > 0 or user_type != "3":
            print("You now have three options: 1. Light attack 2. Heavy attack 3. Escape")
            print(f"You now have {self.player.HP} HP.")
            while user_type not in ["1", "2", "3"]:
                user_type = str(input("Please type your choice (1, 2, or 3): "))
                
                if user_type not in ["1", "2", "3"]:
                    print("Your input is not vaild, pleace try again.\n")
                    
                if user_type == "3":
                    print(f"You choose not to fight the {now_enemy['name']}. You ran away.")
                    break
                
            if user_type == "3":
                break
            
            now_LUK = random.randint(0, self.player.LUK + 75)
            you_DMG = 0

            if user_type == "1" and now_LUK >= 50:
                you_DMG = self.player.SPEED * random.randint(8, self.player.ATK * 2)
                print("critical hit!!")
                
            elif user_type == "2" and now_LUK >= 50:
                you_DMG = random.randint(8, self.player.ATK * 3)
                print("critical hit!!")

            elif user_type == "1":
                you_DMG = self.player.SPEED * random.randint(3, self.player.ATK)

            elif user_type == "2":
                you_DMG = random.randint(4, self.player.ATK * 2)
                
            now_enemy["HP"] -= you_DMG
            print(f"\nYour attack caused {you_DMG} damage") 
            
            if now_enemy["HP"] < 1:
                print(f"\nWIN!! {now_enemy['name']} is died")
                print(f"You get {now_enemy['money']} gold coins from {now_enemy['name']} ")
                self.player.money += now_enemy["money"]
                # 50 50 get item
                get_item = random.randint(0, 1)
                if get_item == 1:
                    random_drop = drop_item[random.randint(0, len(drop_item) - 1)]
                    self.player.inventory.append(random_drop)
                self.player.list_inventory()
                break
            
            self.player.HP -= random.randint(0, now_enemy["ATK"])
            
            if self.player.HP < 1:
                break
            print(f"{now_enemy['name']}'s attack caused {now_enemy['ATK']} damage to you. You have {self.player.HP} HP left")
            
            user_type = "0"
            
        print("\nfight end")
        #-----------------------------end-----------------------------
        
                
    def print_room(self):
        '''
        Purpose: just see what inside the rooms_d 
        '''            
        for key, value in self.rooms_d.items():
            print(key)
            print(value)
        #-----------------------------end-----------------------------
            
            
    def game_start(self):
        '''
        Purpose: Game start!! let user can move, fight and rest
        Parameter(s): self
        Return Value: Return "success" or "fail" to confirm whether the adventure was successful.
        '''
        self.game_read()
        self.set_rooms()
        
        if self.current == "room01" and self.player.name == "room01":
            self.game_opening()
            print("\n-------------story time-------------")
            print("\nYou are an adventurer. Today, you have accepted a quest: a mysterious green creature has appeared in a village.")
            print("Please head to the village, investigate the situation, and eliminate the unknown creature.")
            
            print("\nYou arrive at the village and search the surrounding area, eventually discovering a suspicious cave.")
            print("The massive footprints at the cave entrance indicate that a creature larger than a human lives inside.")
            print("However, this does not deter you. Instead, you bravely step into the cave.\n")
            
        while self.current != "room53":
            Enter_some = input("Press any key to see if there is an enemy in the front:  ")
            Enter_some = Enter_some
            
            if self.rooms_d[self.current].fight != 0 and self.fight_pass == False:
                # print("yes fight!!!!!!!!!!")
                # print(self.rooms_d[self.current].fight)
                self.now_fight()
            else:
                print("No enemy in the front")
            
            
            self.fight_pass = False
            # break the while loop adn return fail
            if self.player.HP < 1: # died stop while loop
                return False
            
            print(f"You now have {self.player.HP} HP.")
            print("Next, you can...")
            print(f"{self.rooms_d[self.current].option1[0]}")
            
            if self.rooms_d[self.current].option2[1] != None:
                print(f"{self.rooms_d[self.current].option2[0]}")
            if self.rooms_d[self.current].option3[1] != None:
                print(f"{self.rooms_d[self.current].option3[0]}")
            if self.count_rest > 0:
                print(f"4. Rest and you can take {self.count_rest} more breaks")
            
            user_type = "0"
            
            while user_type not in ["1", "2", "3", "4", "reset", "exit"]:
                user_type = str(input("Please type your choice (1, 2, ,3 , 4, reset, exit): "))

                if user_type not in ["1", "2", "3", "4", "reset", "exit"]:
                    print("Your input is not vaild, pleace try again.\n")
                elif self.rooms_d[self.current].option2[1] == None and user_type == "2":
                    print("Your input is not vaild, pleace try again.\n")
                    user_type = "error"
                elif self.rooms_d[self.current].option3[1] == None and user_type == "3":       
                    print("Your input is not vaild, pleace try again.\n")
                    user_type = "error"
                elif user_type == "4" and self.count_rest > 0:
                    print("You decided to take a break")
                    HP_add = random.randint(20, 30)
                    if self.player.HP < 50:
                        HP_add += 30
                    self.player.HP += HP_add
                    print(f"You feel your body filled with strength, and your health has been restored by {HP_add}")
                    print(f"You now have {self.player.HP} HP.")
                    self.count_rest -= 1
                    print(f"You can take {self.count_rest} more breaks")
                    
                    user_type = "error"
                elif user_type == "4" and self.count_rest == 0:
                    print("Your input is not vaild, pleace try again.\n")
                    user_type = "error"
                    
                if user_type == "1":
                    self.current = self.rooms_d[self.current].option1[1]
                    # print(current_room)
                elif user_type == "2":
                    self.current = self.rooms_d[self.current].option2[1]
                    # print(current_room)
                elif user_type == "3":
                    self.current = self.rooms_d[self.current].option3[1]
                    # print(current_room)
                elif user_type == "reset":
                    self.game_reset()
                    print("You reset the game\n")
                    again = self.game_start()
                    return again
                elif user_type == "exit":
                    self.fight_pass = True
                    self.game_write()
                    self.current = "exit"
                    return False
            
        return True
        #-----------------------------end-----------------------------
    def ending(self, s_or_f):
        '''
        Purpose: test how much money the player got, and see if the player died or not. give different outcome(Ending)
        Parameter(s): self
        Return Value: 0
        '''
        if self.current == "exit":
            return
        
        
        print(f"You got ${self.player.money} from the monster\n")
        self.player.list_inventory()
        print("----------------------------------end----------------------------------")
        
        if self.player.money > 100 and s_or_f == True:
            print("You flawlessly completed the mission, earning the gratitude of the villagers and a generous reward in return.")
            print("However, your next adventure is already waiting for you.\n")
        elif s_or_f == True:
            print("You completed the quest, but later that day, villagers reported some monsters still lurking in the area.")
            print("Your mission was deemed a failure, and you were even required to pay compensation.\n")
        elif s_or_f == False:
            print("\nYou failed. Although you considered yourself a lucky person, it seems that the goddess of fortune has turned her gaze away from you today.")
            print("As you miserably fled back home, you discovered that you had taken an arrow to the knee. Because of this, you retired from the adventurer's life.\n")
            
        self.game_reset()
        #----------------------------------end----------------------------------
                
        
                
            


if __name__ == "__main__":
    
    game_go = game()
    # game_go.game_opening()
    #game_go.game_write()
    # game_go.game_read()
    # print(game_go.player) 
    
    # game_go.set_rooms()
    # game_go.print_room()
            
    s_or_f = game_go.game_start()
    game_go.ending(s_or_f)
            
