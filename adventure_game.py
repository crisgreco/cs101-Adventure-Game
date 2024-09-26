import random

class Item:
    # To create an item give it a name and how much damage it does. 
    # Players collect items to attack monster. Every time a player kills a monster they get a new item
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

class Animal:
    
    def __init__(self, name, hitpoints, damage, item: Item) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.damage = damage
        self.item = item

    def attack(self, player):
        hit_or_miss = random.randint(1, 2)
        if hit_or_miss == 1:
            player.hitpoints = player.hitpoints - self.damage
            print(f"The {self.name} with {self.hitpoints} hitpoints has attacked {player.name} for {self.damage} damage!")
            print(f"{player.name} has {player.hitpoints} hitpoints remaining.")
        else:
            print(f"The {self.name} has missed {player.name}! No damage done!")

class Room:

    def __init__(self, name, animal: Animal) -> None:
        self.name = name
        self.animal = animal

class Player:
    
    def __init__(self, name, hitpoints) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.items: list[Item] = []

    def enter_room(self, room: Room):
        print(f"{self.name} has entered the {room.name} room...")

    def attack(self, animal: Animal):
        item: Item = random.choice(self.items)
        animal.hitpoints = animal.hitpoints - item.damage
        print(f"{self.name} with {self.hitpoints} hitpoints has attacked the {animal.name} for {item.damage} damage!")
        print(f"{animal.name} has {animal.hitpoints} hitpoints remaining")

def play():
    while True:
        player_name = input("Enter the name of your player: ")
        if len(player_name) > 0:
            player1 = Player(player_name, 100)
            break
        else:
            print("Please enter a name.")
    animal1 = Animal("Dog", 30, 5, Item("hammer", 10))
    room1 = Room("Forest", animal1)
    animal2 = Animal("Chimpanzee", 30, 5, Item("sword", 15))
    room2 = Room("Savanna", animal2)
    animal3 = Animal("King cobra", 100, 25, Item("sword", 40))
    room3 = Room("Rainforest", animal3)
    animal4 = Animal("Crocodile", 100, 25, Item("sword", 40))
    room4 = Room("Swamp", animal4)
    animal5 = Animal("Gorilla", 100, 25, Item("sword", 40))
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
                print("You lost")
                break
            player1.attack(room.animal)
            if room.animal.hitpoints <= 0:
                player1.items.append(room.animal.item)
                print(f"You killed the {room.animal.name}.")
                print(f"You got a new item: {room.animal.item.name}")
                print("Enter the next room.")
                break
            room.animal.attack(player1)
        

play()