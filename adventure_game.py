import random

class Item:
    # To create an item give it a name and how much damage it does. 
    # Players collect items to attack the animal. Every time a player kills an animal they get a new item
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

class Animal:
    # To create an animal specify its name, hitpoints, damage and reward item.
    def __init__(self, name, hitpoints, damage, item: Item) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.item = item

    # Attacks the player. There is a 50% chance the animal misses.
    def attack(self, player):
        hit_or_miss = random.randint(1, 2)
        if hit_or_miss == 1:
            player.hitpoints = player.hitpoints - self.damage
            print(f"The {self.name} with {self.hitpoints} hitpoints has attacked {player.name} for {self.damage} damage!")
            if player.hitpoints > 0:
                print(f"{player.name} has {player.hitpoints} hitpoints remaining.")
        else:
            print(f"The {self.name} has missed {player.name}! No damage done!")

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

    # Shows which room the player enters.
    def enter_room(self, room: Room):
        print(f"{self.name} has entered the {room.name} room...")

    # Player attacks the animal with a random item from their items list.
    def attack(self, animal: Animal):
        item: Item = random.choice(self.items)
        animal.hitpoints = animal.hitpoints - item.damage
        print(f"{self.name} with {self.hitpoints} hitpoints has attacked the {animal.name} with a {item.name} for {item.damage} damage!")
        if animal.hitpoints > 0:
            print(f"{animal.name} has {animal.hitpoints} hitpoints remaining")

# Starts the game
def play():
    while True:
        player_name = input("Enter the name of your player: ")
        if len(player_name) > 0:
            player1 = Player(player_name, 200)
            break
        else:
            print("Please enter a name.")
    animal1 = Animal("Dog", 30, 5, Item("hammer", 10))
    room1 = Room("Forest", animal1)
    animal2 = Animal("Chimpanzee", 40, 8, Item("dagger", 15))
    room2 = Room("Savanna", animal2)
    animal3 = Animal("King cobra", 55, 15, Item("pickaxe", 25))
    room3 = Room("Rainforest", animal3)
    animal4 = Animal("Crocodile", 75, 25, Item("sword", 35))
    room4 = Room("Swamp", animal4)
    animal5 = Animal("Gorilla", 100, 35, Item("katana", 40))
    room5 = Room("Mountain Forest", animal5)

    rooms = [room1, room2, room3, room4, room5]
    player1.items.append(Item("rock", 5))

    for room in rooms:
        if player1.hitpoints > 0:
            player1.enter_room(room)
        else:
            break
        while True:
            if player1.hitpoints <= 0:
                print(f"Unfortunately, you got slayed by the {room.animal.name}.")
                break
            player1.attack(room.animal)
            if room.animal.hitpoints <= 0:
                player1.items.append(room.animal.item)
                print(f"You killed the {room.animal.name}.")
                if room.name == rooms[-1].name:
                    print("Congratulations you won!! There's no more rooms left, you've beaten all the animals.")
                    break
                print(f"Congratualtions! You got a new item in your inventory: {room.animal.item.name}")
                print("Enter the next room.")
                break
            room.animal.attack(player1)
        
play()