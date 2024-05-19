# import smtplib

# my_email = "aiman.ab.ghapar@gmail.com"
# password = "xiuq tivk ypwe kgkp"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="raigaex95@gmail.com", 
#         msg="Subject:Hello\n\nThis is body of my email"
#         )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()

# # print(year)
# # print(month)
# # print(day)
# # print(day_of_week)

# date_of_birth = dt.datetime(year=1995, month=8, day=20)
# print(date_of_birth)

# Challenge
import datetime as dt
import smtplib
import random

current_weekday = dt.datetime.now().weekday()

with open("Day-32-Smtp\quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    
quote = random.choice(all_quotes)

my_email = "aiman.ab.ghapar@gmail.com"
password = ""
if current_weekday == 6:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="raigaex95@gmail.com", 
            msg=f"Subject:Quote of the Day\n\n{quote}"
            )
