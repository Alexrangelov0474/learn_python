username = input()
password = input()

while True:
    new_password = input()
    if new_password != password:
        new_password = input()
        print(f'Welcome {username}!')
        break
