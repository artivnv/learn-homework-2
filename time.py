import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')
from datetime import datetime, date, timedelta

dt_today = datetime.now()
print(f'Сегодняшняя дата:', dt_today.strftime('%d %B %Y'))
dt_yesterday = dt_today - timedelta(days = 1)
print(f'Вчерашняя дата:', dt_yesterday.strftime('%d %B %Y'))
month_ago = dt_today - timedelta(days = 31)
print(f'Месяц назад:', month_ago.strftime('%d %B %Y'))

dt = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(dt, '%d/%m/%Y %H:%M:%S.%f')
print(date_dt)