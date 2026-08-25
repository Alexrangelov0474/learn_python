import re

def guild_exists(current_guild_name : str, guilds_and_heroes_dict: dict) -> bool:
    if current_guild_name not in guilds_and_heroes_dict:
        return False
    return True

def hero_exists(current_guild_name : str, current_hero_name: str, guilds_and_heroes_dict: dict) -> bool:
    if current_hero_name not in guilds_and_heroes_dict[current_guild_name]:
        return False
    return True

pattern = r'[#@]([A-Z]+[a-zA-Z]+)[#@]\(([A-Z]+[a-zA-Z]+)\)=(\d+)'
guilds_and_heroes = {}
while True:
    command = input()
    if command == 'Build':
        break

    match = re.search(pattern, command)
    if match:
        if command[0] == '#':
            guild_name = match.group(1)
            hero_name = match.group(2)
            level = int(match.group(3))
        else:
            guild_name = match.group(2)
            hero_name = match.group(1)
            level = int(match.group(3))

        if not guild_exists(guild_name, guilds_and_heroes) :
            guilds_and_heroes[guild_name] = {}

        if not hero_exists(guild_name, hero_name, guilds_and_heroes):
            guilds_and_heroes[guild_name][hero_name] = level

def add_hero_to_guild(current_guild_name:str, current_hero_name:str, current_level: int, guilds_and_heroes_dict: dict):
    if hero_exists(current_guild_name, current_hero_name, guilds_and_heroes_dict):
        guilds_and_heroes_dict[current_guild_name][current_hero_name] = current_level

def levelup_hero(current_guild_name:str, current_hero_name:str, current_level: int, guilds_and_heroes_dict: dict):
    if hero_exists(current_guild_name, current_hero_name, guilds_and_heroes_dict):
        guilds_and_heroes_dict[current_guild_name][current_hero_name] += current_level

def remove_hero(current_guild_name:str, current_hero_name:str, guilds_and_heroes_dict: dict):
    if hero_exists(current_guild_name, current_hero_name, guilds_and_heroes_dict):
        del guilds_and_heroes_dict[current_guild_name][current_hero_name]


while True:
    command = input().split(' => ')
    if command[0] == 'End':
        break

    elif command[0] == 'Join':
        guild_name = command[1]
        hero_name = command[2]
        level = int(command[3])
        add_hero_to_guild(guild_name,hero_name, level, guilds_and_heroes)

    elif command[0] == 'LevelUp':
        guild_name = command[1]
        hero_name = command[2]
        level = int(command[3])
        levelup_hero(guild_name,hero_name, level, guilds_and_heroes)

    elif command[0] == 'Leave':
        guild_name = command[1]
        hero_name = command[2]
        remove_hero(guild_name, hero_name, guilds_and_heroes)

# Следващата стъпка: Сортиране и отпечатване
