hourly_pay = input('What is your hourly pay? ')

hours_week = input('How many hours do you work a week? ')

weekly_pay = float(hourly_pay) * float(hours_week)

annual_salary = float(weekly_pay) * 52.0

print('You make', annual_salary, 'a year.')
