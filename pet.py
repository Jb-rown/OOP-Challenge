# OOP Challenge: Pet Class
# This is a simple implementation of a pet class in Python.
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"Creating pet: {self.name}")

    def eat(self):
        print(f"🍖 {self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"💤 {self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy > 0:  # Check if the pet has enough energy to play
            print(f"{self.name} is playing...")
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(5, self.hunger + 1)
        else:
            print(f"{self.name} is too tired to play!")

    def get_status(self):
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        if self.tricks:
            print(f"Tricks: {self.tricks}")
        else:
            print("No tricks learned yet.")

    def train(self, trick):
        print(f"{self.name} learned a new trick: {trick}!")
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {self.tricks}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def groom(self):
        print(f'{self.name} is being groomed.')
        self.happiness = min(10, self.happiness + 2)
        print(f'{self.name}\'s happiness increased!')