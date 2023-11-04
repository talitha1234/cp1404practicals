"""
Project Management
Estimate: 4 hours
start:
end:
Actual:
"""

import datetime

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))