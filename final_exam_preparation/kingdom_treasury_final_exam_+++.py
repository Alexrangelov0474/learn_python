import re

valid_resource = ['Gold', 'Wood', 'Stone', 'Food']
cities = {}

def resource_validation(resource_type: str) -> bool:
    return resource_type in valid_resource

def ensure_resource_exists(cities_dict:dict, city_name:str, resource_type:str) -> None:
    if resource_type not in cities_dict[city_name]:
        cities_dict[city_name][resource_type] = 0

def ensure_city_exists(cities_dict:dict, city_name:str) -> None:
    if city_name not in cities_dict.keys():
        cities_dict[city_name] = {}

def both_cities_exist(cities_dict: dict, first_city: str, second_city: str) -> bool:
    return first_city in cities_dict.keys() and second_city in cities_dict.keys()


pattern = r'([#@]([A-Z][A-Za-z]+)[#@])\(([A-Z][a-z]+)\)=(\d+)'
while True:
    cities_data = input()
    if cities_data == 'Build':
        break

    else:

        match = re.search(pattern,cities_data)
        if not match:
            continue

        first_group_sign = match.group(1)
        if first_group_sign[0] == '#':
            city = match.group(2)
            resource = match.group(3)
            amount = int(match.group(4))

        else:
            resource = match.group(2)
            city = match.group(3)
            amount = int(match.group(4))


        if resource_validation(resource):
            ensure_city_exists(cities, city)
            ensure_resource_exists(cities, city, resource)
            cities[city][resource] += amount

def gather_resource(cities_dict:dict, city_name:str,
                    resource_type:str, resource_amount:int) -> None:
    if not resource_validation(resource_type):
        return

    ensure_city_exists(cities_dict,city_name)
    ensure_resource_exists(cities_dict,city_name,resource_type)
    cities_dict[city_name][resource_type] += resource_amount

def spend_resource(cities_dict:dict, city_name:str,
                    resource_type:str, resource_amount:int) -> None:

    if city_name not in cities_dict.keys() or\
            resource_type not in cities_dict[city_name] or\
            resource_amount > cities_dict[city_name][resource_type]:
            return

    cities_dict[city_name][resource_type] -= resource_amount


def transfer_resource(cities_dict:dict, giver_city:str, taker_city:str,
                      resource_type:str, resource_amount:int) -> None:
    if not both_cities_exist(cities_dict, giver_city, taker_city):
        return

    if resource_type not in cities_dict[giver_city]:
        return

    if cities_dict[giver_city][resource_type] < resource_amount:
        return

    if resource_validation(resource_type):
        ensure_resource_exists(cities_dict, taker_city, resource_type)
        cities_dict[giver_city][resource_type] -= resource_amount
        cities_dict[taker_city][resource_type] += resource_amount



def upgrade_city(cities_dict:dict, city_name:str, resource_type:str) -> None:
    if city_name not in cities_dict.keys() \
            or resource_type not in cities_dict[city_name] \
            or not resource_validation(resource_type):
        return

    cities_dict[city_name][resource_type] *= 2


while True:
    command = input().split(' => ')
    if command[0] == 'End':
        break
    action = command[0]
    if action == 'Gather':
        city, resource, amount = command[1], command[2], int(command[3])
        gather_resource(cities ,city, resource, amount)
    elif action == 'Spend':
        city, resource, amount = command[1], command[2], int(command[3])
        spend_resource(cities, city, resource, amount)
    elif action == 'Transfer':
        from_city, to_city, resource, amount =\
            command[1], command[2], command[3], int(command[4])
        transfer_resource(cities, from_city, to_city, resource, amount)
    elif action == 'Upgrade':
        city, resource = command[1], command[2]
        upgrade_city(cities, city, resource)

sorted_cities = sorted(
    cities.items(),
    key=lambda current_city: (-sum(current_city[1].values()), current_city[0])
)

for city, resources in sorted_cities:

    total = sum(resources.values())
    print(f'{city} ({total})')

    sorted_resources = sorted(
        resources.items(),
        key=lambda current_resource: (-current_resource[1], current_resource[0])
    )

    for resource, amount in sorted_resources:
        print(f'- {resource}: {amount}')