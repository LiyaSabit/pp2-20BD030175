"""
from datetime import date, timedelta
res = date.today() - timedelta(5)
print("5 days before it was", res)
"""
"""
from datetime import date, timedelta
yes = date.today() - timedelta(1)
today = date.today() 
tomorrow = date.today() + timedelta(1)
print(yes)
print(today)
print(tomorrow)
"""
"""
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
"""
"""
from datetime import datetime, time
a = datetime.strptime('2023-02-20 12:25:00', '%Y-%m-%d %H:%M:%S')
b = datetime.now()
diff = b - a
res = diff.days * 24 * 3600 + diff.seconds
print(res)
"""
