import random

characters = [
    {"name": "Warrrior", "stats": (100, 20, 10)},  # HP, ATK, DEF
    {"name": "Mage", "stats": (80, 25, 5)},
    {"name": "Archer", "stats": (90, 18, 8)},
]

options = (1, 2)  # Attack, Defend (Options for the computer)

# Print the list of characters
print("Choose your character:")
for i in range(len(characters)):
    print(f"{i + 1}. {characters[i]['name']}")

# Assign the player's character and stats
choice = int(input("Enter the number of the character: ")) - 1
player = characters[choice]
player_hp = player["stats"][0]
player_atk = player["stats"][1]
player_def = player["stats"][2]

# Assign the enemy's character and stats
enemy = random.choice(characters)
enemy_hp = enemy["stats"][0]
enemy_atk = enemy["stats"][1]
enemy_def = enemy["stats"][2]

print(f"\nYou have chosen the {player['name']}.")
print(f"Your opponent is the {enemy['name']}.\n")

while player_hp > 0 and enemy_hp > 0:
    # Player turn
    print("Your turn. What do you want to do?")
    print("1. Attack")
    print("2. Defend")
    player_opt = int(input("Choose an option (1 or 2): "))

    # Enemy turn (random choice)
    enemy_opt = random.choice(options)

    # Resolution of the turn based on options
    # Both attack
    if player_opt == 1 and enemy_opt == 1:
        print("\nBoth characters attacks. Both receive damage.\n")
        enemy_hp -= player_atk
        player_hp -= enemy_atk

    # Player attacks, enemy defends
    elif player_opt == 1 and enemy_opt == 2:
        print("\nPlayer attacks, Enemy defends. Damage received by Enemy is lowered.\n")
        damage = player_atk - (enemy_def * 0.5)
        enemy_hp -= damage

    # Player defends, enemy attacks
    elif player_opt == 2 and enemy_opt == 1:
        print(
            "\nPlayer defends, Enemy attacks. Damage received by Player is lowered.\n"
        )
        damage = enemy_atk - (player_def * 0.5)
        player_hp -= damage

    # Both defend: no damage
    else:
        print("\nBoth defend. No damage this turn.\n")

    # Show current state
    if player_hp <= 0:
        player_hp = 0

    if enemy_hp <= 0:
        enemy_hp = 0

    print(f"HP of {player['name']}: {player_hp} (Player)")
    print(f"HP of {enemy['name']}: {enemy_hp} (Enemy)\n")

# Final result
if player_hp > 0:
    print(f"Congratulations! You have defeated the {enemy['name']}.")
else:
    print(f"You have been defeated by the {enemy['name']}. Enjoy the next one!")
