import re

patter = r'[#@]([A-Z][a-z]+)[#@]\(([A-Z][a-z]+)\)=(\d+)'
clans = {}

def team_exists_checker(clans_dict: dict, current_clan_name: str) -> bool:
    if current_clan_name in clans_dict:
        return True
    return False

def player_exists_checker(clans_dict: dict, current_clan_name: str, current_player_name: str) -> bool:
    if current_player_name in clans_dict[current_clan_name]:
        return True
    return False

while True:
    command = input()
    match = re.search(patter, command)
    if command == 'Build':
        break
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


def adding_player(clan_dict: dict, current_clan_name: str, current_player_name: str, current_score: int):
    if not team_exists_checker(clan_dict, current_clan_name):
        clan_dict[current_clan_name] = {}

    if not player_exists_checker(clan_dict, current_clan_name, current_player_name):
        clan_dict[current_clan_name][current_player_name] = current_score

def train_player(clan_dict: dict, current_clan_name: str, current_player_name: str, points_to_add: int):
    if team_exists_checker(clan_dict, current_clan_name) and player_exists_checker(clan_dict, current_clan_name, current_player_name):
        clan_dict[current_clan_name][current_player_name] += points_to_add

def kick_player(clan_dict: dict, current_clan_name: str, current_player_name: str):
    if team_exists_checker(clan_dict, current_clan_name):
        del clan_dict[current_clan_name][current_player_name]

    while True:
        current_command = input()
        if current_command == 'End':
            break

        current_command = current_command.split(' => ')
        action = current_command[0]
        clan_name = current_command[1]
        player_name = current_command[2]

        if action == 'Join':
            player_score = int(current_command[3])
            adding_player(clans, clan_name, player_name, player_score)

        elif action == 'Train':
            point = int(current_command[3])
            train_player(clans, clan_name, player_name, point)

        elif action == 'Kick':
            kick_player(clans, clan_name, player_name)
