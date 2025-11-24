#datetime module to obtain today's date
from datetime import datetime, timedelta

current_date = datetime.today()
#print(current_date)

def display_current_datetime():
    current_date = datetime.now().time()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    
display_current_datetime()

def calculate_future_date():
    days= int(input("enter number of days"))
    future_date = current_date+timedelta(days)
    print (future_date.strftime("%Y-%m-%d"))
    
calculate_future_date()

