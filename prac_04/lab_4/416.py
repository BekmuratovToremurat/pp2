from datetime import datetime, timedelta, timezone
import sys

def parse_datetime(line):
    parts = line.strip().split()
    dt_str = " ".join(parts[:2])
    tz_str = parts[2]
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    dt = dt.replace(tzinfo=offset)
    return dt

start = parse_datetime(sys.stdin.readline())
end = parse_datetime(sys.stdin.readline())

start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

duration = int((end_utc - start_utc).total_seconds())
print(duration)