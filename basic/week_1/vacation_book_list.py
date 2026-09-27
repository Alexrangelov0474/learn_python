from math import floor

total_pages = int(input(f'pages in the book: '))
pages_per_hour = int(input(f'pages per hour: '))
days_for_reading = int(input(f'days for reading: '))

total_reading_time = total_pages / pages_per_hour
hours_per_day = total_reading_time / days_for_reading

print (floor(hours_per_day))
