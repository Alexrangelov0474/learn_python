from collections import deque

substances = [int(x) for x in input().split(',')]
crystal_energy = deque([int(x) for x in input().split(',')])

potions = [
    ('Brew of Immortality', 110),
    ('Essence of Resilience', 100),
    ('Draught of Wisdom', 90),
    ('Potion of Agility', 80),
    ('Elixir of Strength', 70)
    ]

crafted_potions = []

while potions and substances and crystal_energy:
    substance = substances.pop()
    energy = crystal_energy.popleft()
    sum_material = substance + energy

    for potion in potions:
        if potion[1] == sum_material:
            potions.remove(potion)
            crafted_potions.append(potion[0])
            break
    else:
        for potion in potions:
            if potion[1] < sum_material:
                potions.remove(potion)
                crafted_potions.append(potion[0])

                if energy - 20 > 0:
                    crystal_energy.append(energy - 20)
                break
        else:
            if energy - 5 > 0:
                crystal_energy.append(energy - 5)


if not potions:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystal_energy:
    print(f"Crystals: {', '.join(map(str, crystal_energy))}")
