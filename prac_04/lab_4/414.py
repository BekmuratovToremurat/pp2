from datetime import datetime, timedelta, timezone
import sys

def parse_datetime(line):
    date_str, tz_str = line.strip().split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    dt = dt.replace(tzinfo=offset)
    return dt

dt1 = parse_datetime(sys.stdin.readline())
dt2 = parse_datetime(sys.stdin.readline())

utc1 = dt1.astimezone(timezone.utc)
utc2 = dt2.astimezone(timezone.utc)

diff_seconds = abs((utc1 - utc2).total_seconds())
diff_days = int(diff_seconds // 86400)
print(diff_days)