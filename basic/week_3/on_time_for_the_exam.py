exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

diff = exam_time - arrival_time

if diff < 0 :
    print ('Late')
elif 0 <= diff <= 30:
    print('On time')
else:
    print ('Early')

hours = abs(diff) // 60
minutes = abs(diff) % 60

if diff > 0:
    if diff < 60:
        print (f'{minutes} minutes before the start')
    else:
        print(f'{hours}:{minutes:02d} hours before the start')
if diff < 0:
    if abs(diff) < 60:
        print(f'{minutes} minutes after the start')
    else:
        print(f'{hours}:{minutes:02d} hours after the start')