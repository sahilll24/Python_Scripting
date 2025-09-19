import time
from datetime import datetime

for i in range(5):
    now = datetime.now()
    print(f"Current Time :- ",now.strftime('%H:%M:%S'))
    time.sleep(1)