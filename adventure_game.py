import random
import time

class Item:
    # To create an item give it a name and how much damage it does. 
    # Players collect items to attack the animal. Every time a player kills an animal they get a new item
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def __repr__(self) -> str:
        return f"{self.name}({self.damage} damage)"

class Animal:
    # To create an animal specify its name, hitpoints, damage and reward item.
    def __init__(self, name, hitpoints, damage, item: Item) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.item = item

    # Attacks the player. There is a 50% chance the animal misses.
    def attack(self, player, player_power_up=None):
        if player_power_up == "super agility":
            hit_or_miss = random.randint(1, 4)
        elif player_power_up == None:    
            hit_or_miss = random.randint(1, 2)
        if hit_or_miss == 1:
            player.hitpoints = player.hitpoints - self.damage
            print(f"The {self.name} with {self.hitpoints} hitpoints has attacked {player.name} for {self.damage} damage!")
            if player.hitpoints > 0:
                print(f"{player.name} has {player.hitpoints} hitpoints remaining.")
                print("----------------------------------------------------------")
        else:
            print(f"The {self.name} has missed {player.name}! No damage done!")
            print("----------------------------------------------------------")

class Room:
    # To create a room specify the name and the animal object inside it.
    def __init__(self, name, animal: Animal) -> None:
        self.name = name
        self.animal = animal

class Player:
    # To create a player specify its name and their hitpoints
    def __init__(self, name, hitpoints) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.items: list[Item] = []
        self.power_ups = ["health boost", "super agility", "extra damage"]

    # Shows which room the player enters.
    def enter_room(self, room: Room):
        print(f"\n{self.name} has entered the {room.name} room...\n")

    # Player attacks the animal with a random item from their items list.
    def attack(self, animal: Animal, player_power_up=None, items=None):
        if player_power_up == "extra damage" and items == None:
        # If player uses extra damage, creates a new item list with 25% more damage
            self.buffed_items = []
            for item in self.items:
                self.buffed_items.append(Item(item.name, item.damage * 1.25))
            buffed_item: Item = random.choice(self.buffed_items)
            # Attacks the animal with buffed item
            animal.hitpoints = animal.hitpoints - buffed_item.damage
            print(f"{self.name} with {self.hitpoints} hitpoints has attacked the {animal.name} with a {buffed_item.name} for {buffed_item.damage} damage!")
            if animal.hitpoints > 0:
                print(f"The {animal.name} has {animal.hitpoints} hitpoints remaining.")
                print("----------------------------------------------------------")
        elif player_power_up == "extra damage" and items == "buffed items":
        # For the rest of the attacks while using the extra damage power up, uses an item from the item list created above
            buffed_item: Item = random.choice(self.buffed_items)
            animal.hitpoints = animal.hitpoints - buffed_item.damage
            print(f"{self.name} with {self.hitpoints} hitpoints has attacked the {animal.name} with a {buffed_item.name} for {buffed_item.damage} damage!")
            if animal.hitpoints > 0:
                print(f"The {animal.name} has {animal.hitpoints} hitpoints remaining.")
                print("----------------------------------------------------------")
        else:
        # Normal attack without the power up
            item: Item = random.choice(self.items)
            animal.hitpoints = animal.hitpoints - item.damage
            print(f"{self.name} with {self.hitpoints} hitpoints has attacked the {animal.name} with a {item.name} for {item.damage} damage!")
            if animal.hitpoints > 0:
                print(f"The {animal.name} has {animal.hitpoints} hitpoints remaining.")
                print("----------------------------------------------------------")

# Starts the game
def play():
    # Game introduction
    game_introduction = '''
    Welcome to the Adventure Game!
    ------------------------------
    In this game there are 5 levels. Each level has 3 rooms, inside each there's a dangerous animal.
    Before every level you will choose if you want to use a power up.
    ---------------------------------------------------------------------
    You have 3 power ups that you can use throughout the game:
    1. Health boost: gives you 25% more health.
    2. Super agility: increases the chances that the animal will miss its attack by 25%.
    3. Extra damage: gives you 25% extra damage on all your weapons.
    You will only be able to use one power up per level.
    ---------------------------------------------------------------------
    Then you will choose which room and animal to fight.
    You will start out with a rock as your weapon.
    Each time you attack the animal you will use a random item from your inventory.
    When the animal attacks you, there's a 50% that it misses.
    When you complete a level you will get a new weapon.
    ---------------------------------------------------------------------
    If you kill all the animals you win!\n
    '''
    print(game_introduction)
    # Asks for your character's name.
    while True:
        player_name = input("Enter the name of your player: ")
        if len(player_name) > 0:
            # Creates the player object.
            player1 = Player(player_name, 200)
            break
        else:
            # If you don't type something, it asks again.
            print("Please enter a name.")

    # Makes the animals and rooms for level 1
    animal1_level1 = Animal("Dog", 40, 5, Item("hammer", 10))
    room1_level1 = Room("Grassland", animal1_level1)
    animal2_level1 = Animal("Snake", 20, 10, Item("knife", 12))
    room2_level1 = Room("Desert", animal2_level1)
    animal3_level1 = Animal("Coyote", 30, 7, Item("club", 15))
    room3_level1 = Room("Forest", animal3_level1)
    # Each room gets added to the level 1 rooms list.
    rooms_level1 = [room1_level1, room2_level1, room3_level1]

    # Makes the animals and rooms for level 2
    animal1_level2 = Animal("Kangaroo", 55, 17, Item("shovel", 20))
    room1_level2 = Room("Savanna", animal1_level2)
    animal2_level2 = Animal("Eagle", 45, 20, Item("baseball bat", 25))
    room2_level2 = Room("Arid Desert", animal2_level2)
    animal3_level2 = Animal("Orangutan", 65, 15, Item("crowbar", 22))
    room3_level2 = Room("Rainforest", animal3_level2)
    # Each room gets added to the level 2 rooms list.
    rooms_level2 = [room1_level2, room2_level2, room3_level2]

    # Makes the animals and rooms for level 3
    animal1_level3 = Animal("Wolf", 80, 27, Item("sickle", 30))
    room1_level3 = Room("Tundra", animal1_level3)
    animal2_level3 = Animal("Chimpanzee", 90, 25, Item("axe", 32))
    room2_level3 = Room("Woodland", animal2_level3)
    animal3_level3 = Animal("King Cobra", 70, 30, Item("chainsaw", 35))
    room3_level3 = Room("Swamp", animal3_level3)
    # Each room gets added to the level 3 rooms list.
    rooms_level3 = [room1_level3, room2_level3, room3_level3]

    # Makes the animals and rooms for level 4
    animal1_level4 = Animal("Leopard", 95, 40, Item("machete", 40))
    room1_level4 = Room("Mountains", animal1_level4)
    animal2_level4 = Animal("Bull", 105, 35, Item("mace", 45))
    room2_level4 = Room("Grassland", animal2_level4)
    animal3_level4 = Animal("Anaconda", 100, 37, Item("sword", 42))
    room3_level4 = Room("Swamp", animal3_level4)
    # Each room gets added to the level 4 rooms list.
    rooms_level4 = [room1_level4, room2_level4, room3_level4]

    # Makes the animals and rooms for level 5
    animal1_level5 = Animal("Polar Bear", 110, 50, Item("spear", 50))
    room1_level5 = Room("Arctic Sea", animal1_level5)
    animal2_level5 = Animal("Lion", 120, 45, Item("katana", 55))
    room2_level5 = Room("Grassland", animal2_level5)
    animal3_level5 = Animal("Gorilla", 115, 47, Item("tachi", 52))
    room3_level5 = Room("Tropical Rainforest", animal3_level5)
    # Each room gets added to the level 5 rooms list.
    rooms_level5 = [room1_level5, room2_level5, room3_level5]

    # All the rooms of each level
    rooms_per_lvl = [rooms_level1, rooms_level2, rooms_level3, rooms_level4, rooms_level5]
    # Adds an item to the player to be able to fight
    player1.items.append(Item("rock", 5))

    # Intiates kill counter and level number
    kill_counter = 0
    lvl = 1

    # Loops through every level
    for level in rooms_per_lvl:
        # Checks if player died from the last animal attack
        if player1.hitpoints > 0:
            while True:
                # Shows the status of the game like level, rooms and weapons
                print(f"\nYou are on level {lvl}.")
                print(f"Current hitpoints: {player1.hitpoints}")
                print(f"These are the animals in each room:")
                print(f"Room 1: {level[0].animal.name} in the {level[0].name}, Room 2: {level[1].animal.name} in the {level[1].name}, Room 3: {level[2].animal.name} in the {level[2].name}")
                print(f"These are your weapons: {player1.items}")
                if len(player1.power_ups) == 0:
                # Tells you if you have used all your power ups
                    print("You have no power ups remaining.")
                else:
                    # Shows your remaining power ups
                    print(f"These are your power ups: {[f"{i}. {player1.power_ups[i-1]}" for i in range(1, len(player1.power_ups)+1)]}")
                try:
                    # Checks if you've power ups remaining
                    if len(player1.power_ups) == 0:
                        break
                    # Asks if you want to use a power up
                    power_up_choice = int(input("Before you enter a room, do you want to use one of your power ups? If not, type 0: "))
                    # Checks if the number you entered is valid
                    if power_up_choice >= 0 and power_up_choice <= len(player1.power_ups):
                        if power_up_choice == 0:
                        # Uses no power up
                            power_up = None
                            print("You're not using any power ups this level.")
                        elif power_up_choice == 1:
                        # Uses the first power up in the list for current level
                            power_up = player1.power_ups[0]
                            print(f"You're using the {player1.power_ups[0]} power up for this level.")
                        elif power_up_choice == 2:
                        # Uses the second power up in the list for current level
                            power_up = player1.power_ups[1]
                            print(f"You're using the {player1.power_ups[1]} power up for this level.")
                        else:
                        # Uses the third power up in the list for current level
                            power_up = player1.power_ups[2]
                            print(f"You're using the {player1.power_ups[2]} power up for this level.")
                        break
                    else:
                        # Message if you entered an invalid number
                        print("That power up doesn't exist")
                        print("---------------------------")
                except:
                    # Message if you entered a string instead of a number
                    print("That is not a valid choice.")
                    print("---------------------------")
            while True:
                try:
                    # Asks the player to choose a room to go into
                    room_choice = int(input("Choose the room number you want to enter(1-3): "))
                    # Verifies that they chose a valid number
                    if room_choice > 0 and room_choice < 4:
                        if room_choice == 1:
                            room = level[0]
                        elif room_choice == 2:
                            room = level[1]
                        else:
                            room = level[2]
                        break
                    else:
                        # Message if player chose an invalid number
                        print("That room doesn't exist.")
                        print("------------------------")
                except:
                    # Message if player typed a string instead of a number
                    print("That is not a valid choice.")
                    print("---------------------------")
            # Shows the room the player entered
            player1.enter_room(room)
            lvl += 1
        else:
            break
        # Initializes variable that checks if the player uses the extra damage power up
        extra_damage_used = False
        while True:
            # Initializes variable that checks if the player activated the super agility power up
            super_agility_active = False
            # Checks if the player died from the last animal attack. Ends the game
            if player1.hitpoints <= 0:
                print(f"Unfortunately, you got slayed by the {room.animal.name}.")
                break
            # Checks if and which power up the player used
            if power_up == None:
            # If player chose none, the player attacks normally
                player1.attack(room.animal)
                time.sleep(1)
            elif power_up == "health boost":
            # If player chose health boost power up they get a 25% increase in their total hitpoints
                player1.hitpoints = player1.hitpoints * 1.25
                player1.power_ups.remove("health boost")
                player1.attack(room.animal)
                time.sleep(1)
            elif power_up == "super agility":
            # If player chose super agility power up, the animal has a 25% chance of hitting them, instead of 50%. 
            # Only for current level
                super_agility_active = True
                player1.attack(room.animal)
                time.sleep(1)
            else:
                if extra_damage_used:
                # If player has previously used extra damage power up, they use the enhanced items for the rest of the attacks
                # Only for current level
                    player1.attack(room.animal, "extra damage", "buffed items")
                else:
                    # If player chose extra damage power up they get a 25% damage increase in all their weapons
                    player1.attack(room.animal, "extra damage")
                    extra_damage_used = True
                time.sleep(1)
            # Checks if player has kille the animal
            if room.animal.hitpoints <= 0:
                # Adds the reward item to the player
                player1.items.append(room.animal.item)
                kill_counter += 1
                print(f"You killed the {room.animal.name}.")
                # Checks if player has killed the animal of the final room
                if kill_counter == len(rooms_per_lvl):
                    # Winner Message
                    print("Congratulations you won!! There's no more rooms left, you've beaten all the animals.")
                    break
                # Message if you beat an animal
                print(f"Congratulations! You got a new item in your inventory: {room.animal.item.name}")
                print("Enter the next level.")
                if power_up == "super agility" or power_up == "extra damage":
                # Disables the super agility or extra damage power up for the next level
                # Resets the current power up value
                    player1.power_ups.remove(power_up)
                    power_up = None
                break
            if super_agility_active:
            # If super agility power up is active, the animal has a 25% chance of hitting the player, instead of 50%. 
                room.animal.attack(player1, "super agility")
            else:
            # Normal animal attack
                room.animal.attack(player1)
            if power_up == "health boost":
            # If player used the health boost power up, it expires for the next attacks
                power_up = None
            time.sleep(1)
        
play()