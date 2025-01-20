import random

# Defining the weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    # Saving the random roll into a variable
    weaponRoll = random.randint(1,6)

    heroWeapon = weapons[weaponRoll - 1]
    print(f"Your weapon is {heroWeapon}.")

    heroCombatStrength = 20
    heroCombatStrength += weaponRoll

#Printing the possibilities
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    if heroWeapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")
        
except IndexError:
    print("Error: Weapon roll is out of bounds.")

