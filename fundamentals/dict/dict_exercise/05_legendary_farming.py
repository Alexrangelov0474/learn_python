materials = {"shards": 0, "fragments": 0, "motes": 0}
won_legendary_item = False
legendary_item = ""
while not legendary_item:
    current_materials = input().split()
    for index in range(0, len(current_materials), 2):
        material = current_materials[index + 1].lower()
        quantity = int(current_materials[index])
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity
        if materials["shards"] >= 250:
            materials["shards"] -= 250
            won_legendary_item = True
            legendary_item = "Shadowmourne"
        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            won_legendary_item = True
            legendary_item = "Valanyr"
        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            won_legendary_item = True
            legendary_item = "Dragonwrath"
        if won_legendary_item:
            break

print(f"{legendary_item} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")