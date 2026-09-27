total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

film_name = input()

while film_name != 'Finish':
    free_space = int(input())
    sold_for_film = 0

    while True:
        ticket_type = input()
        if ticket_type == 'End':
            break

        sold_for_film += 1
        total_tickets += 1
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

        if sold_for_film == free_space:
            break

    percent_full = sold_for_film / free_space * 100
    print(f"{film_name} - {percent_full:.2f}% full.")
    film_name = input()

student_percent = student_tickets / total_tickets * 100
standard_percent = standard_tickets / total_tickets * 100
kids_percent = kids_tickets / total_tickets * 100

print(f'Total tickets: {total_tickets}')
print(f'{student_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kids_percent:.2f}% kids tickets.')

