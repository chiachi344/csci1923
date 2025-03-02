# csci1923

# Adventure Game

__Introduction__

This is a text-based adventure game where the player explores various rooms, encounters enemies, and makes strategic decisions to complete the game. The game supports saving and loading progress, allowing the player to resume their journey.

## How to Play

- You usually only need the numbers 1 to 5 on your keyboard to control your character.
- Once you start the game, you can exit anytime by entering "exit".
- The game will automatically save your current room and character status.
- Alternatively, you can enter "reset" to restart the entire game.

__Project Structure__

```
/adventure_game
│── game.py         # Main script to run the game
│── adventure.py    # Controls the adventure process and game loop
│── player.py       # Manages player data
│── rooms.py        # Manages room structures
│── classes_d.json  # Stores data for selectable classes
│── enemies_d.json  # Stores data for enemies
│── rooms_data.json # Stores data for rooms
│── play_d.json     # Stores the player's current progress
│── user_data.json  # Stores saved progress and rest count
│── README.md       # Game instructions
```




