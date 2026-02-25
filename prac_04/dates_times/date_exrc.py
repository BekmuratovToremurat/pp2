#Subtract five days from current date
from datetime import datetime, timedelta

# Current date
today = datetime.now()

# Subtract 5 days
new_date = today - timedelta(days=5)

print("Current date:", today)
print("Date 5 days ago:", new_date)


#Print yesterday, today, tomorrow
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())



#Drop microseconds from datetime
from datetime import datetime

now = datetime.now()

# Remove microseconds
no_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", no_microseconds)



#Calculate difference between two dates in seconds
from datetime import datetime

date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 25, 15, 30, 0)

difference = date2 - date1

# Total seconds
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)


