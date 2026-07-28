import re

def hero_exists(guilds_dict:dict, hero_name:str) -> bool:
    for guild_to_check in guilds_dict.keys():
        if hero_name in guilds_dict[guild_to_check]:
            return True
    return False

guilds = {}
guilds_data = input()
pattern = r'([@%])([A-Z][A-Za-z]{2,})\1\[([A-Z][A-Za-z]{2,})\]:(\d+)'
for match in re.finditer(pattern, guilds_data):
    guild = match.group(2)
    hero = match.group(3)
    level = int(match.group(4))

    if guild not in guilds.keys():
        guilds[guild] = {}
    if not hero_exists(guilds, hero):
        guilds[guild][hero] = level

def add_hero(guilds_dict:dict, guild_name:str, hero_name:str, hero_level:int) -> None:
    if guild_name in guilds_dict.keys() and hero_name not in guilds_dict[guild_name].keys():
        if not hero_exists(guilds_dict, hero_name):
            guilds_dict[guild_name][hero_name] = hero_level

def remove_hero(guilds_dict:dict, guild_name:str, hero_name:str) -> None:
    if guild_name in guilds_dict.keys() and hero_name in guilds_dict[guild_name]:
       del guilds_dict[guild_name][hero_name]

def levelup_hero(guilds_dict:dict, guild_name:str, hero_name:str, level_up_amount:int) -> None:
    if guild_name in guilds_dict.keys() and hero_name in guilds_dict[guild_name]:
        guilds_dict[guild_name][hero_name] += level_up_amount

def transfer_hero(guilds_dict:dict, old_guild_name:str, new_guild_name:str, hero_name:str) -> None:
    if (
        old_guild_name in guilds_dict
        and new_guild_name in guilds_dict
        and hero_name in guilds_dict[old_guild_name]
        and hero_name not in guilds_dict[new_guild_name]
    ):
        hero_to_move = guilds_dict[old_guild_name].pop(hero_name)
        guilds_dict[new_guild_name][hero_name] = hero_to_move

while True:
    command = input().split(':')
    if command[0] == 'End':
        break
    action = command[0]
    if action == 'Add':
        guild = command[1]
        hero = command[2]
        level = int(command[3])
        add_hero(guilds,guild,hero,level)
    elif action == 'Remove':
        guild = command[1]
        hero = command[2]
        remove_hero(guilds, guild, hero)

    elif action == 'LevelUp':
        guild = command[1]
        hero = command[2]
        amount_level = int(command[3])
        levelup_hero(guilds, guild, hero, amount_level)

    elif action == 'Transfer':
        old_guild = command[1]
        new_guild = command[2]
        hero = command[3]
        transfer_hero(guilds, old_guild, new_guild, hero)

for current_guild, guild_data in guilds.items():
    print(f'{current_guild}:')
    for current_hero_name, current_hero_level in guild_data.items():
        print(f'- {current_hero_name} -> {current_hero_level}')
