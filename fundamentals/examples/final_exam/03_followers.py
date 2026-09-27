followers = {}

def username_not_exist(followers_dict: dict, current_username:str) -> bool:
    return current_username not in followers_dict.keys()

while True:
    line = input()
    if line == 'Log out':
        break
    command = line.split(': ')

    action, username = command[0], command[1]

    if action == 'New follower':
        if username_not_exist(followers, username):
            followers[username] = 0


    elif action == 'Like':
        count = int(command[2])
        if username_not_exist(followers, username):
            followers[username] = count
        else:
            followers[username] += count

    elif action == 'Comment':
        if username_not_exist(followers, username):
            followers[username] = 1
        else:
            followers[username] += 1

    elif action == 'Blocked':
        if username_not_exist(followers, username):
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

new_followers = len(followers)
print(f'{new_followers} followers')
for username, likes_and_comments in followers.items():
    print(f'{username}: {likes_and_comments}')

