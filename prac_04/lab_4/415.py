from datetime import datetime, timedelta
import re
import math

def parse_date_with_offset(date_str):
    match = re.match(r'(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})', date_str)
    date_part, sign, h, m = match.groups()
    offset = int(h) * 60 + int(m)
    if sign == '-':
        offset = -offset
    return datetime.strptime(date_part, "%Y-%m-%d"), offset

def solve():
    # Парсим входные данные
    bd, bo = parse_date_with_offset(input().strip())
    cd, co = parse_date_with_offset(input().strip())
    
    # Текущий момент в UTC
    now_utc = cd - timedelta(minutes=co)
    
    # Месяц и день рождения (в часовом поясе рождения)
    bm, bd_day = bd.month, bd.day
    
    # Функция для получения дня рождения в заданном году (в UTC)
    def get_birthday_utc(year):
        # Обработка 29 февраля
        if bm == 2 and bd_day == 29:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                local = datetime(year, 2, 29)
            else:
                local = datetime(year, 2, 28)
        else:
            local = datetime(year, bm, bd_day)
        
        # Конвертируем в UTC
        return local - timedelta(minutes=bo)
    
    # Пробуем день рождения в текущем году
    bday_utc = get_birthday_utc(cd.year)
    
    if bday_utc >= now_utc:
        diff = bday_utc - now_utc
    else:
        bday_utc = get_birthday_utc(cd.year + 1)
        diff = bday_utc - now_utc
    
    # Округляем вверх до целых дней
    days = math.ceil(diff.total_seconds() / 86400)
    print(days)

if __name__ == "__main__":
    solve()