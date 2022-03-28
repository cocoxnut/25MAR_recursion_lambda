from datetime import datetime as data
now = data(2022, 3, 25)
this_year = data(2022, 1, 1)
next_year = data(2023, 1, 1)
#passed_days = now - this_year
#days_left = next_year - now
#print(str(passed_days)[0:8], 'passed from 01 Jan 2022')
#print(str(days_left)[0:8], 'remain till 01 Jan 2023')

p_days = lambda now, this_year: print(f'{now - this_year}, passed from 01 Jan 2022')
days_l = lambda now, next_year: print(f'{next_year - now}, remain till 01 Jan 2023')
p_days(now, this_year)
days_l(next_year, now)
