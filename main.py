from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Bosko")

     # Test the pet's functionality
    print("Welcome to the Digital Pet Simulator!")
    my_pet.get_status()

    # Test eating
    my_pet.eat()
    my_pet.get_status()

    # Test playing
    my_pet.play()
    my_pet.get_status()
    print()

    # Test grooming
    my_pet.groom()
    my_pet.get_status()
    print()
    
    # Test sleeping
    my_pet.sleep()
    my_pet.get_status()
    print()

    # Test training and showing tricks
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.train("Sit")
    my_pet.show_tricks()
    print()

    my_pet.get_status()

if __name__ == "__main__":
    main()
