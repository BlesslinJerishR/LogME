# importing
import datetime as dt
from datetime import date

born_day = date(2000, 12, 3)
today = date.today()
days_alive = today - born_day
date = dt.date.today()
day = dt.date.today().day
month = dt.date.today().month
year = dt.date.today().year
hour = dt.datetime.today().now().hour
mins = dt.datetime.today().now().minute
secs = dt.datetime.today().now().second

