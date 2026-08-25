import re

patter = r'[#@]([A-Z][a-z]+)[#@]\(([A-Z][a-z]+)\)=(\d+)'
clans = {}

def team_exists_checker(clans_dict: dict, clan_name: str) -> bool:
    if clan_name in clans_dict:
        return True
    return False

def player_exists_checker(clans_dict: dict, clan_name: str, player_name: str) -> bool:
    if player_name in clans_dict[clan_name]:
        return True
    return False


while True:
    command = input()
    match = re.search(patter, command)
    if match:
        if command[0] == '#':
            clan = match.group(1)
            player = match.group(2)
            score = int(match.group(3))
        else:
            clan = match.group(2)
            player = match.group(1)
            score = int(match.group(3))

        if not team_exists_checker(clans, clan):
            clans[clan] = {}

        if not player_exists_checker(clans, clan, player):
            clans[clan][player] = score

